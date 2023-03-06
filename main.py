from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles


from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router

# import models

# from database import ENGINE
# models.Base.metadata.create_all(bind=ENGINE)


app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#     return {"message":"한글!!"}

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
app.mount("/build", StaticFiles(directory="frontend/public/build"))

@app.get("/")
def index():
    return FileResponse("frontend/public/index.html")