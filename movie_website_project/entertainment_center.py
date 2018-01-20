import media
import fresh_tomatoes
# the mutiple movies listed below act as the info storage that will
# eventually bepulled by the frest_tomatoes program
toy_story = media.Movie(
    "Toy Story",
    "A story about a boy who plays with his toys",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "An American marine in an unknown world",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")


xmen = media.Movie(
    "X-Men Days of future past",
    "The Wolverine goes back in time to save the world",
    "https://goo.gl/UDmJcu",
    "https://www.youtube.com/watch?v=pK2zYHWDZKo")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat joins a human to cook in paris",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

avengers = media.Movie(
    "The Avengers",
    "All the best superheroes come together to save the world",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

spiderman = media.Movie(
    "The Amazing Spiderman",
    "Peter Parker and his jouney of becoming a hero",
    "https://goo.gl/ghy74W",
    "https://www.youtube.com/watch?v=FpKPiHYJc54")
# the array below takes the 6 movies above and is used
# to create an argument that can be run in the
# open_movies_page function
movies = [toy_story, avatar, xmen, ratatouille, avengers, spiderman]
fresh_tomatoes.open_movies_page(movies)
