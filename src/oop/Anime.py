class Anime:
    def __init__(self, rank, title, score, genres, aired, episodes):
        self._rank = rank
        self._title = title
        self._score = float(score)
        self._genres = genres.split(", ")
        self._aired = aired
        self._episodes = int(episodes) if episodes.isdigit() else None

    @property
    def rank(self):
        return self._rank

    @property
    def title(self):
        return self._title

    @property
    def score(self):
        return self._score

    @property
    def genres(self):
        return self._genres

    @property
    def aired(self):
        return self._aired

    @property
    def episodes(self):
        return self._episodes

    def __str__(self):
        return f"Anime(title={self._title}, score={self._score}, genres={self._genres}, aired={self._aired}, episodes={self._episodes})"