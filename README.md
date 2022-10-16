
Файл - .env

<b>TOKEN</b> = "8234987234:SOMETHING"

<b>API_URL</b>  = "https://api.telegram.org/bot"

<b>CHAT_ID</b> = "@some_channel"

<b>BASE_URL</b> = "https://localhost:8000"


<h1>Перед запуском</h1>
Перед запуском рекомендую удалить файлы миграции <b>"alembic/versions"</b>.

В файле <b>alembic.ini</b> указать адрес базы данных. Например:
 
<b>sqlalchemy.url = sqlite:///app_database.db</b>

Провести миграцию заново: <b>alembic revision --autogenerate -m "<Название миграции>"</b>


<h1>Запуск сервера</h1>

Для запуска сервера используется Ngrok для создания тунеля. Однако на хостинге это может не потребоваться, так что нужно будет удалить ngrok конфигурацию внутри <b>application/appcore</b>
Также в скрипте Python запускается shell команда curl(Почему-то таким образом телеграму все передается нормально)


Команда для запуска сервера:
<b>USE_NGROK=True uvicorn run:app --reload</b>


