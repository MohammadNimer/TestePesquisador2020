import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

df = pd.read_csv('sms_senior.csv', encoding='unicode_escape', parse_dates=['Date'])

wordsData = df.loc[1:,"got":"wan"]

sumData = {}
nameData = {}
for col in wordsData:
    nameData[col] = col
    sumData[col] = sum(wordsData[col])

listName = list(nameData.values())
listSum = list(sumData.values())

##criando o gráfico de barras
pos = arange(len(listName)) + .5

barh(pos, listSum, align='center', color='#b8ff5c')
yticks(pos, listName)
xlabel('Contagem de Palavras')
ylabel('Palavras')
title('Grafico de frequência de palavras')
grid(True)
show()

