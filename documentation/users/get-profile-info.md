## 1. Получение данных профиля юзера

### ** _URL:_ http://79.137.204.172/api/user/get-profile-info/

### ** _Метод:_ GET

<hr>

### ** _Пример для отправки запроса (headers):_

```json
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZXhwIjoxNzA2MjE5MjMyfQ.yMy6RiCFvhitLZ0IavmQS4P_O1-ksLQgaA8JsB3LLl0"
}
```

### ** _Объяснение значений запроса:_

| ключ          | что это такое        |
|---------------|----------------------|
| Authorization | Bearer (токен юзера) |

<hr>

### ** _Пример ответа сервера (JSON):_

```json
{
    "photo": "http://79.137.204.172/static/profile_photos/default_user_profile_photo.png"
    "email": "test1@test.ru"
}
```

### ** _Объяснение значений ответа:_

| ключ  | что это такое               |
|-------|-----------------------------|
| photo | Фото профиля юзера (ссылка) |
| email | Почта юзера                 |

<hr>

### ** _Статус ответа (при успехе):_ 200
