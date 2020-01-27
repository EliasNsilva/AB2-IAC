import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib.style as mplstyle

#1º Gráfico com todos dados.

mplstyle.use(['ggplot'])

dados = pd.read_csv('a2_MANCHAS.csv')
plt.plot(dados.Ano, dados.manchas)
plt.grid(True)
plt.xlabel("Anos")
plt.ylabel("Manchas")
plt.title("Número de manchas Solares")
plt.show()

#2º Dez primeiras linhas de dados.

dados_10 = dados[0:10]
plt.plot(dados_10.Ano, dados_10.manchas, 'g')
plt.grid(True)
plt.xlabel("Anos")
plt.ylabel("Manchas")
plt.title("Número de manchas Solares")
plt.xticks(dados_10.Ano, rotation = 'vertical')
plt.show()

#3º Dez últimas linhas de dados. 

dados_10_ult = dados[167:]
plt.plot(dados_10_ult.Ano, dados_10_ult.manchas, 'b--')
plt.grid(True)
plt.xlabel("Anos")
plt.ylabel("Manchas")
plt.title("Número de manchas Solares")
plt.xticks(dados_10_ult.Ano, rotation = 'vertical')
plt.show()

#4º boxplot.

plt.boxplot(dados.manchas)
plt.grid(True)
plt.ylabel("Manchas")
plt.title("Número de manchas Solares")
plt.show()

#5º Trinta primeiras linhas de dados.

dados_30 = dados[0:30]
plt.plot(dados_30.Ano, dados_30.manchas, 'r')
plt.grid(True)
plt.xlabel("Anos")
plt.ylabel("Manchas")
plt.title("Número de manchas Solares")
plt.xticks(dados_30.Ano, rotation = 'vertical')
plt.show()
