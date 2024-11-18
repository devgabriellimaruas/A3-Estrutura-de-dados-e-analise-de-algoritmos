import math
from src.services.data_manipulation import gerar_cenario, alocar_entregas


if __name__ == "__main__":
    grafo, entregas, caminhoes = gerar_cenario(caminhoes_por_centro=5)
    alocar_entregas(entregas, caminhoes, grafo)

    for caminhao in caminhoes:
        if caminhao.entregas:
            print(f"Caminhão no centro {caminhao.centro_distribuicao} entregará:")

            entregas_ordenadas = sorted(
                caminhao.entregas,
                key=lambda entrega: grafo.obter_distancia(caminhao.centro_distribuicao, entrega.destino) / 60
            )

            for entrega in entregas_ordenadas:
                distancia = grafo.obter_distancia(caminhao.centro_distribuicao, entrega.destino)
                tempo_viagem = distancia / 60
                dias_necessarios = math.ceil(tempo_viagem / caminhao.horas_diarias)
                print(
                    f"  - Destino: {entrega.destino}, Peso: {entrega.peso}kg, "
                    f"Distância: {distancia:.2f}km, Prazo: {entrega.prazo} dias, "
                    f"Dias necessários: {dias_necessarios}"
                )
            print()
