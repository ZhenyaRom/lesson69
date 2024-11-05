from fastapi import FastAPI

app = FastAPI()


@app.get('/id')
async def id_page(username: str, age: int) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get('/user/admin')
async def welcome_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def welcome(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/')
async def main_page() -> dict:
    return {'message': 'Главная страница'}

