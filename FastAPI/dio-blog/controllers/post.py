from datetime import UTC, datetime
from typing import Annotated
from fastapi import Response, Cookie, FastAPI, status, Header
from schemas.post import PostIn

fake_db = [
    {
        "title": "Criando uma aplicação com Django",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": "Criando uma aplicação com FastAPI",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": "Criando uma aplicação com Flask",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": "Criando uma aplicação com Starlett",
        "date": datetime.now(UTC),
        "published": False,
    },
]


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post


@app.get("/posts/")
def read_posts(
    response: Response,
    published: bool,
    limit: int,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    response.set_cookie(key="user", value="kauawt@gmail.com")
    print(f"Cookie: {ads_id}")
    print(f"User_agent: {user_agent}")
    return [
        post for post in fake_db[skip : skip + limit] if post["published" is published]
    ]


@app.get("/posts/{framework}")
def read_framework_posts(framework: str):
    return {
        "posts": [
            {
                "title": "criando uma aplicação com {framework}",
                "date": datetime.now(UTC),
            },
            {
                "title": "criando uma aplicação com {framework}",
                "date": datetime.now(UTC),
            },
        ]
    }
