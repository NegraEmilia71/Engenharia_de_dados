import pandas as pd

def salvar_csv(dados, caminho):
    """Salva dados em CSV"""
    dados.to_csv(caminho, index=False)
    print(f"Arquivo salvo em: {caminho}")

def carregar_csv(caminho):
    """Carrega dados de CSV"""
    return pd.read_csv(caminho)
