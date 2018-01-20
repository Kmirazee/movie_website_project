import webbrowser
# this is a class that I created, it acts as a
# blueprint in that other functions
# and modules and even programs can use


class Movie():
    def __init__(
         self, movie_title, movie_storyline, poster_image, trailer_youtube):
        ''' This function inside of the class movie will be
        used to instantiate information such as the title,
        storyline, poster and trailer'''
        self.title = movie_title
        self.storyline = movie_storyline

        self.poster_image_url = poster_image

        self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            '''This function is written in order to open a browswer
            and follow the link provided previously'''
            webbrowser.open(self.trailer_youtube_url)
