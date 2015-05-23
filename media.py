import webbrowser


class Movie():

# This is the init function.
# Parameters defined when an instance of this class is created
    def __init__(self, movie_title, movie_storyline, image, youtube):
# Here I create variables title,storyline,poster_image_url,trailer_youtube_url.
# These can be accessed by the movie class.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = image
        self.trailer_youtube_url = youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)








