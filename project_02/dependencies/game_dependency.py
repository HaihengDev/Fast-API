from fastapi import Depends

from core.database import get_db
from repositories.game_repository import GameRepository
from services.game_service import GameService

def get_game_dependency(db=Depends(get_db)):
    return GameRepository(db)

def get_game_service(
    repository: GameRepository = Depends(get_game_dependency)
):
    return GameService(repository)