class ModelBase:
    @classmethod
    def printer(cls):
        return 'printer'


class ModelA(ModelBase):
    id = '1'

    def __init__(self, id, name) -> None:
        self.id = id,
        self.name = name

    @classmethod
    def print(cls):
        return {
            'id',cls.id
        }
