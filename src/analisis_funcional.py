import matplotlib.pyplot as plt
from functools import reduce

"""Calcula los mejores y peores scores promedio por género."""
def calcular_mejores_peores_scores_por_genero(genre_scores):
    # Filtrar géneros con listas no vacías y calcular promedios
    promedio_scores = {genre: reduce(lambda a, b: a + b, scores) / len(scores)
                       for genre, scores in genre_scores.items() if scores}
    
    # Ordenar los géneros por su promedio de scores
    mejores_scores = sorted(promedio_scores.items(), key=lambda x: x[1], reverse=True)
    peores_scores = sorted(promedio_scores.items(), key=lambda x: x[1])
    
    return mejores_scores, peores_scores

"""Genera y guarda un gráfico de la evolución de scores promedio a través del tiempo."""
def plot_scores_por_año(year_scores):
    # Filtrar años con listas no vacías y calcular promedios
    years = sorted(year_scores.keys())
    scores = list(map(lambda year: sum(year_scores[year]) / len(year_scores[year]), 
                      filter(lambda year: year_scores[year], years)))
    
    plt.figure(figsize=(14, 7))
    plt.plot(years, scores, marker='o', linestyle='-', color='b', label='Score Promedio')
    plt.xlabel('Año', fontsize=14)
    plt.ylabel('Score Promedio', fontsize=14)
    plt.title('Evolución de Scores a través del tiempo', fontsize=16)
    plt.legend(fontsize=12)
    plt.xticks(fontsize=12, rotation=45)  # Rotar las etiquetas de los años
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.savefig('year_scores.png', bbox_inches='tight')

"""Genera y guarda un gráfico de dispersión de scores versus número de episodios."""
def plot_scores_vs_episodios(scores_vs_episodes):
    episodes, scores = zip(*scores_vs_episodes)

    plt.figure(figsize=(12, 6))
    plt.scatter(episodes, scores, color='b', label='Score por Episodio')
    plt.xlabel('Número de Episodios', fontsize=14)
    plt.ylabel('Score', fontsize=14)
    plt.title('Relación entre Número de Episodios y Score', fontsize=16)
    plt.legend(fontsize=12)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.savefig('scoresvepisodes.png', bbox_inches='tight')

"""Imprime los n pares de géneros más comunes."""
def print_top_n_pares_generos(genre_pairs, n=10):
    top_n_pairs = sorted(genre_pairs, key=lambda x: x[1], reverse=True)[:n]
    for pair, count in top_n_pairs:
        print(f"{pair}: {count} veces")

"""Cuenta y ordena los animes por estación."""
def contar_animes_por_estacion(collection):
    season_counts = collection.get_animes_by_season()
    sorted_seasons = sorted(season_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_seasons