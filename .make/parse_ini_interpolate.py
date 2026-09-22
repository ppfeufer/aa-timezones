#!/usr/bin/env python3

"""
This script parses INI files, normalizes the section and key names, and resolves interpolations in the values. It can output the results in different formats based on the specified mode.
"""

# Standard Library
import re
import sys
from pathlib import Path


def normalize_name(section, key):
    """
    Normalize the section and key names to a consistent format.

    :param section: The section name from the INI file
    :param key: The key name from the INI file
    :return: A normalized name in the format SECTION__KEY, uppercased and with non-alphanumeric characters replaced by underscores
    """

    if section is None or section == "":
        name = key
    else:
        name = f"{section}__{key}"

    name = name.upper()
    name = re.sub(r"[^A-Z0-9_]", "_", name)

    return name


def parse_files(files):
    """
    Parse the given INI files and return a dictionary of normalized names to values, along with the order of the names.

    :param files: A list of file paths to INI files
    :return: A tuple containing a dictionary of normalized names to values and a list of names in the order they were parsed
    """

    vals = {}
    order = []
    section = ""

    for fp in files:
        p = Path(fp)

        if not p.exists():
            continue

        with p.open(encoding="utf-8") as f:
            for line in f:
                s = line.rstrip("\n")
                # section header
                m = re.match(r"^\s*\[([^]]+)]\s*$", s)

                if m:
                    section = m.group(1).strip()

                    continue

                # skip comments or empty
                if re.match(r"^\s*[#;]", s) or not re.search(r"=", s):
                    continue

                # split on first '='
                key, val = re.split(r"=", s, maxsplit=1)
                key = key.strip()
                val = val.strip()
                name = normalize_name(section, key)
                vals[name] = val
                order.append(name)

    return vals, order


def resolve_interpolations(vals, order, max_iters=10):
    """
    Resolve interpolations in the values of the given dictionary.

    :param vals: A dictionary of normalized names to values
    :param order: A list of names in the order they were parsed
    :param max_iters: The maximum number of iterations to resolve interpolations
    :return: The dictionary of values with interpolations resolved
    """

    pattern = re.compile(r"\$\{([^}:]+):?([^}]*)}")

    for _ in range(max_iters):
        changed = False

        for name in order:
            v = vals.get(name, "")

            def _repl(m):
                """
                Replacement function for regex substitution.

                :param m: The regex match object
                :return: The replacement string
                """

                sec = m.group(1) or ""
                key = m.group(2) or ""

                if key == "":
                    # If no colon provided, treat whole as key and empty section
                    ref = normalize_name("", sec)
                else:
                    ref = normalize_name(sec, key)
                return vals.get(ref, "")

            newv = pattern.sub(_repl, v)

            if newv != v:
                vals[name] = newv
                changed = True

        if not changed:
            break

    return vals


def main(argv):
    """
    Main function to parse INI files and resolve interpolations.

    :param argv: A list of command-line arguments
    :return: None
    """

    mode = "make"
    files = []
    i = 1

    while i < len(argv):
        a = argv[i]

        if a.startswith("--mode="):
            mode = a.split("=", 1)[1]
        else:
            files.append(a)

        i += 1

    vals, order = parse_files(files)
    vals = resolve_interpolations(vals, order)
    out_lines = []

    if mode == "names":
        seen = set()

        for name in order:
            if name in seen:
                continue

            seen.add(name)
            out_lines.append(name)

        sys.stdout.write("\n".join(out_lines) + "\n")

        return

    for name in order:
        v = vals.get(name, "")

        if mode == "make":
            # Escape $ for Makefile (write $$ so that Makefile sees a single $)
            v = v.replace("$", "$$")
            out_lines.append(f"{name} := {v}")
        else:
            out_lines.append(f"{name}={v}")

    sys.stdout.write("\n".join(out_lines) + "\n")


if __name__ == "__main__":
    main(sys.argv)
