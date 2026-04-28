import os
from flask import Flask, request, render_template_string
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

app = Flask(__name__)

# -------- FUNÇÃO PDF --------
def extrair_texto_pdf(caminho):
    texto = ""
    try:
        reader = PdfReader(caminho)
        for page in reader.pages:
            texto += page.extract_text() or ""
    except:
        pass
    return texto


# -------- TREINAMENTO (igual seu notebook) --------
texts = []
labels = []

base_path = "/Users/isacosta/Documents/M. Defesa/Representacoes-ML"

for label in ["representacao", "nao_representacao"]:
    pasta = os.path.join(base_path, label)
    
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".pdf"):
            caminho = os.path.join(pasta, arquivo)
            texto = extrair_texto_pdf(caminho)
            
            texts.append(texto)
            labels.append(label)

stopwords_pt = stopwords.words('portuguese')

vectorizer = TfidfVectorizer(stop_words=stopwords_pt)
X_vec = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X_vec, labels)


# -------- FRONT SIMPLES --------
HTML = """
<!doctype html>
<title>Classificador de PDF</title>
<h2>Enviar PDF</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Enviar>
</form>

{% if resultado %}
<h3>Resultado: {{ resultado }}</h3>
{% endif %}
"""


# -------- ROTA --------
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    resultado = None

    if request.method == 'POST':
        file = request.files['file']
        
        if file:
            caminho = "temp.pdf"
            file.save(caminho)

            texto = extrair_texto_pdf(caminho)
            texto_vec = vectorizer.transform([texto])

            pred = model.predict(texto_vec)[0]
            resultado = pred

            os.remove(caminho)

    return render_template_string(HTML, resultado=resultado)


# -------- RODAR --------
if __name__ == '__main__':
    app.run(debug=True)