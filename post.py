from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional
app=FastAPI()

# class Item(BaseModel):
#     name:str
#     price:float
#     quantity:int
# class ItemRespond(BaseModel):
#     name:str  

# @app.post("/items/",response_model=ItemRespond)
# def create_item(item:Item):
#     return item

# --- Validation ---
class Item(BaseModel):
    name:str=Field(...,min_length=4,max_length=40)
    price:float=Field(...,gt=0)

@app.post("/products/")
def create_product(product:Item):
    return product