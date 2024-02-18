## 1. Удаление файла

### ** _URL:_ http://79.137.204.172/api/storage/delete-file/

### ** _Метод:_ DELETE

<hr>

### ** _Пример для отправки запроса:_

#### 1. body (JSON)

```json
{
    "id": 50
}
```

#### 2. headers (содержит токен юзера)

```json
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZXhwIjoxNzA2MjE5MjMyfQ.yMy6RiCFvhitLZ0IavmQS4P_O1-ksLQgaA8JsB3LLl0"
}
```

### ** _Объяснение значений запроса:_

| ключ          | что это такое        |
|---------------|----------------------|
| Authorization | Bearer (токен юзера) |
| id            | id файла             |

<hr>

### ** _Пример ответа сервера (ничего):_

```json
```

### ** _Объяснение значений ответа:_

| ключ | что это такое |
|------|---------------|
| нет  | нет           |

<hr>

### ** _Статус ответа (при успехе):_ 200
