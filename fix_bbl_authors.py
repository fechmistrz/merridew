#!/usr/bin/env python3
"""
This script opens .bbl file and replaces 'and' with ',' in authors
"""

import os
import logging
import re
import sys


def find_replace(input_file):
    """Fix 'authors' entries"""
    bibitem_line = False
    new_content = list()

    with open(input_file, "r") as f:
        for line in f:
            new_line = line
            if bibitem_line:
                new_line = new_line.replace(", and ", ", ")
                new_line = new_line.replace(" and ", ", ")

            if new_line != line:
                logging.warning("Changing '{}' => '{}'".format(line.strip(), new_line.strip()))

            new_content.append(new_line)

            match = re.search(r"^\\bibitem.*", line)
            if match:
                bibitem_line = True
            else:
                bibitem_line = False

    with open(input_file, "w") as f:
        for line in new_content:
            f.write(line)

    return


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    find_replace(sys.argv[1])
