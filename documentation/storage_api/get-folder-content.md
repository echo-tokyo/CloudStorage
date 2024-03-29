## 1. Получение списка файлов юзера из определённой папки

### ** _URL:_ http://79.137.204.172/api/storage/get-folder-content/

### ** _Метод:_ POST

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
    "folder_id": 52
}
```

### ** _Объяснение значений запроса:_

| ключ          | что это такое        |
|---------------|----------------------|
| Authorization | Bearer (токен юзера) |
| folder_id     | id папки             |

<hr>

### ** _Пример ответа сервера (JSON, id род. папки, список объектов файлов и вложенных папок):_

```json
{
    "parent": 11,
    "files": [
        {
            "id": 1,
            "name": "Чувааааак.png",
            "size": 2022246,
            "star": false,
            "created_at": "2024-02-17 07:00"
        },
        {
            "id": 37,
            "name": "Чувааааак.png",
            "size": 2022246,
            "star": false,
            "created_at": "2024-02-18 09:02"
        }
    ],
    "folders": [
        {
            "id": 47,
            "name": "test1",
            "star": false,
            "created_at": "2024-02-17 20:02",
            "updated_at": "2024-02-17 20:02"
        },
        {
            "id": 52,
            "name": "test_aaaa",
            "star": false,
            "created_at": "2024-02-18 09:01",
            "updated_at": "2024-02-18 09:01"
        }
    ]
}
```

### ** _Объяснение значений ответа:_

| ключ       | что это такое                                                                                                      |
|------------|--------------------------------------------------------------------------------------------------------------------|
| parent     | id родительской папки относительно запрашиваемой (если запрашиваемая папка - корневая, то parent будет равен null) |
| id         | Уникальный id файла (или папки)                                                                                    |
| name       | Имя файла (или папки)                                                                                              |
| size       | Размер файла в байтах                                                                                              |
| star       | true, если файл в избранных (или папка)                                                                            |
| created_at | дата и время создания файла (или папки)                                                                            |
| updated_at | дата и время последнего изменения папки                                                                            |

<hr>

### ** _Статус ответа (при успехе):_ 200
