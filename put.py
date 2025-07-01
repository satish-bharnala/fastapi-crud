from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field

app=FastAPI()

fake_db={

    1:{"name":"Silver","price":50000},
    2:{"name":"Gold","price":100000}

}

# class Item(BaseModel):
#     name:str=Field(...,min_length=3)
#     price:int=Field(...,gt=0)

# --- PUT ---
# @app.put("/items/{item_id}")
# def update_item(item_id:int,updated_item:Item):
#     if item_id not in fake_db:
#         raise HTTPException(status_code=404,detail="item not found")
#     fake_db[item_id]=updated_item.model_dump()
#     return{"messege":"Item updated","Item":fake_db[item_id]}

#--- Delete ---
@app.delete("/items/{item_id}")
def del_item(item_id:int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404,detail="item not found")
    deleted_item=fake_db.pop(item_id)
    return{"message":"Item Deleted","Item":deleted_item}