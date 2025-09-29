from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Dockerized FastAPI Example", version="0.1.0")

# simple in-memory store for demonstration purposes
ITEMS: Dict[int, str] = {
    1: "First item",
    2: "Second item",
}


class Item(BaseModel):
    name: str


@app.get("/")
async def read_root() -> Dict[str, str]:
    return {"message": "Welcome to the Dockerized FastAPI"}


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> Dict[str, str]:
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": str(item_id), "name": ITEMS[item_id]}


@app.post("/items", status_code=201)
async def create_item(item: Item) -> Dict[str, str]:
    next_id = max(ITEMS.keys(), default=0) + 1
    ITEMS[next_id] = item.name
    return {"item_id": next_id, "name": item.name}


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int) -> None:
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    del ITEMS[item_id]
    return None


@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "ok"}
