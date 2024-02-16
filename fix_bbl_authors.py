#!/usr/bin/env python3
"""
This script modifies .bbl file in place, imitating English-Polish translation
"""

import os
import logging
import re
import sys


def find_replace(input_file):
    """Fix 'authors' entries"""
    new_content = list()

    with open(input_file, "r") as f:
        is_authors_line = False
        for raw_line in f:
            line = raw_line

            replacements = [
                ('(.*)(pages )([0-9]+--[0-9]+)(.*)', r'\1strony \3\4'),
                ('(.*)(volume[~ ])([0-9]+ )of (.*)', r'\1tom~\3\4'),
                ('(.*), volume~([0-9]+),(.*)', r'\1, tom~\2,\3'),
                ('(.*), No. ([0-9]+[.]?)$', r'\1, numer \2'),
                ('(.*), Vol. ([0-9]+)(.*)', r'\1, tom \2\3'),
                ('^(.newblock) In (.*)', r'\1 W \2'),
                ('^(.newblock) (PhD thesis)(.*)', r'\1 Praca doktorska\3'),
            ]
            for r in replacements:
                new_line = re.sub(r[0], r[1], line)
                if line != new_line:
                    logging.warning(f"Changing: {line.strip()} -> {new_line.strip()}")
                    line = new_line

            if re.search(r"^\\bibitem.*", line):
                is_authors_line = True
                authors = ""
                new_content.append(line)
                continue

            if re.search(r"^\\newblock.*", line):
                if is_authors_line:
                    new_content.append(" ".join(authors.strip().split()).replace(", and ", " oraz ").replace(" and ", " oraz ") + "\n")
                    is_authors_line = False

            if is_authors_line:
                authors += line.strip() + " "
            else:
                new_content.append(line.strip())


    with open(input_file, "w") as f:
        new_content = " ".join(new_content)
        while "  " in new_content:
            new_content = new_content.replace("  ", " ")
        new_content = new_content.replace(" \\newblock ", "\n\\newblock ").replace(" \\bibitem", "\n\\bibitem").replace("\n ", "\n").replace("\n\n", "\n").replace("\\bibitem", "\n\\bibitem")
        f.write(new_content)

    return


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    find_replace(sys.argv[1])
    find_replace(sys.argv[1])
