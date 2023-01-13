import requests
from pprint import pprint

def popular_count():
    response = requests.get(BASE_URL + path, params = params).json()
    return len(response["results"])
    #return response["total_results"]

if __name__ == '__main__':
    BASE_URL = "https://api.themoviedb.org/3"
    path = "/movie/popular"
    params = {
        "api_key" : "21497b24f80e277f5a782f649aaafba8",
    }
    pprint(popular_count())