## 1. Получение нового токена для юзера

### ** _URL:_ http://79.137.204.172/api/user/new-token/

### ** _Метод:_ POST

<hr>

### ** _Пример для отправки запроса (в body - ничего, в заголовках - один ключ, указан ниже):_

```
{
    "key": "Authorization",
    "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZXhwIjoxNzA2MjE5MjMyfQ.yMy6RiCFvhitLZ0IavmQS4P_O1-ksLQgaA8JsB3LLl0"
}
```

### ** _Объяснение значений запроса:_

| ключ                       | что это такое                                                     |
|----------------------------|-------------------------------------------------------------------|
| Authorization              | Название заголовка                                                |
| Bearer eyJhbGciOiJIUzI1... | Обязательно слово "Bearer" и через пробел действующий токен юзера |

<hr>

### ** _Пример ответа сервера (JSON):_

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZXhwIjoxNzA2MjE5MjU2fQ.aEAyGLGb_MilvtytmDQ4jrTV833Wd9bRHnW1JsTsI8g"
}
```

### ** _Объяснение значений ответа:_

| ключ  | что это такое                            |
|-------|------------------------------------------|
| token | Токен (пока что, срок действия - 1 день) |

<hr>

### ** _Статус ответа (при успехе):_ 200
