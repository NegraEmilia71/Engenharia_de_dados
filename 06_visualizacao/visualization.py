import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def grafico_genero(dados):
    """Gráfico de contagem por gênero"""
    plt.figure(figsize=(10, 5))
    sns.countplot(data=dados, x='GENERO', palette='pastel')
    plt.title('Quantidade de pessoas por gênero')
    plt.xlabel('Gênero')
    plt.ylabel('Contagem')
    plt.grid(True)
    plt.show()

def grafico_salario_idade(dados):
    """Gráfico de salário médio por idade"""
    salario_idade = dados.groupby("IDADE")["SALARIO"].mean()
    
    plt.figure(figsize=(12, 5))
    plt.plot(salario_idade.index, salario_idade.values, marker='o', linestyle='--')
    plt.xlabel('Idade')
    plt.ylabel('Média de salário')
    plt.title('Média de salário por idade')
    plt.grid(True)
    plt.show()

def grafico_scatter_interativo(dados):
    """Gráfico scatter interativo"""
    fig = px.scatter(dados, x='IDADE', y='SALARIO', title="Salário por Idade")
    fig.show()
