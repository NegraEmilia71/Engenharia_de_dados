# Importações
"""

from google.colab import drive
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

"""# Uso da biblioteca Pandas"""

# Criar o link de exportação dos dados com o drive
dados = pd.read_excel('/content/drive/MyDrive/ProgramaMaria/planilha_modulo3.xlsx')

# Ler todos os dados do banco de dados e retorna uma nova DataFrame com tais informações.
dados

#Exibir todas as colunas do banco de dados e retorna uma DataFrame com tais informações
dados.columns

# Exibir as 10° posições (0-9) e retorna uma nova DataFrame com tais informações
dados.head(10)

# Exibir as 5° últimas posições e retorna uma nova DataFrame com tais informações
dados.tail()

# Exibir o total de linhas (4271) e colunas (28) do banco de dados e retorna uma nova DataFrame com tais informações.
dados.shape

# Exibir o total de dados (4271) e retorna uma nova DataFrame com tais informações
len(dados)

#Exibir o enunciado de todas das colunas e retorna uma nova DataFrame com tais informações.
dados.columns

#Exibir as informações sobre os dados e retorna uma nova DataFrame com tais informações.
dados.info()

# Exibir as estatísticas descritivas das colunas numéricas -contagem, média, desvio padrão, mínimo, quartis (25%, 50% e 75%) e máximo
dados.describe()

"""# Repetindo análise do excel"""

# Exibir todas as colunas do banco de dados e e retorna uma DataFrame com tais informações.
dados.columns

# Exibir tudo que existe dentro da coluna Gênero (4273) e o tipo de dado (object) e retorna uma DataFrame com tais informações.
dados['GENERO']

# Seleciona e Filtra dentro da coluna Gênero as informações relacionadas ao Feminino (1056 pessoas).
dados[dados['GENERO'] == 'Feminino']

# Seleciona e Filtra dentro da coluna Gênero as informações relacionadas ao Masculino (1077 pessoas).
dados[dados['GENERO']!='Masculino']

# Busca e conta na coluna Gênero se contém 'não', ignora os valores ausentes e retorna uma nova DataFrame com 'Prefiro não informar' (12 pessoas).
dados[dados['GENERO'].str.contains('não', na=False)]

# Filtra e conta na coluna Idade maior ou igual a 30 (2204 pessoas) e retorna uma nova DataFrame com tais informações.
dados[dados['IDADE']>=30]

# Filtra e conta na coluna Idade quem é 'maior ou igual a 30' e da coluna Gênero as que são 'Feminino' e retorna uma nova DataFrame com tais informações.
dados[(dados['IDADE']>30) & (dados['GENERO']=='Feminino')]

# Agrupa e conta os valores únicos de cada grupo existente na coluna Gênero com o da coluna ID e retorna uma nova DataFrame com tais informações.
dados.groupby('GENERO')['ID'].nunique()

# Agrupar e conta os valores únicos de cada grupo existente na coluna Gênero sem excluir os valores ausentes com os da coluna ID e retorna uma nova DataFrame com tais informações.
dados.groupby('GENERO', dropna=False)['ID'].nunique()

# Agrupar e conta os e retorna uma nova DataFrame com tais informações.
dados[dados['IDADE']>30]['NIVEL'].value_counts()

# Filtra e conta na coluna Idade quem é 'maior ou igual a 30' com da coluna Gênero as que são 'Feminino' e conta dentro do grupo da coluna Nível e retorna uma nova DataFrame com tais informações.
dados[(dados['IDADE']>30) & (dados['GENERO']== "Feminino")]['NIVEL'].value_counts()

# Cria uma tabela dinâmica com o objetivo de contar quantas pessoas existem em cada combinação de GENERO e GESTOR.
pd.pivot_table(dados, values= ['ID'], index=['GENERO'], columns=['GESTOR?'], aggfunc='count')

"""# Estatística Básica"""

# Cria uma lista com a sequência de números inteiros.
lista_idades = [26, 30, 32, 22, 26, 35, 40, 20, 43, 31, 23]

# Com uso do NumPy, executa a soma dos número da lista.
np.sum(lista_idades)

# Conta e retorna o número de elementos dentro da lista.
len(lista_idades)

# Calcula a média (ou média aritmética) da lista
np.sum(lista_idades)/len(lista_idades)

# Calcula a média e exibe a frase "Média aritmética:"
media = np.mean(lista_idades)
print("Média aritmédica:", media)

# Coloca as idades na ordem (do menor para o maior)
lista_idades.sort()
lista_idades

# Calcula a mediana
mediana = np.median(lista_idades)
mediana

"""#### Voltando para a tabela"""

# Calcula a média
dados['IDADE'].mean()

# Calcula a mediana
dados['IDADE'].median()

# Calcula a moda
dados['IDADE'].mode()

# Calcula a desvio padrão
dados['IDADE'].std()

# Exibir a idade mínima
dados['IDADE'].min()

# Exibir a idade máxima
dados['IDADE'].max()

# Calcular a idade média feminina
dados[dados['GENERO'] == 'Feminino']['IDADE'].mean()

# Calcular a idade média masculina
dados[dados['GENERO'] == 'Masculino']['IDADE'].mean()

# Calcular o salário médio feminina
dados[dados['GENERO'] == 'Feminino']['SALARIO'].mean()

# Calcular o salário médio masculino
dados[dados['GENERO'] == 'Masculino']['SALARIO'].mean()

# Criar uma tabela dinâmica (pivot table) com a média cruzando as colunas Sálario, Gênero e GESTOR?.
pd.pivot_table(dados, values= ['SALARIO'], index=['GENERO'], columns=['GESTOR?'], aggfunc='mean')

"""# Valores faltantes"""

# Exibe as informações resumidas sobre da base de dados
dados.info()

"""## trabalhando coluna de gênero"""

# Agrupar e conta os valores únicos de cada grupo existente na coluna Gênero sem excluir os valores ausentes com os da coluna ID e retorna uma nova DataFrame com tais informações.
dados.groupby('GENERO', dropna= False)['ID'].nunique()

# Substituir os valores ausentes (Nan) da coluna Gênero por Prefiro não informar.
dados['GENERO'] = dados['GENERO'].fillna("Prefiro não informar")

# Agrupar e contar os valores únicos de cada grupo existente na coluna Gênero com os da coluna ID e retorna uma nova DataFrame com tais informações.
dados.groupby('GENERO', dropna= False)['ID'].nunique()

"""### Trabalhando coluna idade"""

# Contar quantos valores ausentes (nulos) e não ausentes existem na coluna Idade e retorna uma nova DataFrame com tais informações.
dados['IDADE'].isnull().value_counts()

# Contar quantas vezes cada valor da coluna Faixa Idade aparece somente nas linhas da coluna Idade está vazia (NaN) e retorna uma nova DataFrame com tais informações.
dados[dados['IDADE'].isnull()]['FAIXA IDADE'].value_counts()

# Criar a variável Media_17_21 e calcular a média de todas as pessoas que estão na faixa etária de 17 a 21 anos definido na coluna Faixa Idade.
Media_17_21 = dados[dados['FAIXA IDADE'] == '17-21']['IDADE'].mean()

# Preencher os valores ausentes da coluna Idade, somente para as pessoas na faixa etária de 17 a 21, usando a média previamente calculada na variável Media_17_21.
dados.loc[(dados['FAIXA IDADE'] == '17-21') & (dados['IDADE'].isnull()), 'IDADE'] = Media_17_21

# Contar quantas vezes cada valor da coluna Faixa idade aparece está vazia na coluna Idade e retornar uma nova DataFrame com tais informações.
dados[dados['IDADE'].isnull()]['FAIXA IDADE'].value_counts()

# Calcular a média das idades de todas as pessoas que tem mais de 55 anos e retornar uma nova DataFrame com tais informações.
dados[dados['FAIXA IDADE'] == '55+']['IDADE'].mean()

# Exibir os valores da coluna Idade somente para as pessoas da coluna Faixa Idade é mais de 55 anos e retornar uma nova DataFrame com tais informações.
dados[dados['FAIXA IDADE'] == '55+']['IDADE']

# Exibir os valores da coluna Nível somente para as pessoas da coluna Faixa Idade é mais de 55 anos e retornar uma nova DataFrame com tais informações.
dados[dados['FAIXA IDADE'] == '55+']['NIVEL']

# Criar a variável Media_Geral e calcular a média geral da coluna Idade.
Media_geral = dados['IDADE'].mean()
Media_geral

# Preencher os valores ausentes da coluna Idade, somente para as pessoas na faixa etária +55, usando a média previamente calculada na variável Media_geral.
dados.loc[(dados['FAIXA IDADE'] == '55+') & [(dados['IDADE'].isnull)], 'IDADE'] = Media_geral

# Contar quantas vezes cada valor da coluna Faixa Idade aparece somente nas linhas da coluna Idade está vazia (NaN) e retorna uma nova DataFrame com tais informações.
dados[dados['IDADE'].isnull()]['FAIXA IDADE'].value_counts()

"""### Tratando coluna salário"""

#Filtrar e exibir todas as linhas em que o valor da coluna 'SALARIO' está ausente e retorna uma nova DataFrame.
dados[dados['SALARIO'].isnull()]

#Contar quantas vezes cada valor da coluna Faixa Salaria aparece, somente entre as linhas onde o Salário está ausente.
dados[dados['SALARIO'].isnull()]['FAIXA SALARIAL'].value_counts()

#Cria a variável Mediana_salario para calcular a mediana da coluna Salário, após pede para printar o resultado.
Mediana_salario = dados['SALARIO'].median()
print(Mediana_salario)

#Preenche todos os valores ausentes da coluna Salário com a mediana salarial armazenado na variável Mediana_salario.
dados.loc[dados['SALARIO'].isnull(), 'SALARIO'] = Mediana_salario

"""### Valores discrepantes (outliers)"""

#Cria a variável e a lista com número inteiros.
lista_idades = [26, 30, 32, 22, 26, 35, 400, 20, 43, 31, 23]

#Cria a variável média a partir da variável lista_idade.
media = np.mean(lista_idades)

#Cria a variável desvio padrão a partir
desvio = np.std(lista_idades)

#Calcula o limite inferior
lim_inferior = media - 3*desvio
lim_inferior

#Gerar um boxplot que representa graficamente o conjunto de dados numéricos de Mediana (linha dentro da caixa), Quartis (Q1 e Q3 — bordas da caixa), Intervalo interquartil (IQR): Q3 - Q1, Extremos (mínimo e máximo dentro de 1.5×IQR), Outliers (pontos fora do intervalo esperado)
plt.boxplot(lista_idades)

#Gerar um boxplot (diagrama de caixa) dos valores contidos na coluna Salário
plt.boxplot(dados['SALARIO'])

#Calcular o primeiro quartil da coluna Salário (o valor abaixo do qual 25% dos dados se encontram)
Q1 = dados['SALARIO'].quantile(0.25)
Q1

#Calcular o terceiro quartil da coluna Salário (o valor abaixo do qual 75% dos dados se encontram)
Q3 = dados['SALARIO'].quantile(0.75)
Q3

#Calcular o Intervalo Interquartílico (IQR) que é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1)
IQR = Q3 - Q1
IQR

#Cria a variável lim_superior e calcular o limite superior para a identificação de valores discrepantes (outliers):
lim_superior = Q3 + (1.5*IQR)
lim_superior

#Cria a variável lim_inferior e calcular o limite inferior para a identificação de valores discrepantes (outliers):
lim_inferior = Q1 - (1.5*IQR)
lim_inferior

#Conta e exibe a quantidade de grupos existentes na coluna Faixa Salarial
dados['FAIXA SALARIAL'].value_counts()

#Cria a variável media_salario, calcula a média da coluna Salário e exibe o resultado
media_salario = dados['SALARIO'].mean()
media_salario

#Cria a variável desvio_salario, calcula a desvio padrão da coluna Salário e exibe o resultado
desvio_salario = dados['SALARIO'].std()
desvio_salario

#Cria a variável limite_superior, calcula para identificar outliers usando a média e o desvio padrão dos salários e exibe o resultado
limite_superior = media_salario + (3*desvio_salario)
limite_superior

#Filtra os outliers superiores com base no limite superior e contar a quantidade de ocorrências de cada faixa salarial destes outliers.
dados[(dados['SALARIO']> limite_superior)]['FAIXA SALARIAL'].value_counts()

#Cria a variável media_30_40 e calcula a média dos salários para a faixa salarial, considerando os salários menores que outliers superiores
media_30_40 = dados[(dados['FAIXA SALARIAL']=='de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']< limite_superior)]['SALARIO'].mean()

#Localizar e alterar os valores da coluna salário para faixa salarial preenchendo com a média da variável media_30_40
dados.loc[(dados['FAIXA SALARIAL']=='de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']> limite_superior), 'SALARIO'] = media_30_40

#Contar e demonstrar as ocorrências de cada faixa salarial em que o valor do salário é maior que o limite superior
dados[(dados['SALARIO']> limite_superior)]['FAIXA SALARIAL'].value_counts()

##Cria a variável media_40 e calcula a média dos salários para a faixa salarial, considerando os salários maiores que outliers superiores
media_40 = dados[(dados['FAIXA SALARIAL']=='Acima de R$ 40.001/mês') & (dados['SALARIO']< limite_superior)]['SALARIO'].mean()

#Localizar e alterar os valores da coluna salário para faixa salarial preenchendo com a média da variável media_40
dados.loc[(dados['FAIXA SALARIAL']=='Acima de R$ 40.001/mês') & (dados['SALARIO']> limite_superior), 'SALARIO'] = media_40

#Contar e demonstrar as ocorrências de cada faixa salarial em que o valor do salário é maior que o limite superior
dados[(dados['SALARIO']> limite_superior)]['FAIXA SALARIAL'].value_counts()

#Gerar um boxplot da coluna Salário
plt.boxplot(dados['SALARIO'])

"""# Distribuição amostral e intervalo de confiança"""

#Cria a variável Salários e exibir os dados da coluna Salário.
salarios = dados['SALARIO']

#Exibe os dados da variável Salários
salarios

#Cria a variável media_amostral, calcula a média da variável Salários e exibe o resultado
media_amostral = np.mean(salarios)
media_amostral

#Cria a variável desvio_amostral, calcula o desvio padrão da variável Salários e exibe o resultado
desvio_amostral = np.std(salarios)
desvio_amostral

#Cria a variável nivel_amostral e calcula o nível de confiança em 95%
nivel_confianca = [0.95]

#Cria a variável tamanho_amostral, calcula o tamanho da amostra e exibe o resultado
tamanho_amostral = len(salarios)
tamanho_amostral

#Cria a variável erro_padrão, calcula o erro padrão e exibe o resultado
erro_padrao = stats.sem(salarios)
erro_padrao

#Cria a variável intervalo_confianca, calcula o intervalo de confiança e exibe o resultado
intervalo_confianca = stats.t.interval(nivel_confianca, tamanho_amostral-1, loc=media_amostral, scale=erro_padrao)
intervalo_confianca

"""# Featuring Engeneering (Engenharia de Recursos)"""

#Cria a função preencher_nivel para retornar o nível de uma pessoa, mas com uma exceção se a pessoa for gestora (gestor == 1), retornará "Pessoa Gestora".
def preencher_nivel(gestor, nivel):
  if gestor == 1:
    return "Pessoa Gestora"
  else:
    return nivel

#cria uma nova coluna NOVO_NIVEL, Pegar os valores das colunas Gestor e Nive, passa esses dois valores como entrada para a função preencher_nivel().
#O valor retornado pela função preencher_nivel será armazenado na nova coluna.
dados['NOVO_NIVEL'] = dados.apply(lambda x: preencher_nivel(x['GESTOR?'], x['NIVEL']), axis=1)

#conta e exibe as categprias da coluna Novo Nível
dados['NOVO_NIVEL'].value_counts()

#coluna categórica NIVEL do seu DataFrame dados e a transforma em múltiplas colunas binárias ([False]0s e [True]1). Converte categorias em um formato numérico, apaixoneii!
dados = pd.get_dummies(dados, columns=['NIVEL'])

#Exibe os nomes das colunas do banco de dados
dados.columns

#Cria a função determinar_geracao a partir da idade considerando uma faixa. Se a for maior que 13 e menor igual a 29 retornará "Geração Z";
#Se a for maior que 29 e menor igual a 38 retornará "Geração Millenial"; Se a for maior que 39 e menor igual a 58 retornará "Geração X;
#qualquer idade acima de 59, retornará "Outra geração".
def determinar_geracao(idade):
  if 39<idade<=58:
    return "Geração X"
  elif 29<idade<=38:
    return "Geração Millenial"
  elif 13<idade<=29:
    return "Geração Z"
  else:
    "Outra geração"

#Cria uma nova coluna Geracao que será preenchida pela função determinar_funcao a partir do valor identificado na coluna Idade.
dados['GERACAO']= dados['IDADE'].apply(determinar_geracao)

#Contar e exibir as linhas contidas na coluna Geracao.
dados['GERACAO'].value_counts()

#Ler e carregar a base de dados do excel chamada Planilha Aula Parte 2.
dados2 = pd.read_excel('/content/drive/MyDrive/ProgramaMaria/Planilha_Aula_parte2.xlsx')

#Exibir as primeiras linhas da base de dados.
dados2.head()

#Juntar as duas bases de dados a partir da coluna ID. Os dados da esquerda" com os dados2 da direita.
#O resultado da junção é atribuído de volta à variável dados, o que significa que a base de dados original
#será atualizado com as novas colunas e informações do dados2
dados = dados.merge(dados2, on='ID', how='left')

#Exibir as colunas da base de dados, agora já unificada.
dados.columns

#Exibir e contar as linhas da coluna Você pretende mudar de emprego nos próximos 6 meses? e retorna com tais informações.
dados['Você pretende mudar de emprego nos próximos 6 meses?'].value_counts()

#Cria a coluna Em_busca, acessar o texto na coluna Você pretende mudar de emprego nos próximos 6 meses?, verificar se contém a palavra em busca.
#Se a frase for encontrada, a nova coluna EM_BUSCA receberá o valor True para aquela linha.
#Se a frase não for encontrada, a nova coluna EM_BUSCA receberá o valor False para aquela linha.
dados['EM_BUSCA'] = dados['Você pretende mudar de emprego nos próximos 6 meses?'].str.contains('em busca', case=False)

#Exibir e contar as linhas da coluna Em_busca já convertida em True e False .
dados['EM_BUSCA'].value_counts()

#Cria a coluna Aberto_oportunidades, acessar o texto na coluna Você pretende mudar de emprego nos próximos 6 meses?, verificar se contém a palavra aberto.
#Se a frase for encontrada, a nova coluna Aberto_oportunidades receberá o valor True para aquela linha.
#Se a frase não for encontrada, a nova coluna EM_BUSCA receberá o valor False para aquela linha.
dados['ABERTO_OPORTUNIDADES'] = dados['Você pretende mudar de emprego nos próximos 6 meses?'].str.contains('aberto', case=False)

#Exibir e contar as linhas da coluna Aberto_oportunidade já convertida em True e False .
dados['ABERTO_OPORTUNIDADES'].value_counts()

#Exibir e contar as linhas da coluna Cor/Raca/Etnia
dados['COR/RACA/ETNIA'].value_counts()

#Cria a coluna Não_branca, acessar o texto na coluna Cora/Raca/Etnia, verificar se contém as palavras Preto/Pardo.
#Se as palavras Preta/Parda for encontrada, a nova coluna Nao_branca receberá o valor True para aquela linha.
#Se as palavras Preta/Parda não for encontrada, a nova coluna Nao_Branca receberá o valor False para aquela linha.
dados['NÃO_BRANCA'] = dados['COR/RACA/ETNIA'].str.contains('Parda|Preta', case=False)

#Exibir e contar as linhas da coluna Não_branca
dados['NÃO_BRANCA'].value_counts()

#Cria a coluna Branca, acessar o texto na coluna Cora/Raca/Etnia, verificar se contém a palavra Branca.
#Se a palavra Branca for encontrada, a nova coluna branca receberá o valor True para aquela linha.
#Se a palavra Branca não for encontrada, a nova coluna Branca receberá o valor False para aquela linha.
dados['BRANCA'] = dados['COR/RACA/ETNIA'].str.contains('Branca', case=False)

#Exibir e contar as linhas da coluna Branca.
dados['BRANCA'].value_counts()

#Cria a coluna Outra, acessar o texto na coluna Cora/Raca/Etnia, verificar se contém as palavras Amarela/ Indigena/ Prefiro não informar/ Outra.
#Se as palavras Amarela/ Indigena/ Prefiro não informar/ Outra for encontrada, a nova coluna Outra receberá o valor True para aquela linha.
#Se as palavras Amarela/ Indigena/ Prefiro não informar/ Outra não for encontrada, a nova coluna Outra receberá o valor False para aquela linha.
dados['OUTRA'] = dados['COR/RACA/ETNIA'].str.contains('Amarela | Prefiro não informar | Outra | Indígena', case=False)

#Exibir e contar as linhas da coluna Outra.
dados['OUTRA'].value_counts()

"""# Correlação"""

#Cria a variável correlacao_continua, calcula a correlação entre as colunas Idade e Salario e exibe o resultado. A relação é positiva e fraca entre as duas colunas.
correlacao_continua = dados['IDADE'].corr(dados['SALARIO'])
correlacao_continua

#Cria a função Cramer_coeficiente para medir a força da associação entre duas variáveis categóricas.Cria uma tabela de contingência (ou tabela cruzada) a partir das duas colunas categóricas fornecidas
#Converte essa tabela de contingência para um array. Realiza o Teste Qui-Quadrado de Independência na tabela de contingência. Este teste verifica se há uma associação estatisticamente significativa entre as duas variáveis categóricas.
#Calcula a soma total de todas as observações na tabela de contingência. etorna uma tupla com as dimensões da tabela (número de linhas, número de colunas).
#Pega o menor valor entre o número de linhas e o número de colunas. A função Cramer retorna o valor calculado do V de .
def cramer_coeficiente(coluna1, coluna2):
  tabela_cruzada = np.array(pd.crosstab (coluna1, coluna2))
  chi2 = chi2_contingency(tabela_cruzada)[0]
  soma = np.sum(tabela_cruzada)
  mini = min(tabela_cruzada.shape)-1
  cramer = np.sqrt(chi2/(soma*mini))
  return cramer

#calcular o coeficiente V de Cramer entre as colunas COR/RACA/ETNIA e Nivel de ensino
cramer_coeficiente(dados['COR/RACA/ETNIA'],dados['NIVEL DE ENSINO'])

#cria a variável tabela_cruzada e conta a frequência de ocorrência para cada combinação única entre os valores de ambas as colunas.
tabela_cruzada = pd.crosstab (dados['COR/RACA/ETNIA'], dados['NIVEL DE ENSINO'])
tabela_cruzada

#calcular o Coeficiente V de Cramér entre duas variáveis categóricas
cramer_coeficiente(dados['COR/RACA/ETNIA'],dados['GENERO'])

#Salvar o arquivo em CSV no Drive
dados.to_csv('/content/drive/MyDrive/ProgramaMaria/analise_dados.csv', index=False)

"""# Conectando SQL com Pandas"""

import sqlite3

conexao = sqlite3.connect('/content/drive/MyDrive/ProgramaMaria/status_brasil')

query = 'SELECT * FROM Municipios_Brasileiros WHERE Cidade="Itaquaquecetuba"'

query

pd.read_sql(query, con=conexao)

"""## Criando a lista de item com .join"""

#Cria a lista com 1 item
a = 'batata'

print('Eu gosto de {}'.format(a))

b = ['batata', 'tomate', 'alface']

print('Eu gosto de {}, {} e {}'.format(b[0], b[1], b[2]))

c = ['batata', 'tomate', 'alface']

print('Eu gosto de {}'.format(','.join(c)))

"""## Calculo da Renda Média por Estado"""

#exibir o contéudo da lista_estados
lista_estados

#cria a variável lista_estados
lista_estados = (dados['UF ONDE MORA'].unique())

#Cria a variável dados a partir do link indicado oriundo de uma tabela .CSV
dados = pd.read_csv('/content/drive/MyDrive/ProgramaMaria/analise_dados.csv')

#Exibir o nome das colunas
dados.columns

query1 = '''SELECT Municipios_Brasileiros.Estado, AVG(Municipios_Status.Renda) FROM Municipios_Brasileiros
        INNER JOIN Municipios_Status ON Municipios_Brasileiros.MunicipioID = Municipios_Status.MunicipioID
        WHERE Municipios_Brasileiros.Estado IN ({})
        GROUP BY Municipios_Brasileiros.Estado;'''.format(','.join(['?' for _ in lista_estados]))

#Exibir o que contém a query
print(query1)

# ler, criar a variável estados_renda e exibir a tabela com média de renda por Estado
estados_renda = pd.read_sql(query1, con=conexao, params= lista_estados)

dados.rename(columns= {'UF ONDE MORA': 'Estado'}, inplace=True)

dados.columns

dados = dados.merge(estados_renda, on="Estado", how='left')

correlacao_renda_salario = dados['SALARIO'].corr(dados['AVG (Municipios_Status.Renda)'])
correlacao_renda_salario

"""## Calculo da Educação Média por Estado"""

query2 = '''SELECT Municipios_Brasileiros.Estado, AVG(Municipios_Status.Educação) FROM Municipios_Brasileiros
        INNER JOIN Municipios_Status ON Municipios_Brasileiros.MunicipioID = Municipios_Status.MunicipioID
        WHERE Municipios_Brasileiros.Estado IN ({})
        GROUP BY Municipios_Brasileiros.Estado;'''.format(','.join(['?' for _ in lista_estados]))

estados_educacao = pd.read_sql(query2, con=conexao, params= lista_estados)

dados = dados.merge(estados_educacao, on="Estado", how='left')

dados.columns

correlacao_educacao_salario = dados['SALARIO'].corr(dados['AVG(Municipios_Status.Educação)_x'])
correlacao_educacao_salario

"""# Visualização de Dados"""

import pandas as pd

dados = pd.read_csv('/content/drive/MyDrive/ProgramaMaria/analise_dados.csv')

dados.head()

genero_counts = dados['GENERO'].value_counts()

import matplotlib.pyplot as plt

plt.figure()
plt.bar(height = genero_counts.values, x= genero_counts.index)
plt.title('Quantidade de pessoas por gênero na área de dados')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()

import seaborn as sns

plt.figure()
sns.countplot(data=dados, x='GENERO', palette='pastel')
plt.title('Quantidade de pessoas por gênero na área de dados')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.grid(True)
plt.show()

salario_idade = dados.groupby("IDADE")["SALARIO"].mean()
salario_idade

plt.figure()
plt.plot(salario_idade.index, salario_idade.values, marker='o', linestyle= '--')
plt.xlabel('Idade')
plt.ylabel('Média de salário')
plt.title('Média de salário por idade')
plt.grid(True)
plt.show()

import plotly.express as px

fig = px.line(salario_idade.reset_index(), x='IDADE', y= 'SALARIO', title = "Média de salário por idade", markers=True)
fig.show()

plt.figure(figsize=(20,5))
plt.scatter(dados['IDADE'], dados['SALARIO'], alpha=0.5)
plt.xlabel('Idade')
plt.ylabel('Média de salário')
plt.title('Média de salário por idade')
plt.grid(True)
plt.show()

fig = px.scatter(dados, x='IDADE', y= 'SALARIO', title = "Média de salário por idade")
fig.show()

