class Movie:
    watched = False
    __watched_movies = 0
    past_movies = []

    def __init__(self, name, director):
        self.name = name
        self.director = director

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director):
        self.director = new_director

    def watch(self):
        if self.name not in Movie.past_movies:
            Movie.past_movies.append(self.name)
            Movie.__watched_movies += 1
        Movie.watched = True

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
