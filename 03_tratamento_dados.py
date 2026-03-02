"""
Etapa 3: TRATAMENTO DE DADOS
Responsável por limpeza e tratamento de dados faltantes e outliers
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from config import LIMITE_OUTLIERS

def preencher_genero(dados):
    """
    Preenche valores ausentes da coluna Gênero
    
    Args:
        dados (pd.DataFrame): DataFrame para tratamento
        
    Returns:
        pd.DataFrame: DataFrame tratado
    """
    print("\n🔧 Preenchendo valores faltantes de Gênero...")
    faltantes_antes = dados['GENERO'].isnull().sum()
    dados['GENERO'] = dados['GENERO'].fillna("Prefiro não informar")
    print(f"✅ {faltantes_antes} valores preenchidos")
    return dados

def preencher_idade(dados):
    """
    Preenche valores ausentes da coluna Idade por faixa etária
    
    Args:
        dados (pd.DataFrame): DataFrame para tratamento
        
    Returns:
        pd.DataFrame: DataFrame tratado
    """
    print("\n🔧 Preenchendo valores faltantes de Idade...")
    
    media_17_21 = dados[dados['FAIXA IDADE'] == '17-21']['IDADE'].mean()
    quantidade_17_21 = dados.loc[(dados['FAIXA IDADE'] == '17-21') & (dados['IDADE'].isnull())].shape[0]
    dados.loc[(dados['FAIXA IDADE'] == '17-21') & (dados['IDADE'].isnull()), 'IDADE'] = media_17_21
    print(f"  ✅ Faixa 17-21: {quantidade_17_21} valores preenchidos")
    
    media_geral = dados['IDADE'].mean()
    quantidade_55 = dados.loc[(dados['FAIXA IDADE'] == '55+') & (dados['IDADE'].isnull())].shape[0]
    dados.loc[(dados['FAIXA IDADE'] == '55+') & (dados['IDADE'].isnull()), 'IDADE'] = media_geral
    print(f"  ✅ Faixa 55+: {quantidade_55} valores preenchidos")
    
    return dados

def preencher_salario(dados):
    """
    Preenche valores ausentes da coluna Salário com mediana
    
    Args:
        dados (pd.DataFrame): DataFrame para tratamento
        
    Returns:
        pd.DataFrame: DataFrame tratado
    """
    print("\n🔧 Preenchendo valores faltantes de Salário...")
    faltantes = dados['SALARIO'].isnull().sum()
    mediana_salario = dados['SALARIO'].median()
    dados.loc[dados['SALARIO'].isnull(), 'SALARIO'] = mediana_salario
    print(f"✅ {faltantes} valores preenchidos com mediana")
    return dados

def remover_outliers_salario(dados):
    """
    Remove outliers da coluna Salário
    
    Args:
        dados (pd.DataFrame): DataFrame para tratamento
        
    Returns:
        pd.DataFrame: DataFrame com outliers tratados
    """
    print("\n🔧 Tratando outliers de Salário...")
    
    media_salario = dados['SALARIO'].mean()
    desvio_salario = dados['SALARIO'].std()
    limite_superior = media_salario + (LIMITE_OUTLIERS * desvio_salario)
    
    print(f"  📊 Limite superior: R$ {limite_superior:,.2f}")
    outliers = dados[dados['SALARIO'] > limite_superior]
    print(f"  ⚠️  {len(outliers)} outliers identificados")
    
    # Visualizar boxplot
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.boxplot(dados['SALARIO'])
    plt.title('Antes do tratamento')
    plt.ylabel('Salário (R$)')
    
    # Tratar outliers
    if len(outliers) > 0:
        media_30_40 = dados[(dados['FAIXA SALARIAL']=='de R$ 30.001/mês a R$ 40.000/mês') & 
                            (dados['SALARIO'] < limite_superior)]['SALARIO'].mean()
        dados.loc[(dados['FAIXA SALARIAL']=='de R$ 30.001/mês a R$ 40.000/mês') & 
                  (dados['SALARIO'] > limite_superior), 'SALARIO'] = media_30_40
        
        media_40_plus = dados[(dados['FAIXA SALARIAL']=='Acima de R$ 40.001/mês') & 
                              (dados['SALARIO'] < limite_superior)]['SALARIO'].mean()
        dados.loc[(dados['FAIXA SALARIAL']=='Acima de R$ 40.001/mês') & 
                  (dados['SALARIO'] > limite_superior), 'SALARIO'] = media_40_plus
        print(f"  ✅ Outliers tratados com sucesso")
    
    plt.subplot(1, 2, 2)
    plt.boxplot(dados['SALARIO'])
    plt.title('Depois do tratamento')
    plt.ylabel('Salário (R$)')
    plt.tight_layout()
    plt.show()
    
    return dados

def resumo_dados_tratados(dados):
    """
    Exibe resumo dos dados após tratamento
    
    Args:
        dados (pd.DataFrame): DataFrame tratado
    """
    print("\n" + "="*60)
    print("✅ RESUMO - DADOS TRATADOS")
    print("="*60)
    print(f"\n📊 Total de registros: {len(dados)}")
    print(f"📋 Total de colunas: {len(dados.columns)}")
    print(f"❓ Valores faltantes: {dados.isnull().sum().sum()}")
    print("\n✨ Dados prontos para feature engineering!")
