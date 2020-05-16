import json
import math
from collections import defaultdict
R = 6373.0


class Entrada(object):
    def __init__(self):
        self.storeName = {}
        self.storeList()
        self.points = self.extractPoints()
        self.types = self.extractTypes()
        self.grafo = self.makeGraph(self.points)
        print(len(self.points))

    def extractPoints(self):
        points = {}
        with open('nearby.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for places in data['results']:
                location = places['geometry']['location']
                id = places['place_id']
                points[id] = location
        return points

    def extractTypes(self):
        types = {}
        with open('nearby.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for places in data['results']:
                typesList = places['types']
                id = places['place_id']
                types[id] = typesList
        return types

    def storeList(self):
        stores = []
        with open('nearby.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for places in data['results']:
                stores.append(places['place_id'])
                self.storeName[places['place_id']] = places['name']

        with open("stores.json", "w") as stores_file:
            data = json.dump(stores, stores_file)

    def calculateDistance(self, origin, destination):

        lat1 = math.radians(origin['lat'])
        lon1 = math.radians(origin['lng'])
        lat2 = math.radians(destination['lat'])
        lon2 = math.radians(destination['lng'])
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(
            dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        # in km
        return R * c

    def makeGraph(self, points):
        arrestas = []
        for index_u, key_u in enumerate(points):
            for index_v, key_v in enumerate(points):
                if (index_v > index_u):
                    distance = self.calculateDistance(points[key_u],
                                                      points[key_v])
                    if(distance < 0.01):
                        arrestas.append((key_u, key_v, distance))
        return Grafo(arrestas)


class Grafo(object):
    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v, peso in arestas:
            self.adiciona_arco(u, v, peso)

    def adiciona_arco(self, u, v, peso=0):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add((v, peso))
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add((u, peso))

    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}=({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]
