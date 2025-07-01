from fastapi import FastAPI
app=FastAPI()

# @app.get('/')
# def index():
#     return {"message":"Hello WOrld!"}

#Path Parameter
@app.get("/hello/{name}")
def say_hello(name:str):
    return {"Greetings":f"Hello,{name}!"}

# Query Parameter
# @app.get("/items/")
# def read_items(id:int,q:str=None):
#     return{"id_num":id,"query":q}

#both parameters
# @app.get("/users/{satish}")
# def user(satish:str,active:bool=True):
#     return{"user_name":satish,
#            "active":active
#         }