import requests
from bs4 import BeautifulSoup
import json
import time

def get_top_anime(limit):
    anime_list = []
    page = 0
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    } # Encabezados para simular una solicitud de un navegador web y evitar ser bloqueado por el server

    while len(anime_list) < limit:
        url = f"https://myanimelist.net/topanime.php?limit={page * 50}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            rows = soup.find_all('tr', class_='ranking-list')
            for row in rows:
                if len(anime_list) >= limit:
                    break
                title = row.find('h3', class_='anime_ranking_h3').text.strip()
                score = row.find('span', class_='score-label').text.strip()
                
                # Obtener el enlace a la página del anime
                link = row.find('a', class_='hoverinfo_trigger fl-l ml12 mr8')['href']
                
                # Scraping adicional en la página del anime
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
        else:
            print(f"Error: {response.status_code}")
            break

        page += 1 # Cambiar a la siguiente página
        time.sleep(1)  # Esperar 1 segundo para evitar ser bloqueado por el server

    return anime_list

def get_anime_details(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Obtener géneros
        genres = [genre.text for genre in soup.find_all('span', itemprop='genre')]
        
        # Obtener fecha de estreno
        aired = soup.find('span', class_='information season').text.strip() if soup.find('span', class_='information season') else 'N/A'
        
        # Obtener número de episodios
        episodes_tag = soup.find('span', string='Episodes:')
        episodes = episodes_tag.next_sibling.strip() if episodes_tag else 'N/A'
        
        return {
            'genres': ', '.join(genres), 
            'aired': aired,
            'episodes': episodes
        }
    else:
        print(f"Error obtaining details: {response.status_code}") # Mensaje de error si no se puede obtener la información
        return {}

def main():
    limit = int(input("Cuántos animes quieres que se muestren: ")) # Número de animes a mostrar
    top_anime = get_top_anime(limit) # Obtener la lista de los top animes
    if top_anime:
        print(json.dumps(top_anime, indent=4)) # Mostrar la lista de animes
        with open('top_anime.json', 'w') as file: # Guardar la lista de animes en un archivo JSON
            json.dump(top_anime, file, indent=4) 
        print("Data saved to top_anime.json") # Mensaje de confirmación
    else:
        print("Failed to retrieve top anime.") # Mensaje de error 

if __name__ == "__main__":
    main()