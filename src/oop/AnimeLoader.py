import json
from .Anime import Anime

class AnimeLoader:
    # Clase con un metodo estatico para cargar animes desde un archivo JSON.
    @staticmethod
    def load_from_json(json_file):
        # Carga animes desde un archivo JSON y devuelve una lista de objetos Anime.
        animes = []
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    anime = Anime(item['rank'], item['title'], item['score'], item['genres'], item['aired'], item['episodes'])
                    animes.append(anime)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON file: {e}")
        return animes