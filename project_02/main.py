from fastapi import FastAPI
from routers.product_router import router as product_router

app = FastAPI(
    title="Inventory API"
)

app.include_router(product_router)

@app.get('/')
async def root():
    return {
        "message": "MongoDB FastAPI Async API"
    }