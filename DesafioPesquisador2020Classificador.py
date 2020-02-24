import pandas as pd
import string
import nltk
from nltk import stem
from nltk.corpus import stopwords

stemmer = stem.SnowballStemmer('english')
stopwords = set(stopwords.words('english'))

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from math import log, sqrt

#nltk.download('stopwords')
#nltk.download('punkt')

pd.options.mode.chained_assignment = None

df = pd.read_csv('sms_senior.csv', encoding='unicode_escape', parse_dates=['Date'])
df.head()

emails = df[['Full_Text', 'IsSpam']]

spam_words = ' '.join(list(emails[emails['IsSpam'] == 'yes']['Full_Text']))
spam_wc = WordCloud(width = 512, height = 512).generate(spam_words)

## Criando imagem das palavras mais usadas em spam
plt.figure(figsize = (10,8), facecolor='k')
plt.imshow(spam_wc)
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

## Classificação do texto

def process_msg(msg):
    msg = msg.lower()

    #remove os stopword
    msg = [word for word in msg.split() if word not in stopwords]

    #retorna as palavras a seus radicais
    msg = " ".join([stemmer.stem(word) for word in msg])

    return msg

emails['Full_Text'] = emails['Full_Text'].apply(process_msg)

from sklearn.model_selection import train_test_split

#treina com os dados csv
X_train, X_test, y_train, y_test = train_test_split(emails['Full_Text'], emails['IsSpam'], test_size = 0.1, random_state = 1)

from sklearn.feature_extraction.text import TfidfVectorizer

#realiza o calculo de frequência do termo–inverso da frequência nos documentos
vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train)

from sklearn import svm

svm = svm.SVC(C=1000)


svm.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix

X_test = vectorizer.transform(X_test)

y_pred = svm.predict(X_test)

print(confusion_matrix(y_test, y_pred))

def pred(msg):
    msg = vectorizer.transform([msg])
    prediction = svm.predict(msg)
    print(prediction[0])
    return prediction[0]

pred("Urgent! call 09061749602 from Landline. Your complimentary 4* Tenerife Holiday or £10,000 cash await collection SAE T&Cs BOX 528 HP20 1YF 150ppm 18+")
