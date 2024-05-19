
from fastapi import HTTPException, status


class BaseAppException(HTTPException):
    status_code = 500
    default_detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.default_detail)


class UserAlreadyExistsException(BaseAppException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Пользователь с такой почтой уже существует"


class UserIncorrectPasswordException(BaseAppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Неверный email или пароль"


class TokenExpiredException(BaseAppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Токен истек"


class TokenAbsentException(BaseAppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Токен отсутствует"


class IncorrectTokenFormat(BaseAppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Некорректный формат токена"


class UserIdNotFoundException(BaseAppException):
    status_code = status.HTTP_401_UNAUTHORIZED


class UserNotFoundException(BaseAppException):
    status_code = status.HTTP_401_UNAUTHORIZED
