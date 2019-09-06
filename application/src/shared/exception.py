class AppError(Exception):
    """Clase base para excepciones en el módulo."""

    def __init__(self, code: int, message: str, status_code: int):
        self.code = code
        self.message = message
        self.status_code = status_code


class BadRequest(AppError):
    """Clase base para excepciones en el módulo."""

    def __init__(self, code: int, message: str, status_code: int = 401):
        super().__init__(code, message, status_code)


class UnauthorizedRequest(AppError):
    """Clase base para excepciones en el módulo."""

    def __init__(self, code: int = 4030, message: str = 'No tiens permiso', status_code: int = 403):
        super().__init__(code, message, status_code)
