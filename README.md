🛠 Используемые технологии
Python 3.10+

FastAPI — основной фреймворк для API

Pydantic — модели и валидация данных

Passlib (bcrypt) — для хеширования паролей

python-jose — для работы с JWT

OAuth2PasswordBearer из FastAPI — для аутентификации по OAuth2 с паролем

UUID и datetime — для идентификаторов и времени

Uvicorn — сервер, запускающий приложение

🚀 Как запустить проект локально
Клонируй репозиторий:
git clone https://github.com/Ertannic/PythonBack.git
cd PythonBack
2. Создай и активируй виртуальное окружение
python -m venv venv
source venv/bin/activate  # на Windows: venv\Scripts\activate
3. Установи зависимости
pip install -r requirements.txt
4. Запусти приложение
uvicorn main:app --reload
5. Открой документацию
Swagger UI: http://127.0.0.1:8000/docs

Открой Swagger UI по адресу:
http://127.0.0.1:8000/docs

Зарегистрируйся, выполнив запрос POST /register — укажи username и password. В ответе ты получишь токен.

Нажми кнопку Authorize в правом верхнем углу Swagger UI.
В появившейся форме введи свой username и password — Swagger автоматически выполнит вход и получит токен.

После авторизации можно создавать задачи через запрос POST /tasks, указав название, описание и статус.

Получить задачу можно через запрос GET /tasks/{task_id}, где {task_id} — ID нужной задачи.

Токен, полученный при регистрации (POST /register), можно проверить на сайте jwt.io.

