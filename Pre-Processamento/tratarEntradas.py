import json
import math
from grafo import Grafo

R = 6373.0

def extractPoints():
    points = {}
    with open('nearby.json', 'r') as json_file:
        data = json.load(json_file)
        for places in data['results']:
            location = places['geometry']['location']
            id = places['place_id']
            points[id] = location
    return points


def calculateDistance(origin, destination):

    lat1 = math.radians(origin['lat'])
    lon1 = math.radians(origin['lng'])
    lat2 = math.radians(destination['lat'])
    lon2 = math.radians(destination['lng'])
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(
        dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # in km
    return R * c


def makeGraph(points):
    arrestas = []
    for index_u, key_u in enumerate(points):
        for index_v, key_v in enumerate(points):
            if (index_v > index_u):
                distance = calculateDistance(points[key_u], points[key_v])
                arrestas.append((key_u, key_v, distance))
    return Grafo(arrestas)


points = extractPoints()
grafo = makeGraph(points)
