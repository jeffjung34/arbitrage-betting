import requests
from config import API_KEY

def fetch_sports():
    url = f'https://api.the-odds-api.com/v4/sports/?apiKey={API_KEY}'
    response = requests.get(url)
    return response.json()

def fetch_odds(sport_key, regions='us', markets='h2h', odds_format='decimal'):
    url = f'https://api.the-odds-api.com/v4/sports/{sport_key}/odds/'
    response = requests.get(url, params={
        'apiKey': API_KEY,
        'regions': regions,
        'markets': markets,
        'oddsFormat': odds_format,
    })
    return response.json()
