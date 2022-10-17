
Файл - .env

<b>TOKEN</b> = "8234987234:SOMETHING"

<b>API_URL</b>  = "https://api.telegram.org/bot"

<b>CHAT_ID</b> = "@some_channel"

<b>BASE_URL</b> = "https://localhost:8000"




<h1>Запуск сервера</h1>

Для запуска сервера используется Ngrok для создания тунеля. Однако на хостинге это может не потребоваться, так что нужно будет удалить ngrok конфигурацию внутри <b>application/appcore</b>
Также в скрипте Python запускается shell команда curl(Почему-то таким образом телеграму все передается нормально)


Команда для запуска сервера:
<b>USE_NGROK=True uvicorn run:app --reload</b>


