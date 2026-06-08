from bson import ObjectId
from fastapi import HTTPException

from repositories.game_repository import GameRepository

class GameService:
    def __init__(self, repository: GameRepository):
        self.repository = repository

    async def get_games(self):
        return await self.repository.get_all()

    async def get_game_by_id(self, game_id: str):
        if not ObjectId.is_valid(game_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid game id"
            )
        game = await self.repository.get_by_id(game_id)

        if not game:
            raise HTTPException(
                status_code=404,
                detail="Game not found"
            )
        return game

    async def create_game(self, data:dict):
        return await self.repository.create(data)

    async def update_game(self, game_id: str, update_data: dict):
        if not ObjectId(game_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid game id"
            )
        result = await self.repository.update(game_id, update_data)

        if result.matched_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Game not found"
            )
        return await self.repository.get_by_id(game_id)

    async def delete_game(self, game_id: str):
        if not ObjectId(game_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid game id"
            )
        result = await self.repository.delete(game_id)

        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Game not found"
            )
        return {
            "message": "Game deleted successfully"
        }