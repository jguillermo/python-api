from validator_collection import validators, checkers, errors

from src.shared.exception import BadRequest


def is_not_none(value, error_message='el valor no puede ser nulo'):
    if value is None:
        raise BadRequest(error_message)
    return value


def string_validator(value, error_message='ingrese un string valido'):
    if value is None:
        return None

    if isinstance(value, bool):
        return 'True' if value else 'False'

    if isinstance(value, int) and value == 0:
        return '0'

    try:
        data_valid = validators.string(value, coerce_value=True, allow_empty=True)
        if data_valid is None:
            return ''
        if len(data_valid) > 10 and data_valid[0] == '<' and data_valid[-1] == '>' and value.__class__ in data_valid:
            raise BadRequest('no se puede convertir el string')
    except Exception as e:
        raise BadRequest(error_message)

    return data_valid


def integer_validator(value, error_message='ingrese un número válido'):
    if value is None:
        return None

    if isinstance(value, bool):
        raise BadRequest(error_message)

    try:
        data_valid = validators.integer(value, coerce_value=True, allow_empty=True)

    except Exception as e:
        raise BadRequest(error_message)

    return data_valid


def integer_positive(value, error_message='el numero debe ser mayor a cero'):
    try:
        data_valid = integer_validator(value)

    except Exception as e:
        raise BadRequest(error_message)

    if data_valid is None:
        return None

    if data_valid <= 0:
        raise BadRequest(error_message)

    return data_valid


def date_validator(value, error_message='ingrese una fecha válida'):
    if value is None:
        return None

    try:
        data_valid = validators.date(value, coerce_value=True, allow_empty=True)

    except Exception as e:
        raise BadRequest(error_message)

    return data_valid
