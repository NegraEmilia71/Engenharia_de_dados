from google.colab import drive
drive.mount('/content/drive')

# Importar todas as funções
from config import *
from importlib import reload

# Executar pipeline
exec(open('config.py').read())
exec(open('01_carregamento_dados.py').read())
exec(open('02_exploracao_dados.py').read())
exec(open('03_tratamento_dados.py').read())

# Pipeline
dados = carregar_dados_principais()
dados2 = carregar_dados_secundarios()
dados = unificar_dados(dados, dados2)

explorar_dados(dados)
analisar_coluna_genero(dados)
analisar_coluna_idade(dados)
analisar_coluna_salario(dados)

dados = preencher_genero(dados)
dados = preencher_idade(dados)
dados = preencher_salario(dados)
dados = remover_outliers_salario(dados)
resumo_dados_tratados(dados)

print("\n✅ Pipeline concluído com sucesso!")
