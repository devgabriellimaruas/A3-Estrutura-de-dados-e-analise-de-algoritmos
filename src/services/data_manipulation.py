from src.models.model_data import Grafo, Entrega, Caminhao
import math


def alocar_entregas(entregas, caminhoes, grafo):
    for entrega in entregas:
        caminhoes_ordenados = sorted(
            caminhoes,
            key=lambda caminhao: grafo.obter_distancia(caminhao.centro_distribuicao, entrega.destino),
        )

        alocado = False
        motivo_rejeicao = None

        for caminhao in caminhoes_ordenados:
            distancia = grafo.obter_distancia(caminhao.centro_distribuicao, entrega.destino)
            tempo_viagem = distancia / 60
            dias_necessarios = math.ceil(tempo_viagem / caminhao.horas_diarias)

            if dias_necessarios > entrega.prazo:
                motivo_rejeicao = f"Prazo insuficiente (necessário: {dias_necessarios} dias, disponível: {entrega.prazo} dias)."
                continue

            if sum(e.peso for e in caminhao.entregas) + entrega.peso > caminhao.capacidade:
                motivo_rejeicao = f"Capacidade insuficiente no caminhão de {caminhao.centro_distribuicao}."
                continue

            caminhao.entregas.append(entrega)
            alocado = True
            break

        if not alocado:
            print(f"Entrega para {entrega.destino} não pôde ser alocada.")
            if motivo_rejeicao:
                print(f"Motivo: {motivo_rejeicao}")


def gerar_cenario_mais_entregas(caminhoes_por_centro=5):
    grafo = Grafo()

    # Mocamos as coordenadas das localização e destinos
    locais = {
        "Belém": (-1.45502, -48.50237),
        "Recife": (-8.04756, -34.877),
        "São Paulo": (-23.55052, -46.63331),
        "Curitiba": (-25.42895, -49.26714),
        "São Luís": (-2.52998, -44.3028),
        "Salvador": (-12.9714, -38.5014),
        "Rio de Janeiro": (-22.9068, -43.1729),
        "Porto Alegre": (-30.0346, -51.2177),
        "Manaus": (-3.10194, -60.025),
        "Fortaleza": (-3.71722, -38.5434),
        "Brasília": (-15.77972, -47.92972),
        "Natal": (-5.79448, -35.211),
        "Campo Grande": (-20.4697, -54.6201),
        "Vitória": (-20.3155, -40.3128),
        "João Pessoa": (-7.1195, -34.845),
    }

    # Adicionando rotas dinamicamente ao grafo
    for origem, coord_origem in locais.items():
        for destino, coord_destino in locais.items():
            if origem != destino:
                grafo.adicionar_rota(origem, destino, coord_origem, coord_destino)

    # Criação de entregas com locais fixos
    entregas = [
        Entrega("São Luís", 2, 500, locais["São Luís"]),
        Entrega("Salvador", 3, 800, locais["Salvador"]),
        Entrega("Rio de Janeiro", 1, 400, locais["Rio de Janeiro"]),
        Entrega("Porto Alegre", 4, 600, locais["Porto Alegre"]),
        Entrega("Manaus", 5, 1000, locais["Manaus"]),
        Entrega("Fortaleza", 2, 700, locais["Fortaleza"]),
        Entrega("Brasília", 3, 800, locais["Brasília"]),
        Entrega("Natal", 2, 400, locais["Natal"]),
        Entrega("Campo Grande", 4, 600, locais["Campo Grande"]),
        Entrega("Vitória", 3, 700, locais["Vitória"]),
        Entrega("João Pessoa", 2, 300, locais["João Pessoa"]),
    ]

    # Criação de caminhões
    caminhoes = []
    for centro in ["Belém", "Recife", "São Paulo", "Curitiba"]:
        for i in range(caminhoes_por_centro):
            caminhoes.append(
                Caminhao(1000 + i * 500, 8, centro, locais[centro])
            )

    return grafo, entregas, caminhoes

def gerar_cenario_menos_entregas(caminhoes_por_centro=5):
    grafo = Grafo()

    # Mocamos as coordenadas das localização e destinos
    locais = {
        "Belém": (-1.45502, -48.50237),
        "Recife": (-8.04756, -34.877),
        "São Paulo": (-23.55052, -46.63331),
        "Curitiba": (-25.42895, -49.26714),
        "São Luís": (-2.52998, -44.3028),
        "Salvador": (-12.9714, -38.5014),
        "Rio de Janeiro": (-22.9068, -43.1729),
        "Porto Alegre": (-30.0346, -51.2177),
        "Manaus": (-3.10194, -60.025),
        "Fortaleza": (-3.71722, -38.5434),
        "Brasília": (-15.77972, -47.92972),
        "Natal": (-5.79448, -35.211),
        "Campo Grande": (-20.4697, -54.6201),
        "Vitória": (-20.3155, -40.3128),
        "João Pessoa": (-7.1195, -34.845),
    }

    # Adicionando rotas dinamicamente ao grafo
    for origem, coord_origem in locais.items():
        for destino, coord_destino in locais.items():
            if origem != destino:
                grafo.adicionar_rota(origem, destino, coord_origem, coord_destino)

    # Criação de entregas com menos locais
    entregas = [
        Entrega("São Luís", 2, 500, locais["São Luís"]),
        Entrega("Salvador", 3, 800, locais["Salvador"]),
        Entrega("Rio de Janeiro", 1, 400, locais["Rio de Janeiro"]),
    ]

    # Criação de caminhões
    caminhoes = []
    for centro in ["Belém", "Recife", "São Paulo", "Curitiba"]:
        for i in range(caminhoes_por_centro):
            caminhoes.append(
                Caminhao(1000 + i * 500, 8, centro, locais[centro])
            )

    return grafo, entregas, caminhoes
