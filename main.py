from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Our enchanted items
class MagicalItem(BaseModel):
    name: str
    description: str
    price: float

# Sample data from the wizarding world
mock_items = [
    MagicalItem(name="Elder Wand", description="The most powerful wand ever", price=1000.00),
    MagicalItem(name="Invisibility Cloak", description="Hides you from sight", price=500.00),
    MagicalItem(name="Philosopher's Stone", description="Grants immortality", price=10000.00),
    MagicalItem(name="Marauder's Map", description="Shows you everyone's location in Hogwarts", price=250.00),
    MagicalItem(name="Firebolt", description="The fastest broomstick around", price=750.00),
]

@app.get("/items/")
async def get_magical_items():
    return mock_items

# @app.get("/items/{item_id}")
# async def get_magical_item(item_id: int):
#     if item_id < 0 or item_id >= len(mock_items):
#         return {"error": "Item not found"}
#     return mock_items[item_id]

@app.get("/items/{item_name}")
async def get_magical_item(item_name: str):
    for item in mock_items:
        if item.name.lower() == item_name.lower():
            return item
    return {"error": "Item not found"}

@app.get("/items/{item_name}/price")
async def get_magical_item_price(item_name: str):
    for item in mock_items:
        if item.name.lower() == item_name.lower():
            return {"price": item.price}
    return {"error": "Item not found"}
