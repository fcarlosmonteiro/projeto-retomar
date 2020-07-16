import csv
from .formatter import scheduleFormatterDictToJson
import json
import LocalConfig
import os.path


class Export(object):
    def __init__(self, storeShiftsDict, entrada, turnos, quadrante=0, execution=1):
        if not os.path.isdir("results"+LocalConfig.local+"/execution"+str(execution)):
            os.makedirs("results"+LocalConfig.local+"/execution"+str(execution))
        with open("results"+LocalConfig.local+"/execution"+str(execution)+"/Quadrante_"+str(quadrante) + '.json', 'w', encoding='utf-8') as json_file:
            data = json.dump(scheduleFormatterDictToJson(storeShiftsDict, 2, 5,entrada.storeName), json_file)
        if not os.path.isdir("results"+LocalConfig.local+"/execution"+str(execution)+"/csv"):
            os.makedirs("results"+LocalConfig.local+"/execution"+str(execution)+"/csv")
        for i in range(0, turnos):
            with open("results"+LocalConfig.local+"/execution"+str(execution)+"/csv/Quandrante_"+str(quadrante)+"-"+str(i) + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
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
