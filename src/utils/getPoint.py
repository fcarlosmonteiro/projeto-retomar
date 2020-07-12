import requests 
import json
from API_Key import api_key

types = [
"accounting",
"airport",
"amusement_park",
"aquarium",
"art_gallery",
"atm",
"bakery",
"bank",
"bar",
"beauty_salon",
"bicycle_store",
"book_store",
"bowling_alley",
"bus_station",
"cafe",
"campground",
"car_dealer",
"car_rental",
"car_repair",
"car_wash",
"casino",
"cemetery",
"church",
"city_hall",
"clothing_store",
"convenience_store",
"courthouse",
"dentist",
"department_store",
"doctor",
"drugstore",
"electrician",
"electronics_store",
"embassy",
"fire_station",
"florist",
"funeral_home",
"furniture_store",
"gas_station",
"gym",
"hair_care",
"hardware_store",
"hindu_temple",
"home_goods_store",
"hospital",
"insurance_agency",
"jewelry_store",
"laundry",
"lawyer",
"library",
"light_rail_station",
"liquor_store",
"local_government_office",
"locksmith",
"lodging",
"meal_delivery",
"meal_takeaway",
"mosque",
"movie_rental",
"movie_theater",
"moving_company",
"museum",
"night_club",
"painter",
"park",
"parking",
"pet_store",
"pharmacy",
"physiotherapist",
"plumber",
"police",
"post_office",
"primary_school",
"real_estate_agency",
"restaurant",
"roofing_contractor",
"rv_park",
"school",
"secondary_school",
"shoe_store",
"shopping_mall",
"spa",
"stadium",
"storage",
"store",
"subway_station",
"supermarket",
"synagogue",
"taxi_stand",
"tourist_attraction",
"train_station",
"transit_station",
"travel_agency",
"university",
"veterinary_care",
"zoo"]
results = []

for type_search in types:
    key = api_key
    # Dois vizinhos
    location = "-25.746946, -53.055844"
    # Catete
    # location = "-22.925382,-43.180547"
    radius = "1500"
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+location+"&type="+type_search+"&radius="+radius+"&key="+key
    print("==================================================================================================")
    print(url)
    r = requests.get(url)
    response_json = r.json()
    if "results" in response_json:
        results.append(response_json["results"])
    if "next_page_token" in response_json:
        nextPageToken = response_json["next_page_token"]
    else:
        nextPageToken = ""
    while len(nextPageToken) > 0:
        r = requests.get(url+"&pagetoken="+nextPageToken)
        print("=======================================================================================")
        print(url+"&pagetoken="+nextPageToken)
        response_json = r.json()
        if "results" in response_json:
            results.append(response_json["results"])
        if "next_page_token" in response_json:
            nextPageToken = response_json["next_page_token"]
        else:
            nextPageToken = ""
resultJson = {}
resultJson["results"]=[] 
for r in results:
    for p in r:
        resultJson["results"].append(p)
with open("results-dv.json", "w") as res_file:
    data = json.dump(resultJson, res_file)