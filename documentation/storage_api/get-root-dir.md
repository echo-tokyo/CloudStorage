## 1. Получение корневой директории юзера

### ** _URL:_ http://79.137.204.172/api/storage/get-root-dir/

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
    "root_dir": 4
}
```

### ** _Объяснение значений ответа:_

| ключ     | что это такое        |
|----------|----------------------|
| root_dir | Корневая папка юзера |

<hr>

### ** _Статус ответа (при успехе):_ 200
