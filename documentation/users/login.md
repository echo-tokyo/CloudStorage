## 1. Вход существующего юзера

### ** _URL:_ http://79.137.204.172/api/user/login/

### ** _Метод:_ POST

<hr>

### ** _Пример для отправки запроса (body, JSON):_

```json
{
    "email": "test9@test.ru",
    "password": "qwerty123"
}
```

### ** _Объяснение значений запроса:_

| ключ     | что это такое                         |
|----------|---------------------------------------|
| email    | Почта, которую вводит юзер для входа  |
| password | Пароль, который вводит юзер для входа |

<hr>

### ** _Пример ответа сервера (JSON):_

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTAsImV4cCI6MTcwOTA1OTk4OH0.xt2SZsi1CGMtdraR8ovC_6oA4hYIL16-MS3EJ6-3s6Q", 
}
```

### ** _Объяснение значений ответа:_

| ключ     | что это такое                |
|----------|------------------------------|
| token    | Токен для юзера              |

<hr>

### ** _Статус ответа (при успехе):_ 200