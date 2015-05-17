import webbrowser


class Movie():

#This is the init function with parameters that are defined when an instance of this class is created
    def __init__(self,movie_title, movie_storyline, poster_image,trailer_youtube):
#Here we create the variables title, storyline, poster_image_url,trailer_youtube_url that can be accessed by the instances of the movie class
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)








