import pickle
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass:int):
    if Sex != 0 and Sex != 1:
        json_encoded = jsonable_encoder({'status':400, 'message':'Sex must be 0 or 1!'})
        return JSONResponse(content=json_encoded)
    elif Pclass != 1 and Pclass != 3:
        json_encoded = jsonable_encoder({'status':400, 'message':'Pclass must be 1 or 3!'})
        return JSONResponse(content=json_encoded)
    elif Age < 0 and Age > 125:
        json_encoded = jsonable_encoder({'status':400, 'message':'Age must be a postive value!'})
        return JSONResponse(content=json_encoded)

    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
        result = titanic.predict([[Sex, Age, Lifeboat, Pclass]])
        survived=True if result[0] == 1 else False
        json_encoded = jsonable_encoder({'survived':survived, 'status':200, 'message':'SUCCESS'})
        return JSONResponse(content=json_encoded)


@app.get('/model')
def get():
    return {'hello':'test'}
