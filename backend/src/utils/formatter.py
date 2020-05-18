def scheduleFormatterDictToJson(storeShiftsDict, shiftsAmount, daysAmount,storeNameDict):

    storesSchedule = []

    if(daysAmount == 5):
        for store in storeShiftsDict:
            storeSchedule = {
                'storeId': store,
                'store': storeNameDict[store],
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
                'storeId': store,
                'store': storeNameDict[store],
                'schedule': [{
                    'monday': storeShiftsDict[store][0:2],
                    'tuesday': storeShiftsDict[store][2:4],
                    'wednesday': storeShiftsDict[store][4:6],
                    'thursday': storeShiftsDict[store][6:8],
                    'friday': storeShiftsDict[store][8:10],
                    'saturday': storeShiftsDict[store][10:12]
                }]
            }
            storesSchedule.append(storeSchedule)

    return storesSchedule