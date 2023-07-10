#!/usr/bin/env python3
"""
This script opens .bib file and sorts it's entries by year
"""

import argparse
import logging
import re


def strip_year(text):
    """Filter non-digit characters and convert to int"""

    return int("".join([ch for ch in text if ch not in " {},"]))


def sort_key(entry):
    """Print 'year name', key for sorting function"""

    name = entry["bibtex_name"]
    year = strip_year(entry["year"])
    output = "{} {}".format(year, name)

    logging.debug("sort_key => %s", output)
    return output


def print_nicely(lst):
    """Convert list of dicts into nice .bib content"""

    output = ""
    for entry in lst:
        bibtex_name = entry.pop("bibtex_name")
        bibtex_type = entry.pop("bibtex_type")
        tags = sorted(["    {} = {}".format(key.upper(), entry[key]) for key in entry])
        output += "@{} {{{},\n".format(bibtex_type, bibtex_name)
        output += "\n".join(tags)
        output += "\n}\n\n"
    return output


def validate_authors(authors):
    # old_regex = r"^(Mc|\\'|De |van |Van |van der |\\\")?[A-Z][a-zćê'\"\\]+(-[A-Z][a-z~\\]+)?, (De |\\')?[A-Z][a-z'\"\\]+(-[A-Z][a-z'\\]+)? *((Mc)?[A-Z]\. *)*,?$"
    
    # Zoran Škoda
    # David Heath-Brown
    # Marie-Claude Sarmant-Durix
    # lowercase diacritics are too numerous to explain
    UP = "[A-ZŠ]"
    LO = "[a-zßáäèéêóüć]"
    # "".join(sorted(LO))

    regex = f"(De |git Mc|van |van der )?{UP}{LO}+(-{UP}{LO}+)?, ({UP}{LO}+-)?{UP}{LO}+( {UP}\.)*$"
    authors = authors.replace("{", "")
    authors = authors.replace("}", "")
    for author in authors.split(" and "):
        if not re.match(regex, author):
            raise ValueError(f"Incorrect author syntax '{author}' in '{authors}'")
    return


def parse_bib(input_bib_file):
    """Converts .bib file into list of entries"""
    entries = dict()
    accepted_line = re.compile("^( *[A-Z]+ *= *\{.*\},|^@[a-z]+ \{[a-z]+_?[0-9]+,|\}|\s*)$")

    with open(input_bib_file, "r") as bib_file:
        for raw_line in bib_file:
            line = raw_line.strip()
            if not accepted_line.match(line):
                raise NotImplementedError("Syntax error in .bib file: " + line)

            match = re.search(" *@([^ ]+) *{ *([^,]+),", line)
            if match:
                # when line is: "@article {alexander28,"
                bibtex_type = match.group(1).lower()
                bibtex_name = match.group(2)
                logging.debug("parse_bib => type %s name %s", bibtex_type, bibtex_name)

                entries[bibtex_name] = {
                    "bibtex_type": bibtex_type,
                    "bibtex_name": bibtex_name,
                }

            match = re.search(" *([a-zA-Z]+) *= *(.*)", line)
            if match:
                # when line is: "    author = {Alexander, J. W.},"
                key = match.group(1).lower()
                value = match.group(2)

                if value.startswith("{"):
                    value = value[1:]
                else:
                    raise Exception(f"{value=} does not start with a brace")
                if value.endswith("},"):
                    value = value[:-2]
                logging.debug("parse_bib => key %s value %s", key, value)

                if key == "author":
                    validate_authors(value)

                entries[bibtex_name][key] = f"{{{value}}},"
    return entries


def bibliography_sort(input_bib_file):
    """Main function sorting bibliography entries"""

    entries = parse_bib(input_bib_file)
    entries = sorted(list(entries.values()), key=sort_key)
    with open(input_bib_file, "w") as output_bib_file:
        output_bib_file.write(print_nicely(entries))


def check_mandatory_optional(input_bib_file):
    """Looks for missing mandatory or illegal optional fields"""

    entry_type = "@unknown"
    entry_name = "unknown80"
    field = "???"
    fields = list()

    correct_values = {
        "@article": ["author", "title", "journal", "year"],
        "@book": ["author", "title", "publisher", "year"],
        "@incollection": ["author", "title", "booktitle", "publisher", "year"],
        "@inproceedings": ["author", "title", "booktitle", "year"],
        "@misc": [],
        "@phdthesis": ["author", "title", "school", "year"],
    }

    with open(input_bib_file, "r") as bib_file:
        for raw_line in bib_file:
            line = raw_line.strip()

            if line.startswith("@"):
                entry_type, entry_name = line.replace("{", "").replace(",", "").split()
                if entry_type not in correct_values.keys():
                    raise Exception(f"ENTRY TYPE {entry_type}")

            elif " = " in line:
                field = line.split(" = ")[0].lower()
                fields.append(field)

            elif line.startswith("}"):
                missing = [f for f in correct_values[entry_type] if f not in fields]
                if missing:
                    raise Exception(f"Missing {missing} in {entry_name}!")
                fields = list()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bib", help="Path to the bibliography file", required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    bibliography_sort(args.bib)
    check_mandatory_optional(args.bib)
