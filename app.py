from fastapi import FastAPI
from routes.user import user
from docs.docs import tags_metadata
app = FastAPI(
    title = "Ejemplo de una Api",
    description = "Aprendiendo hacer Apis (Parece un laberinto)",
    version = "1.0.1.0",
    openapi_tags= tags_metadata
)

app.include_router(user) # include router está importando todas las librerías que esten en el archivo user
