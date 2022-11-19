class Movie:
    list_of_movies = []
    total_watched = 0

    def __init__(self, name, director, watched=False):
        self.name = name
        self.director = director
        self.watched = watched

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if self.name not in Movie.list_of_movies:
            self.watched = True
            Movie.total_watched += 1
        Movie.list_of_movies.append(self.name)

    def __repr__(self):
        return f'Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.total_watched}'