import requests
import os
from database.question_service import checker_question_id_db, add_question_to_db

# def scraper(count: int) -> dict:
#     os.system('cls')
#     url = f'https://jservice.io/api/random?count={count}'
#     response = requests.get(url)
#     data = response.json()
#     return check_how_data(data, count)
#
#
# def check_how_data(data, count):
#     counter = 0
#     for i in data:
#
#         ids = int(i['id'])
#         is_exists = checker_question_id_db(ids)
#
#         if not is_exists:
#             counter += 1
#             add_question_to_db(ids, i['question'], i['answer'], i['created_at'])
#
#     if counter != count:
#         # Сколько вопросов нужно до генерировать
#         data_checker = count - counter
#         scraper(data_checker)
#     else:
#         return {'status': 'passcheck'}


import httpx


async def scraper(count: int) -> dict:
    url = f'https://jservice.io/api/random?count={count}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    data = response.json()
    return await check_how_data(data, count)


async def check_how_data(data, count):
    counter = 0
    for i in data:
        ids = int(i['id'])
        is_exists = checker_question_id_db(ids)
        if not is_exists:
            counter += 1
            add_question_to_db(ids, i['question'], i['answer'], i['created_at'])
    if counter != count:
        data_checker = count - counter
        await scraper(data_checker)
    else:
        return {'status': 'passcheck'}
п