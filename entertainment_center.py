import media
import fresh_tomatoes

#Here we create 6 instances of the Movie class located in the media.py file
# Each instance of the Movie class has 4 parameters, Movie title, a description of the movie, a poster image, and a youtube link to the trailer.

anchorman = media.Movie("Anchorman",
                        "A comedy about Ron Burgandy, an anchorman for the fictional KVWN and his news team",
                        "http://ia.media-imdb.com/images/M/MV5BMTQ2MzYwMzk5Ml5BMl5BanBnXkFtZTcwOTI4NzUyMw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=Ip6GolC7Mk0")


pineapple_express = media.Movie("Pineapple Express",
                                "Seth Rogan witnesses a murder by a weed cartel and goes to his pot dealer for help",
                                "http://ia.media-imdb.com/images/M/MV5BMTY1MTE4NzAwM15BMl5BanBnXkFtZTcwNzg3Mjg2MQ@@._V1_SX640_SY720_.jpg",
                                "https://www.youtube.com/watch?v=_GnV2u30oOU"
                                )

the_other_guys = media.Movie("The Other Guys", " A comedy about 2 cops",
                             "http://ia.media-imdb.com/images/M/MV5BMTc0NDQzNTA2Ml5BMl5BanBnXkFtZTcwNzI2OTQzMw@@._V1_SX640_SY720_.jpg",
                             "https://www.youtube.com/watch?v=LarFY5tV57s")


inception = media.Movie("Inception",
                        "Extractors perform coorperate espionage by using technology to infiltrate the subconcious of their targets to extract information",
                        "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

interstellar = media.Movie("Interstellar",
                           "Global decline of resources on Earth leads a group of astronauts to search for a new planet to live on. ",
                           "http://ia.media-imdb.com/images/M/MV5BNDYzODY0NDcxNF5BMl5BanBnXkFtZTgwNTAzOTQ3MTE@._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/watch?v=3WzHXI5HizQ")

i_love_you_man = media.Movie("I Love You Man", "A story of a real estate investor whos search for a best man ends in a strong friendship. ",
                           "http://ia.media-imdb.com/images/M/MV5BMTU4MjI5NTEyNV5BMl5BanBnXkFtZTcwNjQ1NTMzMg@@._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/watch?v=kRLf04gH7mc")

#Creates a list of the 6 instances of the movie class that we created above.
movies = [anchorman, i_love_you_man, the_other_guys, inception, interstellar, pineapple_express ]
#call the function open_movies_page(movies) in the fresh_tomatoes.py file which generates the html file with the information above.
fresh_tomatoes.open_movies_page(movies)




