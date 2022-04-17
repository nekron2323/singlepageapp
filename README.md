# singlepageapp
### Таблица в формате Single Page Application.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/nekron2323/singlepageapp.git
```
```
cd singlepageapp/
```
### Для запуска серверной части:
Создать виртуальное окружение и активировать его:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
Необходимо создать файл переменных среды .env:
  DB_HOST - адрес на котором расположена база MySQL
  DB_NAME - название базы данных
  USER - имя пользователя БД
  PASSWORD - пароль
  TABLE_NAME - название таблицы
  
Запускаем сервер
```
python server/app.py
```

### Для запуска пользовательского интерфейса:
Открываем новое окно терминала и переходим в директорию с проектом
Переходим в директорию /client
```
cd client
```
Устанавливаем зависимости:
```
npm install
```
Собираем проект:
```
npm run build
```
Запускаем пользовательский интерфейс:
```
npm run dev
```

### Для запуска приложения переходим по адресу http://localhost:8080
