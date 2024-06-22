from collections import defaultdict
from .Anime import Anime

class AnimeCollection:
    def __init__(self):
        self._animes = []

    def add_anime(self, anime):
        self._animes.append(anime)

    def get_animes(self):
        return self._animes

    def get_anime_by_rank(self, rank):
        for anime in self._animes:
            if anime.rank == rank:
                return anime
        return None

    def get_anime_by_title(self, title):
        for anime in self._animes:
            if anime.title.lower() == title.lower():
                return anime
        return None

    def load_from_json(self, json_file):
        import json
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                anime = Anime(item['rank'], item['title'], item['score'], item['genres'], item['aired'], item['episodes'])
                self.add_anime(anime)

    def get_scores_by_genre(self):
        from collections import defaultdict
        genre_scores = defaultdict(list)
        for anime in self._animes:
            for genre in anime.genres:
                genre_scores[genre].append(anime.score)
        return genre_scores

    def get_scores_by_year(self):
        from collections import defaultdict
        year_scores = defaultdict(list)
        for anime in self._animes:
            year = anime.aired.split()[-1] if anime.aired != "N/A" else "Unknown"
            year_scores[year].append(anime.score)
        return year_scores

    def get_scores_vs_episodes(self):
        scores_vs_episodes = [(anime.episodes, anime.score) for anime in self._animes if anime.episodes is not None]
        return scores_vs_episodes

    def get_genre_combinations(self):
        from collections import defaultdict
        genre_combinations = defaultdict(int)
        for anime in self._animes:
            genres_tuple = tuple(sorted(anime.genres))
            genre_combinations[genres_tuple] += 1
        return genre_combinations
    
    def get_animes_by_season(self):
        season_counts = defaultdict(int)
        for anime in self._animes:
            if anime.aired != "N/A":
                season = anime.aired.split()[0]
                season_counts[season] += 1
        return season_counts