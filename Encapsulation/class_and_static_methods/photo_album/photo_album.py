import audioop


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count)

    def add_photo(self, label: str):
        if len(self.photos) < 4:
            self.photos.append(label)
            return f'{label} photo added successfully on page  slot '
        return 'No more free slots'


    def display(self):
        pass


a = PhotoAlbum(4)
print(a.photos)

# album = PhotoAlbum(2)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.display())
