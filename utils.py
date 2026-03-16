#returns total playtime in hours
def get_total_hours(library):
    total_playtime = 0
    for dic in library:
        total_playtime += dic['playtime']

    return total_playtime / 60

#returns the playtime list but in hours
def min_to_hour(playtime_min):
    playtime_hours = []

    for playtime in playtime_min:
        playtime_hours.append(playtime / 60)

    return playtime_hours

#returns an array with the top five genres
def top_five_genres(sorted_genres):
    top_five = [sorted_genres[0][0], sorted_genres[1][0], sorted_genres[2][0], sorted_genres[3][0], sorted_genres[4][0]]

    return top_five

#returns list with only the genres
def filter_genre_list(genre_list):
    list_without_playtime = []
    for keys in genre_list:
        list_without_playtime.append(keys[0])

    return list_without_playtime

#returns list with only playtime
def filter_genre_list_playtime(genre_list):
    list__playtime = []
    for keys in genre_list:
        list__playtime.append(keys[1])

    return list__playtime