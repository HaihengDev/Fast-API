from fastapi import APIRouter, Depends

from models.book_model import Book
from schemas.game_schema import (
    GameCreate,
    GameUpdate
)
from models.game_model import Game
from services.game_service import GameService
from dependencies.game_dependency import (get_game_service)

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)

@router.get('/')
async def get_games(
    service: GameService = Depends(get_game_service)
):
    games = await service.get_games()

    return [
        Game.to_dict(game)
        for game in games
    ]

@router.get('/{game_id}')
async def get_game_by_id(
    game_id: str,
    service: GameService = Depends(get_game_service)
):
    game = await service.get_game_by_id(game_id)
    return Game.to_dict(game)

@router.post('/')
async def create_game(
    payload: GameCreate,
    service: GameService = Depends(get_game_service)
):
    game = await service.create_game(payload.model_dump())
    return Game.to_dict(game)

@router.put('/{game_id}')
async def update_game(
    game_id: str,
    payload: GameUpdate,
    service: GameService = Depends(get_game_service)
):
    game = await service.update_game(game_id, payload.model_dump(
        exclude_unset=True
    ))
    return Game.to_dict(game)

@router.delete('/{game_id}')
async def delete_game(
    game_id: str,
    service: GameService = Depends(get_game_service)
):
    return await service.delete_game(game_id)