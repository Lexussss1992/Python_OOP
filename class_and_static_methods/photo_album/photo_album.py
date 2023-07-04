from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)

                return f'{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}'
        return 'No more free slots'

    def display(self) -> str:
        res = ['-' * 11]

        for page in self.photos:
            res.append(('[] ' * len(page)))
            res.append('-' * 11)

        return "\n".join(res)


album = PhotoAlbum(1)
album.add_photo("baby")
album.add_photo("first grade")
album.add_photo("eight grade")
album.add_photo("party with friends")
result = album.display().strip()
print(result)