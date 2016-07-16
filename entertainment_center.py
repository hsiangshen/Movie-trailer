
#call phyton code fresh_tomatoes for browser css format and opening movie trailer, media for class Movie
import fresh_tomatoes
import media

sword_rain = media.Movie("Reign of Assassins",
    "A narration tells of a legendary Indian Buddhist monk, Bodhi and the belief that his mummified remains has mystical powers.",
    "https://upload.wikimedia.org/wikipedia/en/6/64/Reign-of-Assassins.jpg",
    "https://www.youtube.com/watch?v=IczLF2rcs10")

tais_toi = media.Movie("Ruby and Quentin",
    "Two guys escaped from a jail",
    "https://upload.wikimedia.org/wikipedia/en/1/1f/Tais-toi_poster.jpg",
    "https://www.youtube.com/watch?v=BSFfMs9teMY")

red_turle = media.Movie("La Tortue rouge",
    "a red tutler journey",
    "https://upload.wikimedia.org/wikipedia/en/f/fe/The_Red_Turtle.png",
    "https://www.youtube.com/watch?v=y3uYequDQqc")

hotarubi_no_morie = media.Movie("Into the forest of firefly light",
    "A young girl had a strange relationship with a spirit",
    "https://upload.wikimedia.org/wikipedia/en/f/fd/Hotarubi_no_Mori_e_%28manga_cover%29.jpg",
    "https://www.youtube.com/watch?v=TFvezWFnaHw")

time_of_eve = media.Movie("The time of Eve",
    "In the near furture, the relationship between people and robort become completcate.",
    "https://upload.wikimedia.org/wikipedia/en/f/fa/Ivu_no_Jikan_poster.jpeg",
    "https://www.youtube.com/watch?v=5CrNNs-37As")

my_neighbor_totoro = media.Movie("My neighbor Totoro",
    "The adventure for 2 little girls after their family moved into an old country house.",
    "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
    "https://www.youtube.com/watch?v=92a7Hj0ijLs")


movies = [
            sword_rain, tais_toi, red_turle, 
            hotarubi_no_morie, time_of_eve, my_neighbor_totoro
        ]
fresh_tomatoes.open_movies_page(movies)

