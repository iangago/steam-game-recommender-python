import steam.steam_api as steam_api
import utils

# Plan: Improve recommending system by apllying this guideline:

#    INTENDED STRUCTURE

#recommended_games = [
#   {
#    'name': "Hades",
#    'game_id: 1234,
#    'score': 8,
#    'genres_matched': [Roguelike, Action],
#    'steam_rank': 12
#   }
#]

#      Genre Score
# favorite genre match   +5
# second genre match     +3
# third genre match      +2
# other top 5 genre      +1

#    Popularity Score
# rank 1-10    +3
# rank 11-30   +2
# rank 31-60   +1
# rank 61-100  +0

#             Diversity Bonus
# If a game matches multiple genres: +1 bonus

#                     **Final Score**
# final_score = genre_score + popularity_score + diversity_bonus

def recommend_games(top_100, user_favourite_genres, user_library_ids, game_cache):
    recommended_games = []

    #goes trough every games id
    game_rank = 0
    for id in top_100:
        popularity_score = 0
        genre_score = 0
        diversity_bonus = 0
        game_rank += 1

        #sets a flag
        game_in_library = False

        #goes trough each id in the users id list
        for user_game_id in user_library_ids:
            #if the id is the same as the current game that means the user already has it in his account
            if id == str(user_game_id):
                #set the flag as true and breaks out of the loop
                game_in_library = True
                break

        #if the flag is true skips the rest of the code
        if game_in_library == True:
            continue

        #now that its sure the game is not in the library of the user
        recommended_games_key = {}
        genres_matched = []

        #goes trough each genre of the current games genre list
        game_details = steam_api.get_game_details(int(id), game_cache)
        if not game_details:
            continue
        for genre in game_details:
            #if the current genre is in the users top genres it adds the game to the recommended list and breaks the loop
            if genre in user_favourite_genres:
                recommended_games_key['name'] = top_100[id]
                recommended_games_key['game_id'] = id
                #top 1 genre
                if genre == user_favourite_genres[0]:
                    genre_score += 5
                    genres_matched.append(genre)
                #top 2 genre
                elif genre == user_favourite_genres[1]:
                    genre_score += 3
                    genres_matched.append(genre)
                #top 3 genre
                elif genre == user_favourite_genres[2]:
                    genre_score += 2
                    genres_matched.append(genre)
                #top 4-5 genre
                else:
                    genre_score += 1
                    genres_matched.append(genre)

        #if no genres matched skips the rest of the code
        if genre_score == 0:
            continue

        #popularity score
        if game_rank > 0 and game_rank <= 10:
            popularity_score += 3
        elif game_rank > 10 and game_rank <= 30:
            popularity_score += 2
        elif game_rank > 30 and game_rank <= 60:
            popularity_score += 1
        
        #Diversity Bonus
        if len(genres_matched) > 1:
            diversity_bonus += 1

        final_score = genre_score + popularity_score + diversity_bonus

        recommended_games_key['score'] = final_score
        recommended_games_key['genres_matched'] = genres_matched
        recommended_games_key['steam_rank'] = game_rank

        recommended_games.append(recommended_games_key)

    #returns list
    return sorted(recommended_games, key=lambda game: game["score"], reverse=True)   




