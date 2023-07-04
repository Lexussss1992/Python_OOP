from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)

                return f'{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}'
        return 'No more free slots'

    def display(self):
        res = ['-' * 11]

        for page in self.photos:
            res.append(('[] ' * len(page)).rsplit())
            res.append('-' * 11)

        return '\n'.join(res)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
