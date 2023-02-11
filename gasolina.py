import pandas as pd
import seaborn as sns

df = pd.read_csv('gasolina.csv')
df
sns.axes_style('whitegrid')
grafico = sns.lineplot(data=df,x='dia',y='venda')
grafico.set(title='Grafico mostrando o valor da gasolina por dia',xlabel='Dia',ylabel='Preço')
grafico.figure.savefig('grafico.png')