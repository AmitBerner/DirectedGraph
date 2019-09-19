import re
import Messages as msg


def read_file(file_name: str):
    """Read given file input

        Args:
            file_name (str): file name to read

        Returns:
            list: all the rows of the file as a list
    """
    try:
        file_pointer = open(file_name, "r")
    except IOError:
        print(msg.ERROR_FILE_NAME)
        exit(1)
    with file_pointer:
        rules = list(file_pointer)
    file_pointer.close()
    parsed_rules = []
    for rule in rules:
        parsed_rules.append(parse_rule(rule))
    return parsed_rules


def parse_rule(rule: str):
    """Parse a given rule

        Args:
            rule (str): rule to parse

        Returns:
            list: a rule as a parsed list
    """
    rule = rule.strip("\"\n")
    parsed_rule = re.split('"', rule)
    if len(parsed_rule) != 3:
        print(msg.ERROR_FILE_FORMAT)
        exit(1)
    return parsed_rule
