import json


def cleaner(fileFrom, fileTo):
    places = {"results": []}
    with open(fileFrom, 'r') as json_file:
        data = json.load(json_file)

        for place in data['results']:
            if 'bar' in place['types']:
                places['results'].append(place)

        with open(fileTo, 'w') as outfile:
            json.dump(places, outfile)


cleaner('results.json', 'nocturnal-results.json')
