import requests
from pprint import pprint

def ranking():
    response = requests.get(BASE_URL + path, params = params).json()
    high_rank = sorted(response["results"], key = lambda result: result["vote_average"], reverse=True)
    return high_rank[:5]

if __name__ == '__main__':
  BASE_URL = "https://api.themoviedb.org/3"
  path = "/movie/popular"
  params = {
    "api_key" : "21497b24f80e277f5a782f649aaafba8",
    'language' : 'ko-KR',
	  'region' : 'KR'
  }
  pprint(ranking())