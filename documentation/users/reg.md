## 1. Регистрация нового юзера

### ** _URL:_ http://79.137.204.172/api/user/reg/

### ** _Метод:_ POST

<hr>

### ** _Пример для отправки запроса (body, JSON):_

```json
{
    "email": "test10@test.ru",
    "password": "qwerty123"
}
```

### ** _Объяснение значений запроса:_

| ключ     | что это такое                               |
|----------|---------------------------------------------|
| email    | Почта, которую вводит юзер для регистрации  |
| password | Пароль, который вводит юзер для регистрации |

<hr>

### ** _Пример ответа сервера (JSON):_

```json
{
    "email": "test10@test.ru",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTEsImV4cCI6MTcwOTA1ODE3OX0.-RIvAaZ7A75uV_RBGe9GGTq24rke-JzsDm7DnnaUWmA",
    "nickname": "User_012730",
    "photo": "http://79.137.204.172/static/profile_photos/default_user_profile_photo.png"
}
```

### ** _Объяснение значений ответа:_

| ключ     | что это такое                              |
|----------|--------------------------------------------|
| email    | Почта только что зарегистрированного юзера |
| token    | Токен для юзера                            |
| nickname | Ник юзера                                  |
| photo    | Фото профиля юзера (ссылка)                |

<hr>

### ** _Статус ответа (при успехе):_ 201
