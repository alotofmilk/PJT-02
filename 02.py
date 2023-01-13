import requests
from pprint import pprint

def vote_average_movies():
  response = requests.get(BASE_URL + path, params = params).json()
  popular_movies = []
  for i in range(len(response["results"])):
    if response["results"][i]["vote_average"] >= 8.0:
      popular_movies.append(response["results"][i])
  return popular_movies

if __name__ == '__main__':
  BASE_URL = "https://api.themoviedb.org/3"
  path = "/movie/popular"
  params = {
    "api_key" : "21497b24f80e277f5a782f649aaafba8",
    'language' : 'ko-KR',
	  'region' : 'KR'
  }
  pprint(vote_average_movies())