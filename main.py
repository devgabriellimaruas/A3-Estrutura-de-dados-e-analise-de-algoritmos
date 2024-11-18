import math
from src.services.data_manipulation import gerar_cenario, alocar_entregas
from src.services.create_sheets import criar_planilha_entregas


if __name__ == "__main__":
    grafo, entregas, caminhoes = gerar_cenario(caminhoes_por_centro=5)
    alocar_entregas(entregas, caminhoes, grafo)

    # Listar para armazenar os dados das entregas
    dados_entregas = []

    for caminhao in caminhoes:
        if caminhao.entregas:
            entregas_ordenadas = sorted(
                caminhao.entregas,
                key=lambda entrega: grafo.obter_distancia(caminhao.centro_distribuicao, entrega.destino) / 60
            )

            for entrega in entregas_ordenadas:
                distancia = grafo.obter_distancia(caminhao.centro_distribuicao, entrega.destino)
                tempo_viagem = distancia / 60
                dias_necessarios = math.ceil(tempo_viagem / caminhao.horas_diarias)

                # Adicionar as informações ao DataFrame
                dados_entregas.append({
                    "Centro de Distribuição": caminhao.centro_distribuicao,
                    "Destino": entrega.destino,
                    "Peso (kg)": entrega.peso,
                    "Distância (km)": f"{distancia:.2f}",
                    "Prazo (dias)": entrega.prazo,
                    "Dias Necessários": dias_necessarios
                })

    # Criar o arquivo Excel
    criar_planilha_entregas(dados_entregas)
