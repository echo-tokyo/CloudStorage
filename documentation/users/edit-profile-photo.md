## 1. Обновление фото профиля юзера

### ** _URL:_ http://79.137.204.172/api/user/edit-profile-photo/

### ** _Метод:_ PUT

<hr>

### ** _Пример для отправки запроса

#### 1. body, FormData

```jshint
{
    formData.append('photo', file);

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
| photo         | Объект файла (обязательно фотография)   |
| Authorization | Bearer (токен юзера)                    |

<hr>

### ** _Пример ответа сервера (JSON):_

```json
{
    "photo_url": "http://79.137.204.172/static/profile_photos/user_19.jpg"
}
```

### ** _Объяснение значений ответа:_

| ключ      | что это такое                     |
|-----------|-----------------------------------|
| photo_url | Фото профиля юзера (новая ссылка) |

<hr>

### ** _Статус ответа (при успехе):_ 200
