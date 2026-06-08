class Game:
    @staticmethod
    def to_dict(game):
        return {
            "id": str(game['_id']),
            'name': game['name'],
            'imgUrl': game['imgUrl'],
            'stock': game['stock'],
            'discount': game['discount'],
            'price': game['price']
        }