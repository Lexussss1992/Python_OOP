from functools import wraps


def logged(function):
    def wrapper(*args):
        return 3 + len(args)

    return wrapper


print(print(func(4, 4, 4)))

# @logged
# def func(*args):
#     return 3 + len(args)


# print(func(4, 4, 4))