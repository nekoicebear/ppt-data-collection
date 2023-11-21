from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#
# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}

#app 객체에 include_router 메서드를 사용해 quesiton_router.py 파일의
#router 객체를 등록했다.
app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)