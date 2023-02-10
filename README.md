# api_final
## **Описание проекта api_final_yatube**

Проект предназначен для публикации зарегистрироаванными пользователями постов различной тематики, комментариев к ним. Зарегистрированным пользователям предоставляется возможность подписки на публикации отдельных авторов. Всем пользователям доступно чтение постов и комментариев в ним.
Проект представляет доступ к своей функциональности через API, что расширяет применение проекта как для десктопных так и для мобильных приложений.


## **Как запустить проект:**
### 1. Клонировать репозиторий и перейти в него в командной строке:

```
    git clone https://github.com/dnevvs/api_final_yatube.git
    cd api_final_yatube
```

### 2. Cоздать и активировать виртуальное окружение:

```
    python -m venv venv
    source venv/bin/activate
```

### 3. Установить зависимости из файла requirements.txt:

```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install djoser djangorestframework-simplejwt==4.7.2
    pip install pillow
    python -m pip install --upgrade Pillow
    pip install sorl-thumbnail
<<<<<<< HEAD
    pip install django-filter
=======
>>>>>>> d44c210e6188c9379e4bd2ef3ad4166982ce2fda
```

### 4. Выполнить миграции:

```
    python manage.py migrate
```

### 5. Запустить проект:

```
    python manage.py runserver
```

## **Примеры запросов к API:**

**GET _http://127.0.0.1:8000/api/v1/posts/_**

**Пример ответа: _200_**
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

**POST _http://127.0.0.1:8000/api/v1/posts/_**
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
**Пример ответа: _200 (или 400, 401)_**
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

**GET _http://127.0.0.1:8000/api/v1/posts/{id}/_**

**Пример ответа: _200 (или 404)_**
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

**PUT _http://127.0.0.1:8000/api/v1/posts/{id}/_**
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
**Пример ответа: _200 (или 400, 401, 403, 404)_**
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

**PATCH _http://127.0.0.1:8000/api/v1/posts/{id}/_**
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
**Пример ответа: _200 (или 401, 403, 404)_**
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

**DESTROY _http://127.0.0.1:8000/api/v1/posts/{id}/_**

**Пример ответа: _401 (или 204, 403, 404)_**
```
{
  "detail": "Учетные данные не были предоставлены."
}
```

**GET _http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/_**

Пример ответа: 200 (или 404)
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

**POST _http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/_**
```
{
  "text": "string"
}
```
**Пример ответа: _201 (или 400, 401, 404)_**
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

**GET _http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/_**

**Пример ответа: _200 (или 404)_**
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

**PUT _http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/_**
```
{
  "text": "string"
}
```
**Пример ответа: _200 (или 400, 401, 403, 404)_**
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

**PATCH _http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/_**
```
{
  "text": "string"
}
```
**Пример ответа: _200 (или 401, 403, 404)_**
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

**DESTROY _http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/_**

**Пример ответа: _401 (или 204, 403, 404)_**
```
{
  "detail": "Учетные данные не были предоставлены."
}
```

**GET _http://127.0.0.1:8000/api/v1/groups/_**

**Пример ответа: _200 (или 404)_**
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

**GET _http://127.0.0.1:8000/api/v1/groups/{id}/_**

**Пример ответа: _200 (или 404)_**
```
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```

**GET _http://127.0.0.1:8000/api/v1/follow/_**

**Пример ответа: _200 (или 401)_**
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```

**POST _http://127.0.0.1:8000/api/v1/follow/_**
```
{
  "following": "string"
}
```
**Пример ответа: _201 (или 400, 401)_**
```
{
  "user": "string",
  "following": "string"
}
```

**POST _http://127.0.0.1:8000/api/v1/jwt/create/_**
```
{
  "username": "string",
  "password": "string"
}
```
**Пример ответа: _200 (или 400, 401)_**
```
{
  "refresh": "string",
  "access": "string"
}
```

**POST _http://127.0.0.1:8000/api/v1/jwt/refresh/_**
```
{
  "refresh": "string"
}
```
**Пример ответа: _200 (или 400, 401)_**
```
{
  "access": "string"
}
```

**POST _http://127.0.0.1:8000/api/v1/jwt/verify/_**
```
{
  "token": "string"
}
```
**Пример ответа: _400 (или 200, 401)_**
```
{
  "token": [
    "Обязательное поле."
  ]
}
```
