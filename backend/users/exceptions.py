from rest_framework.views import exception_handler


def core_exception_handler(exc, context):
    # Если возникает исключение, которые мы не обрабатываем здесь явно, мы
    # хотим передать его обработчику исключений по-умолчанию, предлагаемому
    # DRF. И все же, если мы обрабатываем такой тип исключения, нам нужен
    # доступ к сгенерированному DRF - получим его заранее здесь.
    response = exception_handler(exc, context)
    # словарь с видом ошибки и её обработчиком
    handlers = {
        # users
        'AuthenticationFailed': _handle_error,
        'ValidationError': _handle_invalid_data_validation_error,
        'TokenNDoesNotExist': _handle_my_error,
        'UserValidateError': _handle_my_error,
        'UserAccessForbidden': _handle_my_error,
        # storage_api
        'FolderValueError': _handle_my_error,
        'FileNotGivenError': _handle_my_error,
    }
    # Определить тип текущего исключения. Мы воспользуемся этим сразу далее,
    # чтобы решить, делать ли это самостоятельно или отдать эту работу DRF.
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        # Если это исключение можно обработать - обрабатываем. В противном
        # случае, вернуть ответ сгенерированный стандартными средствами заранее
        return handlers[exception_class](exc, context, response)

    return response


def _handle_error(exc, context, response):
    # Это самый простой обработчик исключений, который мы можем создать. Мы
    # берем ответ сгенерированный DRF и заключаем его в ключ 'errors'.
    response.data = {
        'errors': response.data
    }
    return response


def _handle_invalid_data_validation_error(exc, context, response):
    """ValidationError error handler"""

    # получаем информацию об ошибке
    response_data = response.data
    new_response_data = {}

    # поля для проверки в запросе
    fields = ['email', 'password', 'old_password', 'new_password']
    for field in fields:
        # если есть ошибки, связанные с field, то в цикле перебираем их и записываем в отдельную переменную
        if field in response_data:
            errors = response_data.get(field)
            for error in errors:
                error_code = error.code
                error_message = str(error)
                new_response_data[f'{field} {error_code}'] = error_message

    # если есть ошибки в переменной, то заменяем содержимое дефолтного ответа на неё
    if new_response_data:
        response.data = new_response_data
    # если в теле ответа хоть что-то есть
    if response.data:
        response.data = {'errors': response.data}

    return response


def _handle_my_error(exc, context, response):
    """UserValidateError and UserAccessForbidden errors handler"""

    # получаем ошибку
    error_detail = response.data.get('detail', None)
    # если ничего нет, то генерим дефолтный ответ
    if not error_detail:
        return response

    # достаём код и описание ошибки
    error_code = error_detail.code
    error_message = str(error_detail)

    # упаковываем ошибку в "JSON"
    response.data = {
        'errors': {
            error_code: error_message
        }
    }
    return response
