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
        ordered_collection = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        if not self.movies_collection:
            return 'No movies found.'

        return "\n".join([str(m.details()) for m in ordered_collection])

    def __str__(self):
        res = []

        if not self.users_collection:
            res.append('All users: No users.')
        else:
            res.append(f'All users: {", ".join(u.username for u in self.users_collection)}')

        if not self.movies_collection:
            res.append('All movies: No movies.')
        else:
            res.append(f'All movies: {", ".join(m.title for m in self.movies_collection)}')

        return "\n".join(i for i in res)