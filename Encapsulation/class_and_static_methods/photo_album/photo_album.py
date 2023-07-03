class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []

    @classmethod
    def from_photos_count(cls, photos_count: int):
        cls()

    def add_photo(self, label: str):
        pass

    def display(self):
        pass


album = PhotoAlbum(2)

print(album.add_photo("baby"))