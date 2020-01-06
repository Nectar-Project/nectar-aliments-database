from fdb.datasources.ciqual import CiqualDatasource


class Datasources:
    def __init__(self):
        self.datasources = [
            CiqualDatasource()
        ]

    def generate(self):
        return self.datasources[0].generate()