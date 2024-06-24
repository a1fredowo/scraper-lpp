from collections import defaultdict
from itertools import combinations

class AnimeCollection:
    def __init__(self):
        self._animes = []

    def add_anime(self, anime):
        # Añade un objeto Anime a la colección.
        self._animes.append(anime)

    def add_animes(self, animes):
        # Añade múltiples objetos Anime a la colección.
        self._animes.extend(animes)

    def get_animes(self):
        # Devuelve la lista de animes en la colección.
        return self._animes

    def get_anime_by_rank(self, rank):
        # Devuelve el anime con el rango especificado.
        for anime in self._animes:
            if anime.rank == rank:
                return anime
        return None

    def get_anime_by_title(self, title):
        # Devuelve el anime con el título especificado.
        for anime in self._animes:
            if anime.title.lower() == title.lower():
                return anime
        return None

    def get_scores_by_genre(self):
        # Devuelve los scores agrupados por género.
        genre_scores = defaultdict(list)
        for anime in self._animes:
            for genre in anime.genres:
                genre_scores[genre].append(anime.score)
        return genre_scores

    def get_scores_by_year(self):
        # Devuelve los scores agrupados por año.
        year_scores = defaultdict(list)
        for anime in self._animes:
            year = anime.aired.split()[-1] if anime.aired != "N/A" else "Unknown"
            year_scores[year].append(anime.score)
        return year_scores

    def get_scores_vs_episodes(self):
        # Devuelve una lista de tuplas (episodios, score) para cada anime.
        scores_vs_episodes = [(anime.episodes, anime.score) for anime in self._animes if anime.episodes is not None]
        return scores_vs_episodes

    def get_animes_by_season(self):
        # Devuelve la cantidad de animes por temporada.
        season_counts = defaultdict(int)
        for anime in self._animes:
            if anime.aired != "N/A":
                season = anime.aired.split()[0]
                season_counts[season] += 1
        return season_counts

    def get_top_genre_pairs(self, top_n=10):
        # Devuelve los pares de combinaciones de géneros más comunes.
        genre_combinations = defaultdict(int)
        for anime in self._animes:
            genres = sorted(anime.genres)
            if len(genres) > 1:
                for combo in combinations(genres, 2):
                    genre_combinations[combo] += 1
        most_common_pairs = sorted(genre_combinations.items(), key=lambda x: x[1], reverse=True)
        return most_common_pairs[:top_n]

    def __repr__(self):
        return f"AnimeCollection({len(self._animes)} animes)"