from fastapi import FastAPI
from service import scraper
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')


@app.post("/")
async def get_any_questions(questions_num: int = 1):
    return scraper(questions_num)

