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
    try:
        year = strip_year(entry["year"])
    except:
        # workaround for @unpublished
        try:
            year = strip_year(entry["note"])
        except:
            raise Exception(f"Cannot find year in {entry}")
    output = "{} {}".format(year, name)

    logging.debug("sort_key => %s", output)
    return output


def print_nicely(lst):
    """Convert list of dicts into nice .bib content"""

    output = ""
    for entry in lst:
        bibtex_name = entry.pop("bibtex_name")
        bibtex_type = entry.pop("bibtex_type")
        official_fields = get_mandatory_fields("@" + bibtex_type) + get_optional_fields("@" + bibtex_type)
        human_friendly_keys = [key for key in official_fields if key in entry] + [key for key in entry if key not in official_fields]
        tags = ["    {} = {}".format(key.upper(), entry[key]) for key in human_friendly_keys]
        output += f"@{bibtex_type} {{{bibtex_name},\n"
        output += "\n".join(tags)
        output += "\n}\n\n"
    return output


def validate_authors(authors):
    # old_regex = r"^(Mc|\\'|De |van |Van |van der |\\\")?[A-Z][a-zćê'\"\\]+(-[A-Z][a-z~\\]+)?, (De |\\')?[A-Z][a-z'\"\\]+(-[A-Z][a-z'\\]+)? *((Mc)?[A-Z]\. *)*,?$"

    # Zoran Škoda
    # David Heath-Brown
    # Marie-Claude Sarmant-Durix
    # lowercase diacritics are too numerous to explain
    UP = "[A-ZÉÖŠ]"
    LO = "[a-zßááäâèéêíñóöüćł]"
    # "".join(sorted(LO))

    regex = f"(De |Mc|Van |van |van der )?{UP}{LO}+(-{UP}{LO}+)?, ({UP}{LO}+-|De )?{UP}{LO}+( (Mc)?{UP}\.)*$"
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


def get_mandatory_fields(entry_type):
    mandatory_fields = {
        "@article": ["author", "title", "journal", "fjournal", "year"],
        "@book": ["author", "title", "publisher", "year"],
        "@incollection": ["author", "title", "booktitle", "publisher", "year"],
        "@inproceedings": ["author", "title", "booktitle", "year"],
        "@misc": [],
        "@phdthesis": ["author", "title", "school", "year"],
        "@unpublished": ["author", "title", "note"],
    }

    if entry_type not in mandatory_fields:
        raise Exception("I don't know which fields are mandatory for %s!" % entry_type)
    return mandatory_fields[entry_type]


def get_optional_fields(entry_type):
    optional_fields = {
        "@article": ["volume", "number", "pages", "month", "note"],
        "@book": ["volume", "number", "series", "address", "edition", "month", "note"],
        "@incollection": ['editor', 'volume', 'number', 'series', 'type', 'chapter', 'pages', 'address', 'edition', 'month', 'note'],
        "@inproceedings": ["editor", "volume", "number", "series", "pages", "address", "month", "organization", "publisher", "note"],
        "@misc": ["author", "title", "howpublished", "month", "year", "note"],
        "@phdthesis": ["type", "address", "month", "note"],
        "@unpublished": ["month", "year"],
    }.get(entry_type, [])

    if not optional_fields:
        logging.warning("I don't know which fields are optional for %s!" % entry_type)
        return []

    optional_agnostic_fields = [
        "doi", "pages", "url",
        "issn", "isbn",
        "mrclass", "mrnumber", "mrreviewer", # used in citations from MathSciNet
        "zbl"                                # used in ZentralBlatt Math
    ]
    optional_agnostic_fields = [f for f in optional_agnostic_fields if f not in optional_fields]
    optional_fields += optional_agnostic_fields

    return optional_fields


def check_mandatory_optional(input_bib_file):
    """Looks for missing mandatory or illegal optional fields"""

    entry_type = "@unknown"
    entry_name = "unknown80"
    field = "???"
    fields = list()

    with open(input_bib_file, "r") as bib_file:
        for raw_line in bib_file:
            line = raw_line.strip()

            if line.startswith("@"):
                entry_type, entry_name = line.replace("{", "").replace(",", "").split()
                must_have = get_mandatory_fields(entry_type)
                may_have = get_optional_fields(entry_type)

            elif " = " in line:
                field = line.split(" = ")[0].lower()
                fields.append(field)

            elif line.startswith("}"):
                missing = set(must_have) - set(fields)
                if missing:
                    raise Exception(f"Missing {missing} in {entry_name}!")


                unexpected_fields = set(fields) - set(must_have)
                if may_have:
                    unexpected_fields = sorted(list(set(unexpected_fields) - set(may_have)))
                if unexpected_fields:
                    logging.warning(f"Found unexpected fields: {unexpected_fields} in {entry_name} ({entry_type})")

                fields = list()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bib", help="Path to the bibliography file", required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    bibliography_sort(args.bib)
    check_mandatory_optional(args.bib)
