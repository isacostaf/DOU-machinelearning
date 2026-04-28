const express = require("express");
const multer = require("multer");
const fs = require("fs");
const pdf = require("pdf-parse");

const app = express();
const upload = multer({ dest: "uploads/" });

// carregar modelo
const data = JSON.parse(fs.readFileSync("model.json"));

const vocab = data.vocab;
const idf = data.idf;
const model = data.model;
const stopwords = new Set(data.stopwords);

// -------- preprocess --------
function tokenize(text) {
  return text
    .toLowerCase()
    .replace(/[^\w\s]/g, "")
    .split(/\s+/)
    .filter(w => w && !stopwords.has(w));
}

// -------- TF-IDF --------
function vectorize(text) {
  const tokens = tokenize(text);
  const vec = new Array(idf.length).fill(0);

  tokens.forEach(t => {
    if (vocab[t] !== undefined) {
      vec[vocab[t]] += 1;
    }
  });

  return vec.map((tf, i) => tf * idf[i]);
}

// -------- Naive Bayes --------
function predict(vec) {
  let bestClass = null;
  let bestScore = -Infinity;

  model.classes.forEach((cls, cIndex) => {
    let score = model.class_log_prior[cIndex];

    vec.forEach((v, i) => {
      if (v > 0) {
        score += v * model.feature_log_prob[cIndex][i];
      }
    });

    if (score > bestScore) {
      bestScore = score;
      bestClass = cls;
    }
  });

  return bestClass;
}

// -------- rota --------
app.post("/upload", upload.single("file"), async (req, res) => {
  const buffer = fs.readFileSync(req.file.path);
  const dataPdf = await pdf(buffer);

  const texto = dataPdf.text;

  const vec = vectorize(texto);
  const result = predict(vec);

  res.send({ resultado: result });

  fs.unlinkSync(req.file.path);
});

// -------- front simples --------
app.get("/", (req, res) => {
  res.send(`
    <h2>Upload PDF</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
      <input type="file" name="file"/>
      <button type="submit">Enviar</button>
    </form>
  `);
});

app.listen(3001, () => console.log("http://localhost:3000"));