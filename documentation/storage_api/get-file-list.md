## 1. Получение корневой директории юзера

### ** _URL:_ http://79.137.204.172/api/storage/get-file-list/

### ** _Метод:_ GET

<hr>

### ** _Пример для отправки запроса:_

#### 1. headers (содержит токен юзера)

```json
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZXhwIjoxNzA2MjE5MjMyfQ.yMy6RiCFvhitLZ0IavmQS4P_O1-ksLQgaA8JsB3LLl0"
}
```

#### 2. body (JSON)

```json
{
    "folder_id": 1
}
```

### ** _Объяснение значений запроса:_

| ключ          | что это такое        |
|---------------|----------------------|
| Authorization | Bearer (токен юзера) |

<hr>

### ** _Пример ответа сервера (JSON, список файлов):_

```json
[
    {
        "id": 1,
        "name": "file1.txt",
        "size": 494,
        "star": false,
        "created_at": "2024-02-05 21:48"
    },
    {
        "id": 2,
        "name": "monkey_high_resolution.jpg",
        "size": 43594,
        "star": false,
        "created_at": "2024-02-05 21:51"
    }
]
```

### ** _Объяснение значений ответа:_

| ключ       | что это такое               |
|------------|-----------------------------|
| id         | Уникальный id файла         |
| name       | Имя файла                   |
| size       | Размер файла в байтах       |
| star       | true, если файл в избранных |
| created_at | дата и время создания файла |

<hr>

### ** _Статус ответа (при успехе):_ 200
