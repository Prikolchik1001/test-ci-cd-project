import json
from typing import Dict, List

from sqlalchemy.future import select
from fastapi.exceptions import HTTPException
from models import Recipe


async def add_recipe(item, session) -> Dict:
    recipe = Recipe(
        name=item.name,
        cooking_time=item.cooking_time,
        ingredients=item.ingredients,
        description=item.description,
    )

    session.add(recipe)
    session.commit()
    session.refresh(recipe)

    return {
        "name": recipe.name,
        "cooking_time": recipe.cooking_time,
        "ingredients": recipe.ingredients,
        "description": recipe.description
    }


async def search_recipe(id_recipe: int, session) -> Dict:
    result = session.get(Recipe, id_recipe)
    if not result:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return {
        "id": result.id,
        "name": result.name,
        "cooking_time": result.cooking_time,
        "count_viewing": result.count_viewing,
        "ingredients": result.ingredients,
        "description": result.description,
    }


async def get_all_recipes(session) -> List[dict]:
    recipes = session.exec(
        select(Recipe).order_by(Recipe.count_viewing.desc())
    ).scalars().all()
    return [
        {
            "id": recipe.id,
            "name": recipe.name,
            "cooking_time": recipe.cooking_time,
            "count_viewing": recipe.count_viewing,
            "ingredients": recipe.ingredients,
            "description": recipe.description,
        }
        for recipe in recipes
    ]
