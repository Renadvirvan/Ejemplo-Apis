from fastapi import APIRouter # Redirecciona a las diferentes rutas las
from config.db import conect
from schemas.user import userEntity, usersEntity
from models.user import User
from bson import ObjectId
from passlib.hash import sha256_crypt
user = APIRouter() # Aquí estrán todas las rutas de los usuarios
# El arroba ya lo hace un decorador 
# El "get" es un método abstracto
@user.get('/getUsers', tags=['users']) 
def getUsers():
    return usersEntity(conect.local.test.find())

# Línea 15 PENDIENTE
@user.get('/getUser', tags = ["users"])
def getUser(id:str):
    return userEntity(conect.local.test.find_one({"_id":ObjectId(id)}))

@user.get('/gerita', tags = ["gerita"]) 
def gerita(): 
    return "Malvao"

@user.post("/crearUruario", tags = ["users"])
def crearUsuario(usuario:User): 
    newUsuario = dict(usuario)
    del newUsuario["userID"]
    newUsuario["password"]=sha256_crypt.encrypt(newUsuario["password"]) # Encriptando la Contraseña
    return str(conect.local.test.insert_one(newUsuario).inserted_id)
    
@user.put("/actualizarUser", tags = ["users"])
def actualizarUser(actualizando:User,id:str):
    actUser = dict(actualizando)
    actUser["password"]=sha256_crypt.encrypt(actUser["password"]) # Encriptando la Contraseña
    conect.local.test.find_one_and_update({"_id":ObjectId(id)},{"$set":actUser})
    return userEntity(conect.local.test.find_one({"_id":ObjectId(id)}))

@user.delete("/borrarUser", tags = ["users"])
def borrarUser(borrarID:str):
    conect.local.test.find_one_and_delete({"_id":ObjectId(borrarID)})
    return "Ok lo borre"