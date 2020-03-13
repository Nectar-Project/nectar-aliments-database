#from fdb.datasources.ciqual import CiqualDatasource
from fdb.datasources.cnf import CnfDatasource


class Datasources:
    def __init__(self):
        self.datasources = [
            # Ciqual has not enough data
            # CiqualDatasource()
            CnfDatasource()
        ]

    def generate(self):
        return self.datasources[0].generate()