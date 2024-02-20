## 1. Очищение корзины (удаление оттуда всех файлов  и папок)

### ** _URL:_ http://79.137.204.172/api/storage/clear-trash/

### ** _Метод:_ DELETE

<hr>

### ** _Пример для отправки запроса:_

#### 1. headers (содержит токен юзера)

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

### ** _Пример ответа сервера (JSON, список объектов файлов и папок):_

```json
{
    "result": "Recycle bin has been cleared"
}
```

### ** _Объяснение значений ответа:_

| ключ       | что это такое                           |
|------------|-----------------------------------------|
| result     | Результат операции                      |

<hr>

### ** _Статус ответа (при успехе):_ 200
