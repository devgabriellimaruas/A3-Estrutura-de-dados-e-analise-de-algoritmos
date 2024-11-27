import math
import time
import tracemalloc
from src.services.data_manipulation import gerar_cenario_mais_entregas, gerar_cenario_menos_entregas, alocar_entregas
from src.services.create_sheets import criar_planilha_entregas


if __name__ == "__main__":
    # Inicia o o tempo de execução
    start_time = time.time()
    # Inicia o rastreamento de alocação de memória
    tracemalloc.start()
    grafo, entregas, caminhoes = gerar_cenario_mais_entregas(caminhoes_por_centro=5)
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
    criar_planilha_entregas(dados_entregas, "mais_entregas_caminhoes.xlsx")
    
    # Tempo de execução
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo de execução do cenário 1: {elapsed_time} segundos")
    
    # Memória alocada
    memoria_usada = tracemalloc.get_traced_memory()[1] / 1024  # Usado em KB
    print(f"Memória após a execução do cenário 1: {memoria_usada} KB")

    # Finaliza o rastreamento
    tracemalloc.stop()
    
    
    
    #Criando cenário 2
    # Inicia o o tempo de execução
    start_time = time.time()
    # Inicia o rastreamento de alocação de memória
    tracemalloc.start()
    grafo, entregas, caminhoes = gerar_cenario_menos_entregas(caminhoes_por_centro=5)
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
    criar_planilha_entregas(dados_entregas, "menos_entregas_caminhoes.xlsx")

    # Tempo de execução
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo de execução do cenário 1: {elapsed_time} segundos")
    
    # Memória alocada
    memoria_usada = tracemalloc.get_traced_memory()[1] / 1024  # Usado em KB
    print(f"Memória após a execução do cenário 1: {memoria_usada} KB")
    # Finaliza o rastreamento
    tracemalloc.stop()
