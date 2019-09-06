import unittest

from src.shared.exception import AppError, BadRequest, UnauthorizedRequest


class TestSharedDomainException(unittest.TestCase):

    def test_exception_app_empty(self):
        try:
            raise AppError(4010, "mensaje", 401)
        except AppError as e:
            self.assertEqual(4010, e.code)
            self.assertEqual('mensaje', e.message)
            self.assertEqual(401, e.status_code)
        except Exception as e:
            self.assertEqual('no entro  a la exception AppError', '')

    def test_exception_no_entran_todos_los_parametros(self):
        with self.assertRaises(Exception):
            raise AppError(4010)

    def test_exception_app_bad_request(self):
        try:
            raise BadRequest(4010, "mensaje")
        except BadRequest as e:
            self.assertEqual(4010, e.code)
            self.assertEqual('mensaje', e.message)
            self.assertEqual(401, e.status_code)
        except AppError as e:
            self.assertEqual('no entro  a la exception AppError', '')
        except Exception as e:
            self.assertEqual('no entro  a la exception AppError', '')

    def test_exception_app_unauthrized_request(self):
        try:

            raise UnauthorizedRequest(4030, "mensaje")
        except UnauthorizedRequest as e:
            self.assertEqual(4030, e.code)
            self.assertEqual('mensaje', e.message)
            self.assertEqual(403, e.status_code)
        except AppError as e:
            self.assertEqual('no entro  a la exception AppError', '')
        except Exception as e:
            self.assertEqual('no entro  a la exception AppError', '')
