## 1. Загрузка файла на сервер

### ** _URL:_ http://79.137.204.172/api/storage/upload-file-to-server/

### ** _Метод:_ POST

<hr>

### ** _Пример для отправки запроса

#### 1. body, FormData

```jshint
{
    formData.append('folder_id', 1);
    formData.append('file', file);

}
```

#### 2. headers (содержит токен юзера)

```json
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZXhwIjoxNzA2MjE5MjMyfQ.yMy6RiCFvhitLZ0IavmQS4P_O1-ksLQgaA8JsB3LLl0"
}
```

### ** _Объяснение значений запроса:_

| ключ          | что это такое                           |
|---------------|-----------------------------------------|
| folder_id     | Id папки, в которую юзер добавляет файл |
| file          | Объект файла (получен в input)          |
| Authorization | Bearer (токен юзера)                    |

<hr>

### ** _Пример ответа сервера (JSON):_

```json
{
  "id": 7,
  "name": "prezi_info",
  "size": 4934,
  "star": false,
  "created_at": "2024-02-02 20:26:"
}
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

### ** _Статус ответа (при успехе):_ 201
