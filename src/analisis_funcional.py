import matplotlib.pyplot as plt

def calcular_mejores_peores_scores_por_genero(genre_scores):
    promedio_scores = {genre: sum(scores)/len(scores) for genre, scores in genre_scores.items()}
    mejores_scores = sorted(promedio_scores.items(), key=lambda x: x[1], reverse=True)
    peores_scores = sorted(promedio_scores.items(), key=lambda x: x[1])
    return mejores_scores, peores_scores

def plot_scores_por_año(year_scores):
    years = sorted(year_scores.keys())
    scores = [sum(year_scores[year])/len(year_scores[year]) for year in years]
    
    plt.figure(figsize=(12, 6))
    plt.plot(years, scores, marker='o')
    plt.xlabel('Año')
    plt.ylabel('Score Promedio')
    plt.title('Evolución de Scores a través del tiempo')
    plt.savefig('year_scores.png')

def plot_scores_vs_episodios(scores_vs_episodes):
    episodes, scores = zip(*scores_vs_episodes)
    
    plt.figure(figsize=(12, 6))
    plt.scatter(episodes, scores)
    plt.xlabel('Número de Episodios')
    plt.ylabel('Score')
    plt.title('Relación entre Número de Episodios y Score')
    plt.savefig('scoresvepisodes.png')

def print_combinaciones_generos(genre_combinations):
    sorted_combinations = sorted(genre_combinations.items(), key=lambda x: x[1], reverse=True)
    for combination, count in sorted_combinations:
        print(f"{combination}: {count} veces")

def contar_animes_por_estacion(collection):
    season_counts = collection.get_animes_by_season()
    sorted_seasons = sorted(season_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_seasons