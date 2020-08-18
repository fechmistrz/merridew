#!/usr/bin/env python3
"""
This script opens .bbl file and replaces 'and' with ',' in authors
"""

import os
import re
import sys


def find_replace(input_file):
    """Fix 'authors' entries"""
    bibitem_line = False
    new_content = list()

    with open(input_file, "r") as f:
        for line in f:
            # line = raw_line.strip()
                
            match = re.search(r"^\\bibitem.*", line)
            if match:
                bibitem_line = True
            else:
                bibitem_line = False

            if bibitem_line:
                line = line.replace(", and ", ", ")
                line = line.replace(" and ", ", ")

            new_content.append(line)
    
    with open(input_file, "w") as f:
        for line in new_content:
            f.write(line + "\n")

    return


if __name__ == "__main__":
    find_replace(sys.argv[1])