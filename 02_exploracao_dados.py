"""
Etapa 2: EXPLORAÇÃO DE DADOS
Responsável por análise exploratória e estatísticas descritivas
"""

import pandas as pd
import numpy as np

def explorar_dados(dados):
    """
    Análise exploratória completa
    
    Args:
        dados (pd.DataFrame): DataFrame para análise
    """
    print("\n" + "="*60)
    print("🔍 ANÁLISE EXPLORATÓRIA")
    print("="*60)
    
    print(f"\n📊 Dimensões: {dados.shape}")
    print(f"\n📋 Primeiras linhas:\n{dados.head()}")
    print(f"\n📈 Estatísticas descritivas:\n{dados.describe()}")

def analisar_coluna_genero(dados):
    """
    Análise detalhada da coluna Gênero
    
    Args:
        dados (pd.DataFrame): DataFrame para análise
    """
    print("\n" + "="*60)
    print("👥 ANÁLISE - GÊNERO")
    print("="*60)
    
    contagem = dados['GENERO'].value_counts(dropna=False)
    print(f"\n{contagem}")
    print(f"\nPercentual:\n{(contagem/len(dados)*100).round(2)}")

def analisar_coluna_idade(dados):
    """
    Análise detalhada da coluna Idade
    
    Args:
        dados (pd.DataFrame): DataFrame para análise
    """
    print("\n" + "="*60)
    print("📅 ANÁLISE - IDADE")
    print("="*60)
    
    print(f"\n📊 Média: {dados['IDADE'].mean():.2f} anos")
    print(f"📊 Mediana: {dados['IDADE'].median():.2f} anos")
    print(f"📊 Moda: {dados['IDADE'].mode().values[0]:.0f} anos")
    print(f"📊 Desvio padrão: {dados['IDADE'].std():.2f}")
    print(f"📊 Mínimo: {dados['IDADE'].min():.0f} anos")
    print(f"📊 Máximo: {dados['IDADE'].max():.0f} anos")

def analisar_coluna_salario(dados):
    """
    Análise detalhada da coluna Salário
    
    Args:
        dados (pd.DataFrame): DataFrame para análise
    """
    print("\n" + "="*60)
    print("💰 ANÁLISE - SALÁRIO")
    print("="*60)
    
    print(f"\n💵 Média: R$ {dados['SALARIO'].mean():,.2f}")
    print(f"💵 Mediana: R$ {dados['SALARIO'].median():,.2f}")
    print(f"💵 Desvio padrão: R$ {dados['SALARIO'].std():,.2f}")
    print(f"💵 Mínimo: R$ {dados['SALARIO'].min():,.2f}")
    print(f"💵 Máximo: R$ {dados['SALARIO'].max():,.2f}")
    
    print(f"\n📊 Distribuição por faixa salarial:")
    print(dados['FAIXA SALARIAL'].value_counts())

def analisar_dados_categoricos(dados):
    """
    Análise de variáveis categóricas
    
    Args:
        dados (pd.DataFrame): DataFrame para análise
    """
    print("\n" + "="*60)
    print("🏷️  ANÁLISE - VARIÁVEIS CATEGÓRICAS")
    print("="*60)
    
    categoricas = dados.select_dtypes(include='object').columns
    for col in categoricas[:5]:  # Primeiras 5
        print(f"\n📋 {col}:")
        print(dados[col].value_counts().head(3))
