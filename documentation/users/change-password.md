## 1. Изменение пароля существующего юзера

### ** _URL:_ http://79.137.204.172/api/user/change-password/

### ** _Метод:_ PUT

<hr>

### ** _Пример для отправки запроса (пусть почта: test9@test.com):_

#### 1. body, JSON (содержит новый и старый пароль юзера)

```json
{
    "old_password": "ytrewq321",
    "new_password": "qwerty123"
}
```

#### 2. headers (содержит токен юзера)

```json
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZXhwIjoxNzA2MjE5MjMyfQ.yMy6RiCFvhitLZ0IavmQS4P_O1-ksLQgaA8JsB3LLl0"
}
```

### ** _Объяснение значений запроса:_

| ключ          | что это такое                    |
|---------------|----------------------------------|
| old_password  | Текущий пароль на аккаунте юзера |
| new_password  | Новый пароль для аккаунта юзера  |
| Authorization | Bearer (токен юзера)             |

<hr>

### ** _Пример ответа сервера (JSON):_

```json
{
    "email": "test9@test.ru",
    "result": "Password was changed!"
}
```

### ** _Объяснение значений ответа:_

| ключ   | что это такое              |
|--------|----------------------------|
| email  | Почта юзера                |
| result | Результат изменения пароля |


<hr>

### ** _Статус ответа (при успехе):_ 200
