## 1. Переименование папки

### ** _URL:_ http://79.137.204.172/api/storage/rename-folder/

### ** _Метод:_ PUT

<hr>

### ** _Пример для отправки запроса:_

#### 1. body (JSON)

```json
{
    "id": 48,
    "name": "test_1222"
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
| id            | id папки             |
| name          | новое имя папки      |

<hr>

### ** _Пример ответа сервера:_

```json
{
    "id": 48,
    "name": "test_1222",
    "star": false,
    "created_at": "2024-02-18 10:04",
    "updated_at": "2024-02-18 10:04"
}
```

### ** _Объяснение значений ответа:_

| ключ       | что это такое                    |
|------------|----------------------------------|
| id         | id папки                         |
| name       | имя папки                        |
| star       | true, если папка в избранных     |
| created_at | время создания папки             |
| updated_at | время последнего изменения папки |

<hr>

### ** _Статус ответа (при успехе):_ 200
