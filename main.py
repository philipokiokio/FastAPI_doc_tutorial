from enum import Enum
from fastapi import FastAPI
from typing import Optional




class ModelName(str,Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'




app = FastAPI()
fake_items_db = [{'item_name':'Foo'},{'item_name':'Bar'}, {'item_name':'Baz'}]
# query
@app.get('/items/')
async def read_item(skip:int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]



@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}





@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name,
                "message":"Deep Learning FTW!"}

    if model_name == ModelName.lenet:
        return {"model_name": model_name,
                "message":"LeCNN all the images!"}

    return {"model_name": model_name,
                "message":"Have somes residuals"}










@app.get("/")
async def root():
    return {
        'Expression': 'Hello World'
    }


@app.get("/users/me")
async def read_user_me():
    return {
        "user_id": "The current user"
    }

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {
        "user_id": user_id
    }

# query

@app.get('/items/{item_id}')
async def read_item(item_id: str, q: Optional[str]= None, short :bool =False):
    item = {"item_id": item_id}

    if q:
        item.update({ 'q':q})
    if not short:
        item.update({'description': 'this is an amazing item that has a long description'})
    return item