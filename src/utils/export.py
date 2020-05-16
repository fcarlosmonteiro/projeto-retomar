import csv


class Export(object):
    def __init__(self, storeShiftsDict, entrada, turnos):
        for i in range(0, turnos):
            strCSV = ""
            with open("csv/"+str(i) + '.csv', 'w', newline='') as csvfile:
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
