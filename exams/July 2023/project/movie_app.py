from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
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

        if user.username != movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = next(filter(lambda u: u.username == username, self.users_collection))

        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if user.username != movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value

            if key == 'year':
                movie.year = value

            if key == 'age_restriction':
                movie.age_restriction = value

        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))

        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if user.username != movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))

        if user.username == movie.owner.username:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')

        if movie in user.movies_liked:
            raise Exception(f'{username} already liked the movie {movie.title}!')

        movie.likes += 1
        user.movies_liked.append(movie)
        return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))

        if movie not in user.movies_liked:
            raise Exception(f'{username} has not liked the movie {movie.title}!')

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        if not self.movies_collection:
            return 'No movies found.'

        return "\n".join(m.details() for m in self.movies_collection)

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
print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.like_movie('Alexandra', movie))
print(movie_app.dislike_movie('Martin', movie2))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.delete_movie('Alexandra', movie2))
movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.display_movies())