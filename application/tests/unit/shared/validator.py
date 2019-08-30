import datetime
import unittest


from src.shared.domain.validator import is_not_none, string_validator, integer_validator, integer_positive, \
    date_validator

from src.shared.exception import BadRequest


class AlgunObject:
    def __init__(self) -> None:
        self.name = 'jose'


class TestSharedDomainValidatorIsNone(unittest.TestCase):

    def test_data_none(self):
        with self.assertRaises(BadRequest):
            is_not_none(None)

    def test_data_string(self):
        self.assertEqual('123', is_not_none('123'))

    def test_data_string_empty(self):
        self.assertEqual('', is_not_none(''))

    def test_data_integer(self):
        self.assertEqual(2, is_not_none(2))

    def test_data_integer_zero(self):
        self.assertEqual(0, is_not_none(0))


class TestSharedDomainValidatorString(unittest.TestCase):

    def test_data_ok(self):
        self.assertEqual('hola', string_validator('hola'))

    def test_data_empty(self):
        self.assertEqual('', string_validator(''))

    def test_data_integer(self):
        self.assertEqual('1', string_validator(1))
        self.assertEqual('0', string_validator(0))
        self.assertEqual('-1', string_validator(-1))

    def test_data_bool(self):
        self.assertEqual('True', string_validator(True))
        self.assertEqual('False', string_validator(False))

    def test_data_float(self):
        self.assertEqual('1.01', string_validator(1.01))
        self.assertEqual('0.01', string_validator(0.01))

    def test_data_None(self):
        self.assertEqual(None, string_validator(None))

    def test_data_object(self):
        with self.assertRaises(BadRequest):
            string_validator(AlgunObject())


class TestSharedDomainValidatorInteger(unittest.TestCase):

    def test_data_ok(self):
        self.assertEqual(5, integer_validator(5))

    def test_data_empty(self):
        with self.assertRaises(BadRequest):
            integer_validator('0')
            integer_validator('')

    def test_data_integer(self):
        self.assertEqual(1, integer_validator('1'))
        self.assertEqual(0, integer_validator('0'))
        self.assertEqual(-1, integer_validator('-1'))

    def test_data_bool(self):
        with self.assertRaises(BadRequest):
            integer_validator(True)
            integer_validator(False)

    def test_data_float(self):
        self.assertEqual(2, integer_validator(1.01))
        self.assertEqual(1, integer_validator(0.01))

    def test_data_None(self):
        self.assertEqual(None, integer_validator(None))

    def test_data_object(self):
        with self.assertRaises(BadRequest):
            integer_validator(AlgunObject())
            integer_validator('hola')


class TestSharedDomainValidatorIntegerPositive(unittest.TestCase):
    def test_data_None(self):
        self.assertEqual(None, integer_positive(None))

    def test_data_ok(self):
        self.assertEqual(5, integer_positive(5))

    def test_data_empty(self):
        with self.assertRaises(BadRequest):
            integer_positive(-1)


class TestSharedDomainValidatorDate(unittest.TestCase):
    def test_data_ok(self):
        self.assertEqual(datetime.date(2019, 1, 1), date_validator('2019-01-01'))

    def test_data_none(self):
        self.assertEqual(None, date_validator(None))

    def test_data_object(self):
        with self.assertRaises(BadRequest):
            date_validator(AlgunObject())

    def test_data_error(self):
        with self.assertRaises(BadRequest):
            date_validator('')
            date_validator('texto')
            date_validator(0)
            date_validator(0.324)

    def test_data_date_error(self):
        with self.assertRaises(BadRequest):
            date_validator('2019-34-34')
            date_validator('12-12-2019')

