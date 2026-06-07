class Product:
    @staticmethod
    def to_dict(product):
        return {
            "id": str(product["_id"]),
            "name": product["name"],
            "stock": product["stock"],
            "price": product['price']
        }