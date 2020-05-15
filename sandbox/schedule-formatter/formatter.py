def scheduleFormatterDictToJson(storeShiftsDict, shiftsAmount, daysAmount):

    storesSchedule = []

    if(daysAmount == 5):
        for store in storeShiftsDict:
            storeSchedule = {
                'store': store,
                'schedule': [{
                    'monday': storeShiftsDict[store][0:2],
                    'tuesday': storeShiftsDict[store][2:4],
                    'wednesday': storeShiftsDict[store][4:6],
                    'thursday': storeShiftsDict[store][6:8],
                    'friday': storeShiftsDict[store][8:10]
                }]
            }
            storesSchedule.append(storeSchedule)

    if(daysAmount == 6):
        for store in storeShiftsDict:
            storeSchedule = {
                'store': store,
                'schedule': [{
                    'monday': storeShiftsDict[store][0:2],
                    'tuesday': storeShiftsDict[store][2:4],
                    'wednesday': storeShiftsDict[store][4:6],
                    'thursday': storeShiftsDict[store][6:8],
                    'friday': storeShiftsDict[store][8:10]
                    'saturday': storeShiftsDict[store][10:12]
                }]
            }
            storesSchedule.append(storeSchedule)

    return storesSchedule

storeShifts = {
    'A': [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'B': [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    'C': [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    'D': [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    'E': [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    'F': [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    'G': [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    'H': [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
}

storeShift = scheduleFormatterDictToJson(storeShifts, 2, 5)
print(storeShift)