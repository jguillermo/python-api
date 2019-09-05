class Response:
    PROCESS_SUCCESS_CODE = 2
    PROCESS_SUCCESS_MESSAGE = 'SUCCESS'

    PROCESS_ERROR_CODE = 4
    PROCESS_ERROR_MESSAGE = 'ERROR'

    @classmethod
    def success(cls, data, code=None):
        try:
            return cls._schema(True,
                               cls.PROCESS_SUCCESS_CODE if code is None else code,
                               cls.PROCESS_SUCCESS_MESSAGE,
                               data if data is not None else [])
        except Exception as e:
            raise e

    @classmethod
    def error(cls, message, code=None):
        try:
            return cls._schema(False,
                               cls.PROCESS_ERROR_CODE if code is None else code,
                               cls.PROCESS_ERROR_MESSAGE if message is None else message,
                               [])
        except Exception as e:
            raise e

    @staticmethod
    def _schema(success, code, message, data):
        return {
            'success': success,
            'code': code,
            'message': message,
            'data': data
        }
