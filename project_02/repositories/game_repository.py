from bson import ObjectId

class GameRepository:
    def __init__(self, db):
        self.collection = db.games

    async def get_all(self):
        games = []

        async for game in self.collection.find():
            games.append(game)
        return games

    async def get_by_id(self, game_id: str):
        return await self.collection.find_one(
            {"_id": ObjectId(game_id)}
        )

    async def create(self, data: dict):
        result = await self.collection.insert_one(data)

        return await self.collection.find_one(
            {"_id": result.inserted_id}
        )

    async def update(self, game_id: str, update_data: dict):
        return await self.collection.update_one(
            {"_id": ObjectId(game_id)},
            {'$set': update_data}
        )

    async def delete(self, game_id: str):
        return await self.collection.delete_one(
            {"_id": ObjectId(game_id)}
        )
