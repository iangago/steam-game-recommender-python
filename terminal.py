import library
import utils
import analyzer
import recommender
import steam_api

def print_terminal(api_key):
    print("\nSTEAM GAME RECOMMENDER")
    print("----------------------")

    steam_id = input("\nEnter your SteamID64: ")

    #make user library
    print("\nAnalyzing Steam Library...")
    user_library = library.build_library(steam_id, api_key)

    user_library_games_ids = library.library_games_id(user_library)

    user_top_genres = utils.filter_genre_list(analyzer.top_genres(user_library))

    weekly_top_100 = steam_api.get_top_100()
    print("\nSearching Game Recommendations...")
    user_recommended_games = recommender.recommend_games(weekly_top_100, user_top_genres, user_library_games_ids)


    #print user library basic information
    print(f"\nTotal Games: {len(user_library)}")
    print(f"Total Playtime: {utils.get_total_hours(user_library):.1f} hours")

    #print top 3 genres
    print("\nTop Genres")
    i = 1
    for genre in user_top_genres:
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
        print(f"     Score: {game['score']}")
        print(f"     Genres Matched: {game['genres_matched']}")
        print(f"     Steam Rank: #{game['steam_rank']}\n")
        i += 1