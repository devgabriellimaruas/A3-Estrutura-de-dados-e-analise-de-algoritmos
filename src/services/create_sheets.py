import pandas as pd

def criar_planilha_entregas(dados_entregas, nome_arquivo="entregas_caminhoes.xlsx"):
    df = pd.DataFrame(dados_entregas)
    df.to_excel(nome_arquivo, index=False)
    print(f"Dados das entregas exportados para o arquivo: {nome_arquivo}")
