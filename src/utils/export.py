import csv
from .formatter import scheduleFormatterDictToJson
import json

class Export(object):
    def __init__(self, storeShiftsDict, entrada, turnos, quadrante=0):
        with open("results/Quadrante_"+str(quadrante) + '.json', 'w', encoding='utf-8') as json_file:
            data = json.dump(scheduleFormatterDictToJson(storeShiftsDict, 2, 5,entrada.storeName), json_file)

        for i in range(0, turnos):
            with open("csv/Quandrante_"+str(quadrante)+"-"+str(i) + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
                spamwriter = csv.writer(csvfile,
                                        delimiter=',',
                                        quotechar='|',
                                        quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(
                    ["Latitude-longitude information", "Name "])
                for store in storeShiftsDict:  # all shifts of a single store
                    if storeShiftsDict[store][i]:
                        spamwriter.writerow([
                            str(entrada.points[store]['lat']) + " " +
                            str(entrada.points[store]['lng']),
                            entrada.storeName[store]
                        ])
