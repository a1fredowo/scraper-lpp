import requests
from bs4 import BeautifulSoup
import time

def fetch_anime_page(page, headers):
    url = f"https://myanimelist.net/topanime.php?limit={page * 50}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        print(f"Error: {response.status_code}")
        return None

def parse_anime_list(soup, anime_list, limit, headers):
    rows = soup.find_all('tr', class_='ranking-list')
    for row in rows:
        if len(anime_list) >= limit:
            break
        title = row.find('h3', class_='anime_ranking_h3').text.strip()
        score = row.find('span', class_='score-label').text.strip()
        
        link = row.find('a', class_='hoverinfo_trigger fl-l ml12 mr8')['href']
        anime_details = get_anime_details(link, headers)
        
        anime_info = {
            'rank': len(anime_list) + 1,
            'title': title,
            'score': score,
            'genres': anime_details.get('genres', 'N/A'),
            'aired': anime_details.get('aired', 'N/A'),
            'episodes': anime_details.get('episodes', 'N/A')
        }
        anime_list.append(anime_info)
    return anime_list

def get_anime_details(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        genres = [genre.text for genre in soup.find_all('span', itemprop='genre')]
        aired = soup.find('span', class_='information season').text.strip() if soup.find('span', class_='information season') else 'N/A'
        episodes_tag = soup.find('span', string='Episodes:')
        episodes = episodes_tag.next_sibling.strip() if episodes_tag else 'N/A'
        
        return {
            'genres': ', '.join(genres), 
            'aired': aired,
            'episodes': episodes
        }
    else:
        print(f"Error obtaining details: {response.status_code}")
        return {}

def get_top_anime(limit):
    anime_list = []
    page = 0
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    while len(anime_list) < limit:
        soup = fetch_anime_page(page, headers)
        if soup:
            anime_list = parse_anime_list(soup, anime_list, limit, headers)
        else:
            break
        page += 1
        time.sleep(1)

    return anime_list
