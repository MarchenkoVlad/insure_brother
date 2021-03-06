# Приложение Insure_brother "Застрахуй братуху"

## Общий функционал
Это биржа продажи услуг страховых компаний.
Предполагается два типа пользователей - страховые компании которые могут конфигурировать и размещать свои услуги,
и покупатели - люди которые хотят что-либо застраховать.
У страховых компаний есть личный кабинет, где они могут конфигурировать свои продукты - указывать процентные ставки, сроки, категории(недвижимость, авто, жизнь),
а также просматривать данные по откликам на их продукты.
У покупателей(не авторизованные пользователи) есть страницы с услугами всех компаний и всевозможными фильтрами по ним.
У покупателей есть возможность откликнуться на предложение страховой комании указав свою контактную информацию(имя и контактные данные)

## Основные технологии
* Python
* Django
* Docker Compose
* Celery
* Redis

## Запуск приложения

```docker-compose up -d```

```docker-compose run web python manage.py search_index --rebuild```

Команды для запуска без докера:

создание окружения и установка зависимостей:

```virtualenv --python=python3 env```

```source env/bin/activate```

```pip3 install -r requirements.txt```

```export $(xargs <.env)```
```python manage.py runserver ```
