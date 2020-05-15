import csv


class Export(object):
    def __init__(self, storeShiftsDict, entrada):
        for i in range(0, 13):
            strCSV = ""
            with open(str(i) + '.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile,
                                        delimiter=',',
                                        quotechar='|',
                                        quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(
                    ["Latitude-longitude information", "Name "])
                for store in storeShiftsDict:  # all shifts of a single store
                    spamwriter.writerow([
                        str(entrada.points[store]['lat']) + " " +
                        str(entrada.points[store]['lng']),
                        entrada.storeName[store]
                    ])
