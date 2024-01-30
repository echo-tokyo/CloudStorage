from .models import Token


class TokenNotInTable(Exception):
    def __init__(self, message):
        super().__init__(message)


class CheckTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.

        # print('\nrequest', request)
        # print(request.headers)

        try:
            auth_header = request.headers['Authorization']
        except KeyError:
            # если нет заголовка Authorization, то пропускаем все действия ниже
            return self.get_response(request)

        header_token = auth_header.split(' ')[-1]
        print([header_token])

        table_token = Token.objects.filter(token=header_token)
        # если токен не был найден в БД
        if not table_token:
            raise TokenNotInTable('Sent token was not found in table')

        # здесь находится QuerySet
        print(table_token)

        response = self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        return response


# request <WSGIRequest: POST '/api/user/login/'>
# ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cors_enabled', '_current_scheme_host', '_encoding',
# '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files',
# '_mark_post_parse_error', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers',
# 'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'encoding',
# 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_signed_cookie', 'headers',
# 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match',
# 'scheme', 'session', 'upload_handlers', 'user']
#
#
# response <Response status_code=200, "application/json">
# ['__bytes__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_charset',
# '_container', '_content_type_for_repr', '_handler_class', '_is_rendered', '_post_render_callbacks', '_reason_phrase',
# '_request', '_resource_closers', 'accepted_media_type', 'accepted_renderer', 'add_post_render_callback', 'charset',
# 'close', 'closed', 'content', 'content_type', 'context_data', 'cookies', 'data', 'delete_cookie', 'exception',
# 'flush', 'get', 'getvalue', 'has_header', 'headers', 'is_rendered', 'items', 'make_bytes', 'readable',
# 'reason_phrase', 'render', 'rendered_content', 'renderer_context', 'rendering_attrs', 'resolve_context',
# 'resolve_template', 'seekable', 'serialize', 'serialize_headers', 'set_cookie', 'set_signed_cookie', 'setdefault',
# 'status_code', 'status_text', 'streaming', 'tell', 'template_name', 'using', 'writable', 'write', 'writelines']
