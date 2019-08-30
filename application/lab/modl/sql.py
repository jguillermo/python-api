class Sql:
    def __init__(self) -> None:
        print("se inicio el SQL")
        self.params = None

    def get_sql(self):
        return 'ejecutando sql {}'.format(self.params)

    def set_paramas(self, params):
        self.params = params
