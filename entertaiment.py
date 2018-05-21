#to import fresh_tomatoes media files
import fresh_tomatoes
import media
#insatnces for class movie
Avengers= media.Movie("Avengers: Infinity War","action",
                     "https://preview.ibb.co/icTDFo/avengers_infinity_war_imax.jpg",
                     "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
Deadpool=media.Movie("Deadpoll 2","action",
                    "https://preview.ibb.co/cOeLvo/deadpool_2_movie_poster.jpg",
                    "https://www.youtube.com/watch?v=wLeGWcVeIZ4")
Black=media.Movie("Black Panther","action",
                    "https://image.ibb.co/iFHjMT/black_panther_poster_sfkn_640.jpg",
                    "https://www.youtube.com/watch?v=xjDjIWPwcPU")
Ant=media.Movie("Ant Man and Wasp","action",
                    "https://preview.ibb.co/m8L4MT/Ant_Man_and_The_Wasp_poster_2.jpg",
                    "https://www.youtube.com/watch?v=8_rTIAOohas")
Rampage= media.Movie("Rampage","action",
                    "https://preview.ibb.co/hmYfvo/rampage.jpg",
                    "https://www.youtube.com/watch?v=yrkVDJ4L38U")

movies=[Avengers,Deadpool,Black,Ant,Rampage]
#to open web browser with argument movies
fresh_tomatoes.open_movies_page(movies)