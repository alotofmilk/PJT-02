import requests
from pprint import pprint

def search_movie(title):
    BASE_URL = "https://api.themoviedb.org/3"
    path = "/search/movie"
    params = {
        "api_key" : "21497b24f80e277f5a782f649aaafba8",
        "language" : "ko-KR",
        'query' : title
    }
    response = requests.get(BASE_URL + path, params=params).json()
    for i in range(len(response["results"])):
        if title in response["results"][i]["title"]:
            return response["results"][i]["id"]
if __name__ == '__main__':
    pprint(search_movie("기생충"))