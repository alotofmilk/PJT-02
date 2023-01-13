import requests
from pprint import pprint

def recommendation(title):
    BASE_URL = "https://api.themoviedb.org/3"
    path = "/search/movie"
    params = {
        "api_key" : "21497b24f80e277f5a782f649aaafba8",
        "language" : "ko-KR",
        'region' : 'KR',
        'query' : title
    }
    response = requests.get(BASE_URL + path, params=params).json()
    for i in range(len(response["results"])):
        if response["results"][i]["original_title"] == title:
            id_search = response["results"][i]["id"]
    if id_search != None:
        return make_recommendation(id_search)

def make_recommendation(id_search):
    BASE_URL = "https://api.themoviedb.org/3"
    path = "/movie/" + str(id_search) + "/recommendations"
    params = {
        "api_key" : "21497b24f80e277f5a782f649aaafba8",
        "language" : "ko-KR",
        'region' : 'KR',
    }
    res = requests.get(BASE_URL + path, params=params).json()
    make_list = []
    for i in range(len(res["results"])):
        make_list.append(res["results"][i]["title"])
    return make_list

if __name__ == '__main__':
    print(recommendation('기생충'), end=" ")