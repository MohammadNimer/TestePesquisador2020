import pandas as pd
import matplotlib.pyplot as plt
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

barh(pos, listSum, align='center', color='#b8ff5c')
yticks(pos, listName)
xlabel('Contagem de Palavras')
ylabel('Palavras')
title('Grafico de frequência de palavras')
grid(True)
show()

##2 - Agrupar por ano e mes
dados = df.loc[:,"Common_Word_Count":]

group = pd.DataFrame(data=dados)

group['Date'] = group['Date'].astype('datetime64')

group['mesAno'] = group['Date'].map(lambda x: 100*x.year + x.month)
group['IsSpam'] = group['IsSpam'].map({'no':0, 'yes':1})
group['IsNotSpam'] = group['IsSpam'].map(lambda x: x==0 ).astype('int')

group = group.groupby(['mesAno']).sum().reset_index()

groupFiltered = group.loc[:, group.columns != 'Date']
groupFiltered = group.loc[:, group.columns != 'Word_Count']
groupFiltered = group.loc[:, group.columns != 'Common_Word_Count']

groupFiltered.plot(x = 'mesAno', y = ['IsSpam','IsNotSpam'], kind = 'bar')
plt.show()

print('########## --------------------------------- ##########')
##3 - Calculos estatisticos

de = pd.DataFrame(data=dados)

de['Date'] = de['Date'].astype('datetime64')
de['Date'] = pd.to_datetime(df['Date']).dt.normalize()

de['mesAno'] = de['Date'].map(lambda x: 100*x.year + x.month)
de = de.loc[:, de.columns != 'IsSpam']

deFilterMax = de['Word_Count'].groupby(de['mesAno']).max()
deFilterMin = de['Word_Count'].groupby(de['mesAno']).min()
deFilterMean = de['Word_Count'].groupby(de['mesAno']).mean()
deFilterMedian = de['Word_Count'].groupby(de['mesAno']).median()
deFilterStd = de['Word_Count'].groupby(de['mesAno']).std()
deFilterVar = de['Word_Count'].groupby(de['mesAno']).var()

print('Valor máximo do Word_Count: ' + str(deFilterMax))
print('Valor minímo do Word_Count: ' + str(deFilterMin))
print('Média do Word_Count por mês: '+ str(deFilterMean))
print('Mediana do Word_Count por mês: '+ str(deFilterMedian))
print('Desvio Padrão do Word_Count por mês: '+ str(deFilterStd))
print('Variância do Word_Count por mês: '+ str(deFilterVar))

print('########## --------------------------------- ##########')
##4 - dia de cada mes que possui a maior sequencia de mensagens comuns/não spam
dg = pd.DataFrame(data=dados)

dg = dg.loc[:, dg.columns != 'IsNotSpam']
dg = dg.loc[:, dg.columns != 'Word_Count']
dg = dg[dg.IsSpam != 1]

dg = dg[['Common_Word_Count','Date']].groupby(dg['mesAno']).max()

print('Maior Sequência de palavras comuns de textos que não são spams por mês: ')
print(dg)
