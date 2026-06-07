from fastapi import FastAPI
from routers.product_router import router as product_router
from routers.book_router import router as book_router

app = FastAPI(
    title="Inventory API"
)

app.include_router(product_router)
app.include_router(book_router)

@app.get('/')
async def root():
    return {
        "message": "MongoDB FastAPI Async API"
    }