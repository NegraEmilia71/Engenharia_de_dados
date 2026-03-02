import pandas as pd

def criar_novo_nivel(dados):
    """Cria coluna NOVO_NIVEL"""
    def preencher_nivel(gestor, nivel):
        return "Pessoa Gestora" if gestor == 1 else nivel
    
    dados['NOVO_NIVEL'] = dados.apply(lambda x: preencher_nivel(x['GESTOR?'], x['NIVEL']), axis=1)
    return dados

def codificar_nivel(dados):
    """Transforma NIVEL em variáveis binárias"""
    dados = pd.get_dummies(dados, columns=['NIVEL'])
    return dados

def criar_geracao(dados):
    """Cria coluna de geração"""
    def determinar_geracao(idade):
        if 39 < idade <= 58:
            return "Geração X"
        elif 29 < idade <= 38:
            return "Geração Millenial"
        elif 13 < idade <= 29:
            return "Geração Z"
        else:
            return "Outra geração"
    
    dados['GERACAO'] = dados['IDADE'].apply(determinar_geracao)
    return dados

def criar_features_emprego(dados):
    """Cria features sobre procura de emprego"""
    dados['EM_BUSCA'] = dados['Você pretende mudar de emprego nos próximos 6 meses?'].str.contains('em busca', case=False)
    dados['ABERTO_OPORTUNIDADES'] = dados['Você pretende mudar de emprego nos próximos 6 meses?'].str.contains('aberto', case=False)
    return dados

def criar_features_etnia(dados):
    """Cria features sobre cor/raça/etnia"""
    dados['NÃO_BRANCA'] = dados['COR/RACA/ETNIA'].str.contains('Parda|Preta', case=False)
    dados['BRANCA'] = dados['COR/RACA/ETNIA'].str.contains('Branca', case=False)
    dados['OUTRA'] = dados['COR/RACA/ETNIA'].str.contains('Amarela|Prefiro não informar|Outra|Indígena', case=False)
    return dados
