import requests
from django.conf import settings

class CustomRetriever:
    def __init__(self):
        self.omdb_api_key = settings.OMDB_API_KEY
        self.tmdb_api_key = settings.TMDB_API_KEY
        self.omdb_api_url = 'http://www.omdbapi.com/'
        self.tmdb_base_url = 'https://api.themoviedb.org/3/'
        self.timeout = 10  

    def retrieve(self, query):
        omdb_results = self.retrieve_from_omdb(query)
        tmdb_results = self.retrieve_from_tmdb(query)
        merged_results = omdb_results + tmdb_results
        return merged_results

    def retrieve_from_omdb(self, query):
        try:
            params = {
                's': query,
                'apikey': self.omdb_api_key
            }
            response = requests.get(self.omdb_api_url, params=params, timeout=self.timeout)
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()
            if data.get('Response') == 'True':
                movies = data.get('Search', [])
                for movie in movies:
                    movie['source'] = 'OMDb'
                return movies
        except requests.RequestException as e:
            print(f"Error accessing OMDb API: {e}")
        return []

    def retrieve_from_tmdb(self, query):
        try:
            endpoint = 'search/movie'
            params = {
                'api_key': self.tmdb_api_key,
                'query': query
            }
            response = requests.get(self.tmdb_base_url + endpoint, params=params, timeout=self.timeout)
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()
            movies = data.get('results', [])
            for movie in movies:
                movie['source'] = 'TMDb'
            return movies
        except requests.RequestException as e:
            print(f"Error accessing TMDb API: {e}")
        return []
