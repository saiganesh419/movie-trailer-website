import webbrowser
# creating movie class


class Movie():
    '''Attributes:
    movie_title (str): Indicates the movie tile name.
    movie_type  (str): Indicates the type of movie.
    poster (str): Url for poster image.
    youtube_url (str): youtube_url link.'''
    def __init__(self, movie_title, movie_type, poster, youtube_url):
        self.title = movie_title
        self.storyline = movie_type
        self.poster_image_url = poster
        self.trailer_youtube_url = youtube_url

# defining for to show youtube tariler
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
