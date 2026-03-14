import json

CACHE_PATH = "storage/cache.json"

def load_cache():
    try:
        with open(CACHE_PATH, "r") as file:
            data = json.load(file)
            return data
        
    except FileNotFoundError:
        return {}

def save_cache(cache):
    with open(CACHE_PATH, "w") as file:
        json.dump(cache, file, indent=4)

def get_cached_game(cache, appid):
    if str(appid) in cache:
        return cache[str(appid)]
    
    return None

def add_game_to_cache(cache, appid, name, genres):
    if str(appid) not in cache:
        cache[str(appid)] = {"name": name, "genres": genres}
