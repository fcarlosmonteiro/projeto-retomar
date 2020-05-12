import json
import math

R = 6373.0


def calculateDistance(latDestination, lngDestination):
    with open('nearby.json', 'r') as json_file:
        data = json.load(json_file)
        for places in data['results']:
            location = places['geometry']['location']

            lat = math.radians(location['lat'])
            lng = math.radians(location['lng'])

            phi1, phi2 = math.radians(lat), math.radians(latDestination)
            dphi = math.radians(latDestination - lat)
            dlambda = math.radians(lngDestination - lng)

            a = math.sin(dphi/2)**2 + \
                math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2

            print(2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a)))


# informações do endereço do FCarlos
calculateDistance(-25.7521094, -53.0566417)
