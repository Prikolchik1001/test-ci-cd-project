from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from models import create_db_and_tables, Recipe, SessionDep
from CRUD import get_all_recipes, search_recipe, add_recipe


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/recipes")
async def recipes(session: SessionDep):
    response = await get_all_recipes(session)
    return response


@app.get("/recipe/{recipes_id}")
async def id_recipes(recipes_id: int, session: SessionDep):
    response = await search_recipe(recipes_id, session)
    return response


@app.post("/recipe")
async def add_recipes(item: Recipe, session: SessionDep):
    response = await add_recipe(item, session)
    return response


if __name__ == "__main__":
    uvicorn.run(app)
