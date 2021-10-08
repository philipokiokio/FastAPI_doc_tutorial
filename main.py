from enum import Enum
from fastapi import FastAPI,Path,Query
from typing import Optional,List
from pydantic import BaseModel




class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None




class ModelName(str,Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'




app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *,q:str,item_id: int = Path(..., title='The ID of the item to get'),
    size : float =Query(..., gt=0,lt=10.5)
    ):

    results = {'item_id':item_id,'size':size}

    if q: 
        results.update({'q':q})
    
    return results










# request body









@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({
            'price_with_tax': price_with_tax
        })

    return item_dict

@app.put('/item/{item_id}')
async def create_item(item_id: int,item:Item, q: Optional[str] = None):
    result = {'item_id':item_id, **item.dict()}
    if q:
        result.update({'q':q})
    return result

# querry parameters and string validation 
@app.get('/items/')
async def read_items(q: Optional[List[str]]= Query('fixedquery', min_length=3,max_length = 50)):
    results = {"items": [{"item_id":'FOO'},{"item_id":'BAR'}]}
    if q:
        results.update({'q':q})
    return results



# fake_items_db = [{'item_name':'Foo'},{'item_name':'Bar'}, {'item_name':'Baz'}]
# # query
# @app.get('/items/')
# async def read_item(skip:int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]



# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}





# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name,
#                 "message":"Deep Learning FTW!"}

#     if model_name == ModelName.lenet:
#         return {"model_name": model_name,
#                 "message":"LeCNN all the images!"}

#     return {"model_name": model_name,
#                 "message":"Have somes residuals"}










# @app.get("/")
# async def root():
#     return {
#         'Expression': 'Hello World'
#     }


# @app.get("/users/me")
# async def read_user_me():
#     return {
#         "user_id": "The current user"
#     }

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {
#         "user_id": user_id
#     }

# # query

# @app.get('/items/{item_id}')
# async def read_item(item_id: str, q: Optional[str]= None, short :bool =False):
#     item = {"item_id": item_id}

#     if q:
#         item.update({ 'q':q})
#     if not short:
#         item.update({'description': 'this is an amazing item that has a long description'})
#     return item