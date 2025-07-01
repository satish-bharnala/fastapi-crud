from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Dict

app=FastAPI()

fake_db: Dict[int,dict]={}

class Item(BaseModel):
    name:str=Field(...,min_length=4,max_length=50)
    price:float=Field(...,gt=0)
    quantity:int=Field(...,ge=1)

#Create Item(Post)

@app.post("/items/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in fake_db:
        raise HTTPException(status_code=400,detail="item already exists")
    fake_db[item_id]=item.model_dump()
    return{"Message":"Item Added","Item":fake_db[item_id]}

#Get single item

@app.get("/items/{item_id}")
def get_item(item_id:int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404,detail="Item Not found")
    return fake_db[item_id]

# Get all items

@app.get('/')
def all_items():
    return fake_db


#Update item

@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404,detail="Item Not found")
    fake_db[item_id]=item.model_dump()
    return{"Message":"Item Updated","item":fake_db[item_id]}

#Delete Item

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404,detail="Item Not Found")
    deleted_item=fake_db.pop(item_id)
    return{"Message":"Item Deleted","Item":deleted_item}


