from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.product_router import router as product_router
from routers.book_router import router as book_router
from routers.game_router import router as game_router

app = FastAPI(
    title="Inventory API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(product_router)
app.include_router(book_router)
app.include_router(game_router)

@app.get('/')
async def root():
    return {
        "message": "MongoDB FastAPI Async API"
    }