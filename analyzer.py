def top_genres(game_library):
    genres_playtime = genre_playtime(game_library)

    #sort trough the dictionary putting the highest playtime first
    sorted_genres = sorted(genres_playtime.items(), key=lambda x: x[1], reverse=True)

    top_5_genres = [sorted_genres[0], sorted_genres[1], sorted_genres[2], sorted_genres[3], sorted_genres[4]]

    #return sorted list
    return top_5_genres
    
def genre_playtime(game_library):
    genre_list = {}

    #goes trough the dictionaries
    for dic in game_library:
        #if there are information in the 'genres' key
        if dic['genres'] != None:
            #goes trough the list
            for genre in dic['genres']:
                #if the genre was not added to the final list it adds it
                if genre not in genre_list:
                    genre_list[genre] = 0

                #adds the playtime to the genre key
                genre_list[genre] += dic['playtime']
    
    #returns dictionary
    #this genre list has the hours in it as well 
    return genre_list