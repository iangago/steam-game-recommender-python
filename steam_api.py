import requests

def get_owned_games(steam_id, API_KEY):
    #steampowered api wich returns the informations of steam user
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={steam_id}&include_appinfo=1" 

    response = requests.get(url) 

    data = response.json() 

    #gets the games
    games = data["response"]["games"] 

    return games

def get_game_details(appid):
    #steampowered api wich returns the informations of a game given its id
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"

    response = requests.get(url)

    data_id = response.json() 
    if not data_id:
        return None

    app_data = data_id.get(str(appid))
    if not app_data:
        return None
    
    game_data = app_data.get("data")
    if not game_data:
        return None

    genres = game_data.get("genres")
    if not genres:
        return None

    return_genres = []

    for section in genres:
        return_genres.append(section['description'])

    return return_genres

def get_top_100():
    #steamspy api wich returns Top 100 apps by players in the last two weeks
    url = "https://steamspy.com/api.php?request=top100in2weeks"

    response = requests.get(url)

    data = response.json()

    data_ids =  {}

    for id in data:
        data_ids[id] = data[id]['name']

    return data_ids

