import steam.steam_api as steam_api

#INTENDED STRUCTURE
#library = [
#   {
#    'name': "Hades",
#    'game_id': 435
#    'playtime': 5400}}
#    'genres': ["Action", "Roguelike"]
#   }
#]

def build_library(steam_id, api_key, game_cache):
    #gets the games from the function
    games = steam_api.get_owned_games(steam_id, api_key)

    library_list = []

    #iterates trough each game
    for game in games:
        #builds the structure for the dictionary
        library = {'name': game['name'],
                   'game_id': game['appid'],
                   'playtime': game['playtime_forever'],
                   'genres': steam_api.get_game_details(game['appid'], game_cache)}
        
        #adds dictionary to main library
        library_list.append(library)
    
    return library_list

def library_games_id(library):
    library_ids = []
    #gets every games id and adds it to the list
    for dic in library:
        library_ids.append(dic['game_id'])

    return library_ids