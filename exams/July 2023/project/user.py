from typing import List


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List = []
        self.movies_owned: List = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == '':
            raise ValueError('Invalid username!')
        else:
            self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError('Users under the age of 6 are not allowed!')
        else:
            self.__age = value

    def __str__(self):
        details_liked_movies_list = []
        details_owned_movies_list = []

        if len(self.movies_liked) == 0:
            details_liked_movies_list.append('No movies liked.')
        else:
            for m in self.movies_liked:
                details_liked_movies_list.append(m)

        if len(self.movies_owned) == 0:
            details_owned_movies_list.append('No movies owned.')
        else:
            for m in self.movies_owned:
                details_owned_movies_list.append(m)

        return f"Username: {self.username}, Age: {self.age}\n"\
               f"Liked movies:\n"\
               f"{', '.join(i.title for i in details_liked_movies_list)}\n"\
               f"Owned movies:\n"\
               f"{', '.join(i.title for i in details_owned_movies_list)}"
