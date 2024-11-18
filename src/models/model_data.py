from geopy.distance import geodesic


class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_rota(self, origem, destino, coordenadas_origem, coordenadas_destino):
        # Calcular a distância entre os pontos
        distancia = geodesic(coordenadas_origem, coordenadas_destino).km

        # Adicionar a rota bidirecional no grafo
        if origem not in self.adjacencias:
            self.adjacencias[origem] = []
        if destino not in self.adjacencias:
            self.adjacencias[destino] = []

        self.adjacencias[origem].append((destino, distancia))
        self.adjacencias[destino].append((origem, distancia))

    def obter_distancia(self, origem, destino):
        if origem in self.adjacencias:
            for vizinho, distancia in self.adjacencias[origem]:
                if vizinho == destino:
                    return distancia
        return float('inf')


class Entrega:
    def __init__(self, destino, prazo, peso, coordenadas):
        self.destino = destino
        self.prazo = prazo
        self.peso = peso
        self.coordenadas = coordenadas


class Caminhao:
    def __init__(self, capacidade, horas_diarias, centro_distribuicao, coordenadas):
        self.capacidade = capacidade
        self.horas_diarias = horas_diarias
        self.centro_distribuicao = centro_distribuicao
        self.coordenadas = coordenadas
        self.entregas = []
