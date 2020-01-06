#!/usr/bin/env python3
import json
from os import path
import time;

from fdb.datasources import Datasources

HERE = path.dirname(path.abspath(__file__))


def main():
    datasources = Datasources()
    data = datasources.generate()
    version = int(time.time())
    out = {
        "version": version,
        "aliments": data
    }
    with open(path.join(HERE, 'out', 'data.json'), 'w') as outfile:
        json.dump(out, outfile)

    with open(path.join(HERE, 'out', 'version.json'), 'w') as outfile:
        json.dump({"version": version}, outfile)


if __name__ == '__main__':
    main()