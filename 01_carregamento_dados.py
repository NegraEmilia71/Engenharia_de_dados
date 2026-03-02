"""
Etapa 1: CARREGAMENTO DE DADOS
Responsável por importar dados do Excel e unificar bases
"""

import pandas as pd
from config import ARQUIVO_PRINCIPAL, ARQUIVO_PARTE2

def carregar_dados_principais():
    """
    Carrega a planilha principal
    
    Returns:
        pd.DataFrame: Dados do arquivo principal
    """
    print("\n📥 Carregando dados principais...")
    dados = pd.read_excel(ARQUIVO_PRINCIPAL)
    print(f"✅ {len(dados)} registros carregados com sucesso!")
    return dados

def carregar_dados_secundarios():
    """
    Carrega a segunda planilha
    
    Returns:
        pd.DataFrame: Dados do arquivo secundário
    """
    print("\n📥 Carregando dados secundários...")
    dados2 = pd.read_excel(ARQUIVO_PARTE2)
    print(f"✅ {len(dados2)} registros carregados com sucesso!")
    return dados2

def unificar_dados(dados, dados2):
    """
    Une as duas bases de dados via ID
    
    Args:
        dados (pd.DataFrame): Base principal
        dados2 (pd.DataFrame): Base secundária
        
    Returns:
        pd.DataFrame: Dados unificados
    """
    print("\n🔗 Unificando bases de dados...")
    dados = dados.merge(dados2, on='ID', how='left')
    print(f"✅ Dados unificados! Total de colunas: {len(dados.columns)}")
    return dados

def info_dados(dados):
    """
    Exibe informações básicas dos dados
    
    Args:
        dados (pd.DataFrame): DataFrame para análise
    """
    print("\n" + "="*60)
    print("📊 INFORMAÇÕES - DADOS CARREGADOS")
    print("="*60)
    print(f"\n📝 Dimensões: {dados.shape[0]} linhas × {dados.shape[1]} colunas")
    print(f"\n📋 Colunas:\n{list(dados.columns)}")
    print(f"\n🔍 Tipos de dados:\n{dados.dtypes}")
    print(f"\n⚠️  Valores ausentes:\n{dados.isnull().sum()}")
