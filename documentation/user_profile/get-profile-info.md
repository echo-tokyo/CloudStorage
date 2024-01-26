## 1. Получение информации профиля юзера

### ** _URL:_ http://79.137.204.172/api/user_profile/get/

### ** _Метод:_ GET

<hr>

### ** _Пример для отправки запроса (в body - ничего, в заголовках - один ключ, указан ниже):_

```
{
    "key": "Authorization",
    "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZXhwIjoxNzA2MjE5MjMyfQ.yMy6RiCFvhitLZ0IavmQS4P_O1-ksLQgaA8JsB3LLl0"
}
```

#### (пример из postman):

![Postman](./img/postman_get_user_profile.png)

### ** _Объяснение значений запроса:_

| ключ                       | что это такое                                                     |
|----------------------------|-------------------------------------------------------------------|
| Authorization              | Название заголовка                                                |
| Bearer eyJhbGciOiJIUzI1... | Обязательно слово "Bearer" и через пробел действующий токен юзера |

<hr>

### ** _Пример ответа сервера (JSON):_

```json
{
    "id": 5,
    "nickname": "User_000005",
    "photo": "/media/profile_photos/default_user_profile_photo.png"
}
```

### ** _Объяснение значений ответа:_

| ключ     | что это такое                                  |
|----------|------------------------------------------------|
| id       | Уникальный идентификатор юзера                 |
| nickname | Ник юзера                                      |
| photo    | Фото профиля юзера (ссылка, пока не настроена) |

<hr>

### ** _Статус ответа (при успехе):_ 200
