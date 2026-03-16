import steam.library as library
import utils
import core.analyzer as analyzer
import core.recommender as recommender
import steam.steam_api as steam_api
import storage.cache as cache
import visualization

def print_terminal(api_key):
    game_cache = cache.load_cache()

    print("\nSTEAM GAME RECOMMENDER")
    print("----------------------")

    steam_id = input("\nEnter your SteamID64: ")

    #make user library
    print("\nAnalyzing Steam Library...")
    user_library = library.build_library(steam_id, api_key, game_cache)

    user_library_games_ids = library.library_games_id(user_library)

    genre_playtime = analyzer.genre_playtime(user_library)

    sorted_genres = analyzer.sorted_genres(genre_playtime)

    top_5_genres = utils.top_five_genres(sorted_genres)

    weekly_top_100 = steam_api.get_top_100()
    print("\nSearching Game Recommendations...")
    user_recommended_games = recommender.recommend_games(weekly_top_100, top_5_genres, user_library_games_ids, game_cache)


    #print user library basic information
    print(f"\nTotal Games: {len(user_library)}")
    print(f"Total Playtime: {utils.get_total_hours(user_library):.1f} hours\n")

    

    #print top 3 genres
    print('Generating visualization...')
    visualization.plot_top_genres(sorted_genres)
    print('Chart saved to: charts/top_genres.png')

    print("\nTop Genres")
    i = 1
    for genre in top_5_genres:
        print(f"{i}. {genre}")
        i += 1      

    #print recommended games
    #     Game Rec Structure
    #1. Hades II
    #   Score: 8
    #   Genres matched: Roguelike, Action
    #   Steam Rank: #12

    i = 1
    print("\nRecommended Games")
    for game in user_recommended_games:
        print(f"{i}. {game['name']}")
        print(f"Score: {game['score']}")
        print(f"Genres Matched: {game['genres_matched']}")
        print(f"Steam Rank: #{game['steam_rank']}\n")
        i += 1

    cache.save_cache(game_cache)