#!/usr/bin/env python3
import json
from os import path
import time
import lzma

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

    with open(path.join(HERE, 'out', 'data.json'), 'rb') as infile:
        f = lzma.LZMAFile(path.join(HERE, 'out', 'data.json.xz'), mode="wb")
        f.write(infile.read())
        f.close()


if __name__ == '__main__':
    main()