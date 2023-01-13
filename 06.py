import requests
from pprint import pprint

def credits(title):
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
            movie_id = response["results"][i]["id"]
    if movie_id != None:
        return search_people(movie_id)
    elif movie_id == None:
        return None

def search_people(movie_id):
    BASE_URL2 = "https://api.themoviedb.org/3"
    path2 = "/movie/" + str(movie_id) + "/credits"
    params2 = {
        "api_key" : "21497b24f80e277f5a782f649aaafba8",
        "language" : "ko-KR",
        'region' : 'KR',
        'query' : movie_id
    }
    res = requests.get(BASE_URL2 + path2, params=params2).json()
    dictionary = {
        "cast" : [], "crew" : []
    }
    for i in range(len(res["cast"])):
        if res["cast"][i]["cast_id"] < 10:
            dictionary["cast"].append(res["cast"][i]["name"])
    for i in range(len(res["crew"])):
        if res["crew"][i]["department"] == "Directing":
            dictionary["crew"].append(res["crew"][i]["name"])
    return dictionary

if __name__ == '__main__':
    pprint(credits('기생충'))