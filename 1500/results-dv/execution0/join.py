
import json

full_result = []
for i in range(0,4):
    with open("Quadrante_"+str(i)+".json", "r", encoding='utf-8') as resultado_file:
        data_res = json.load(resultado_file)
        for data in data_res:
            with open('000000000000
            nearby-dv.json', 'r', encoding='utf-8') as json_file:
                data_entrada = json.load(json_file)
                for places in data_entrada["results"]:
                    if data["storeId"] == places["place_id"]:
                        data["types"] = places["types"]
                        full_result.append(data)
                        break
with open('schedule-dv.json', 'w', encoding='utf-8') as json_file:
    data = json.dump(full_result, json_file)