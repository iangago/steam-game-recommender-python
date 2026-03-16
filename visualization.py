import matplotlib.pyplot as plt
import utils

def plot_top_genres(sorted_genres_playtime):
    sorted_genres_playtime = sorted_genres_playtime[:10]

    genres = utils.filter_genre_list(sorted_genres_playtime)
    playtime = utils.filter_genre_list_playtime(sorted_genres_playtime)
    playtime = utils.min_to_hour(playtime)

    genres = genres[::-1]
    playtime = playtime[::-1]

    plt.figure(figsize=(10,8), facecolor="#e3e3e3")

    plt.gca().set_facecolor("#e3e3e3")

    ax = plt.gca()

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.barh(genres, playtime, color="#cb500e")

    plt.xlabel("Hours Played")
    plt.ylabel("Genre")
    plt.title("Top Genres in Your Steam Library")

    plt.tight_layout()

    plt.savefig("charts/top_genres.png")
