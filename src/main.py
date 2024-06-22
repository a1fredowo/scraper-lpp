from oop.AnimeCollection import AnimeCollection
import scraping_procedural as sp
import analisis_funcional as af
import json

def main():
    # Paso 1: Ejecutar el scraping procedural
    limit = int(input("Seleccione el número de animes a mostrar: "))
    top_anime = sp.get_top_anime(limit)
    if top_anime:
        print("Scraping completado exitosamente.")
        with open('top_anime.json', 'w') as file:
            json.dump(top_anime, file, indent=4)
        print("Datos guardados en top_anime.json")
    else:
        print("Error al obtener los datos de anime.")
        return

    # Paso 2: Cargar los datos en las clases orientadas a objetos
    collection = AnimeCollection()
    collection.load_from_json('top_anime.json')
    print("Datos cargados en la colección de animes.")

    # Paso 3: Ejecutar los análisis funcionales
    genre_scores = collection.get_scores_by_genre()
    mejores_scores, peores_scores = af.calcular_mejores_peores_scores_por_genero(genre_scores)
    print("Mejores Scores por Género:")
    print(mejores_scores[:5])
    print("Peores Scores por Género:")
    print(peores_scores[:5])

    year_scores = collection.get_scores_by_year()
    af.plot_scores_por_año(year_scores)

    scores_vs_episodes = collection.get_scores_vs_episodes()
    af.plot_scores_vs_episodios(scores_vs_episodes)

    genre_combinations = collection.get_genre_combinations()
    af.print_combinaciones_generos(genre_combinations)

    common_seasons = af.contar_animes_por_estacion(collection)
    print("Estaciones más comunes de emisión de anime:")
    for season, count in common_seasons:
        print(f"{season}: {count} animes")

if __name__ == "__main__":
    main()