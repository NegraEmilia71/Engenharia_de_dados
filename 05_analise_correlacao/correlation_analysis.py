import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

def correlacao_continua(col1, col2):
    """Calcula correlação entre variáveis contínuas"""
    return col1.corr(col2)

def cramer_coeficiente(coluna1, coluna2):
    """Calcula V de Cramér entre variáveis categóricas"""
    tabela_cruzada = np.array(pd.crosstab(coluna1, coluna2))
    chi2 = chi2_contingency(tabela_cruzada)[0]
    soma = np.sum(tabela_cruzada)
    mini = min(tabela_cruzada.shape) - 1
    cramer = np.sqrt(chi2 / (soma * mini))
    return cramer

def analisar_correlacoes(dados):
    """Analisa correlações principais"""
    corr_idade_salario = correlacao_continua(dados['IDADE'], dados['SALARIO'])
    print(f"Correlação Idade-Salário: {corr_idade_salario}")
    
    corr_etnia_ensino = cramer_coeficiente(dados['COR/RACA/ETNIA'], dados['NIVEL DE ENSINO'])
    print(f"Correlação Etnia-Nível de Ensino: {corr_etnia_ensino}")
