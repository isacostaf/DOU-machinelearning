# DOU-machinelearning

## 🧠 Como interpretar

### ✔️ Precision (Precisão)
Indica o quanto o modelo acerta **quando decide por uma classe**.

- `1.00` → todas as previsões estão corretas  
- `0.50` → metade das previsões estão erradas  

👉 Exemplo:  
Para `nao_representacao`, precision = 1.00  
→ sempre que o modelo disse que era “não representação”, ele acertou.

---

### ✔️ Recall (Revocação)
Indica o quanto o modelo consegue **encontrar todos os exemplos reais de uma classe**.

- `1.00` → encontrou todos  
- `0.33` → encontrou poucos  

👉 Exemplo:  
Para `nao_representacao`, recall = 0.33  
→ de 3 casos reais, só identificou 1.

---

### ✔️ F1-score
Média entre precision e recall.

- Mede o equilíbrio entre acertar e encontrar os casos  
- Quanto mais próximo de 1, melhor  

---

### ✔️ Support
Quantidade real de exemplos daquela classe no teste.

- `nao_representacao`: 3 documentos  
- `representacao`: 2 documentos  

---

### ✔️ Accuracy (Acurácia)
Percentual total de acertos do modelo.

- `0.60` → acertou 3 de 5 documentos  

---

### ✔️ Macro avg
Média simples entre as classes (cada classe tem o mesmo peso).

---

### ✔️ Weighted avg
Média ponderada pelo número de exemplos de cada classe.
## 1.0
                         precision    recall  f1-score   support
    nao_representacao       1.00      0.33      0.50         3
        representacao       0.50      1.00      0.67         2

             accuracy                           0.60         5
            macro avg       0.75      0.67      0.58         5
         weighted avg       0.80      0.60      0.57         5

## 2.0
                           precision    recall  f1-score   support
      nao_representacao       0.75      1.00      0.86         3
          representacao       1.00      0.50      0.67         2
      
               accuracy                           0.80         5
              macro avg       0.88      0.75      0.76         5
           weighted avg       0.85      0.80      0.78         5

## 3.0
                         precision    recall  f1-score   support
    nao_representacao       1.00      1.00      1.00         4
        representacao       1.00      1.00      1.00         3
    
             accuracy                           1.00         7
            macro avg       1.00      1.00      1.00         7
         weighted avg       1.00      1.00      1.00         7
