class Book:
    @staticmethod
    def to_dict(book):
        return {
            "id": str(book["_id"]),
            "title": book['title'],
            'author': book['authro'],
            'release_date': book['release_date']
        }