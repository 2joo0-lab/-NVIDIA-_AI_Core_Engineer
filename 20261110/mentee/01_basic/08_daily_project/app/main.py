from fastapi import FastAPI
from app.routers import knowledge

app = FastAPI(title="Knowledge API")
app.include_router(knowledge.router)

@app.get("/health")
def health():
    return {"status": "ok"}