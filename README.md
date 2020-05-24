# sketchpad
#### Проект предлагает бэкенд на Django и Django Rest Framework с базой данных и API. Фронтенд на VueJS: при помощи модальных окон можно редактировать базу.

### Запуск приложения
- pip install -r requirements.txt для установки зависимостей
+ python3 manage.py makemigrations - для инициализации модели (эта команда также необходима после обновления модели)
+ python3 manage.py migrate - для фиксации изменений в модели (эта команда также необходима после обновления модели)
+ python3 manage.py runserver - для запуска на localhost:8000. 
+ localhost:8000/events - при помощи VueJS
+ localhost:8000/api/events - через встроенный интерфейс Django Rest Framework

