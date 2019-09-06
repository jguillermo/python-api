import uuid
from abc import ABC, abstractmethod

from src.shared.domain.validator import string_validator, integer_validator
from src.shared.exception import BadRequest


class TypeBase:

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def is_none(self) -> bool:
        return self._value is None


class TypeString(TypeBase):
    def __init__(self, value):
        _value = string_validator(value)
        super().__init__(_value)

    def __str__(self) -> str:
        return self.value()


class TypeUuid(TypeString):
    def __init__(self, value):
        super().__init__(value)
        self._validate_uuid()

    def _validate_uuid(self, message='No es un uuid válido'):
        if self.is_none():
            return True

        try:
            _uuid = uuid.UUID(self.value())
        except Exception as e:
            raise BadRequest(4047, message)

    @classmethod
    def random(cls):
        return cls(uuid.uuid4().__str__())

    @classmethod
    def by_name(cls, name: str):
        return cls(uuid.uuid5(uuid.NAMESPACE_DNS, name).__str__())


class TypeId(TypeUuid):
    def __init__(self, value):
        super().__init__(value)
        if self.is_none():
            raise BadRequest(4046, "El Id no puede ser nulo")
        self._validate_uuid(message='No es un valor válido para el Id')


class TypeInteger(TypeBase):

    def __init__(self, value):
        _value = integer_validator(value)
        super().__init__(_value)

    def __str__(self) -> str:
        return str(self.value())
