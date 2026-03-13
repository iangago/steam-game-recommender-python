def get_total_hours(library):
    total_playtime = 0
    for dic in library:
        total_playtime += dic['playtime']

    return total_playtime / 60

def filter_genre_list(genre_list):
    list_without_playtime = []
    for keys in genre_list:
        list_without_playtime.append(keys[0])

    return list_without_playtime