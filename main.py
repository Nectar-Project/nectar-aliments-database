#!/usr/bin/env python3
import json
from os import path

from fdb.datasources import Datasources

HERE = path.dirname(path.abspath(__file__))


def main():
    datasources = Datasources()
    data = datasources.generate()
    with open(path.join(HERE, 'out', 'data.json'), 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    main()