import requests
from bs4 import BeautifulSoup

def get_visits(game_id):
    url = f"https://www.roblox.com/games/{game_id}"
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    visits = soup.find("span", {"class": "game-stat-text"}).text
    return visits
