from project.movie_specification.action import Action
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        user = User(username, age)

        try:
            next(filter(lambda u: u.username == username, self.users_collection))
            return Exception('User already exists!')
        except StopIteration:
            self.users_collection.append(user)
            return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):

        try:
            next(filter(lambda u: u.username == username, self.users_collection))
        except StopIteration:
            raise Exception('This user does not exist!')

        user = next(filter(lambda u: u.username == username, self.users_collection))

        if user:
            if user.username != movie.owner.username:
                raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f'{username} successfully added {movie.title} movie.'


movie_app = MovieApp()
print(movie_app.register_user('Martin', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Martin', movie))
print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))
user2 = movie_app.users_collection[1]
movie2 = Action('Free Guy', 2021, user2, 16)
print(movie_app.upload_movie('Alexandra', movie2))