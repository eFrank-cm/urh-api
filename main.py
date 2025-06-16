from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel, AfterValidator
from typing import Annotated
import random

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'
    
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

    
def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id
    
app = FastAPI()

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if (model_name is ModelName.alexnet):
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if (model_name.value == "lenet"):
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/items/{item_id}")
async def read_items(item_id, skip: str, long: bool = False):
    item = {"item_id": item_id, "skip": skip}
    if long: 
        item.update({"description": "This is an amazing item that has a long description"})
    return item


@app.get("/items/")
async def read_items(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
    

@app.post("/items/")
async def create_item(item: Item):
    s = item.name + item.price
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump(), "tax": 'Nuevo tax'}