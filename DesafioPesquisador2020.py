import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

df = pd.read_csv('sms_senior.csv', encoding='unicode_escape', parse_dates=['Date'])

wordsData = df.loc[:,"got":"wan"]

sumData = {}
nameData = {}
for col in wordsData:
    nameData[col] = col
    sumData[col] = sum(wordsData[col])

listName = list(nameData.values())
listSum = list(sumData.values())

##1 - criando o gráfico de barras
pos = arange(len(listName)) + .5

##barh(pos, listSum, align='center', color='#b8ff5c')
##yticks(pos, listName)
##xlabel('Contagem de Palavras')
##ylabel('Palavras')
##title('Grafico de frequência de palavras')
##grid(True)
#show()

##2 - Agrupar por ano e mes
dados = df.loc[:,"Word_Count":]

dp = pd.DataFrame(data=dados)

dp['Date'] = dp['Date'].astype('datetime64')

dp = dp.sort_values(['Date'])

dp['mesAno'] = dp['Date'].map(lambda x: 100*x.year + x.month)
dp['IsSpam'] = dp['IsSpam'].map({'no':0, 'yes':1})
dp['IsNotSpam'] = dp['IsSpam'].map(lambda x: x==0 ).astype('int')

dp = dp.groupby(['mesAno']).sum().reset_index()

dp1 = dp.loc[:, dp.columns != 'Date']
dp1 = dp.loc[:, dp.columns != 'Word_Count']

#dp1.plot(x = 'mesAno', y = ['IsSpam','IsNotSpam'], kind = 'bar')
#plt.show()

##3 -
print('Valor máximo do Word_Count: ' + str(max(dp['Word_Count'])))
print('Valor minímo do Word_Count: ' + str(min(dp['Word_Count'])))
##print('Média do Word_Count no mês de Janeiro: ' + str(dp['Word_Count'][0]/3))
##print('Mediana do Word_Count no mês de Janeiro: ' + str(dp['Word_Count'][0]/3))
##print('Desvio Padrão do Word_Count no mês de Janeiro: ' + str(dp['Word_Count'][0]/3))
##print('Variância do Word_Count no mês de Janeiro: ' + str(dp['Word_Count'][0]/3))

##4 - dia de cada mes que possui a maior sequencia de mensagens comuns/não spam


#Segunda Etapa
##Classificar as mensagens por algoritmo proprio
