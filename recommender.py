import steam_api
import utils

def recommend_games(top_100, user_favourite_genres, user_library_ids):
    recommended_games = {}

    #goes trough every games id
    for id in top_100:

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
        #goes trough each genre of the current games genre list
        game_details = steam_api.get_game_details(int(id))
        if not game_details:
            continue
        for genre in game_details:
            #if the current genre is in the users top genres it adds the game to the recommended list and breaks the loop
            if genre in user_favourite_genres:
                recommended_games[id] = top_100[id]
                break
    
    #returns list
    return recommended_games




