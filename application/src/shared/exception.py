


class AppError(Exception):
    """Clase base para excepciones en el módulo."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class BadRequest(AppError):
    """Clase base para excepciones en el módulo."""
    pass

class UnauthorizedRequest(AppError):
    """Clase base para excepciones en el módulo."""
    pass


class Example(AppError):
    """Excepción lanzada por errores en las entradas.

    Atributos:
        expresion -- expresión de entrada en la que ocurre el error
        mensaje -- explicación del error
    """

    def __init__(self, expresion, mensaje):
        self.expresion = expresion
        self.mensaje = mensaje
