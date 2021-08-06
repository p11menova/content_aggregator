import datetime as dt
from const import FORMAT_FROM, FORMAT_TO


def convert_to_correct_format(elem,
                              format_from=FORMAT_FROM,
                              format_to=FORMAT_TO) -> str:
    return dt.datetime.strptime(elem, format_from).strftime(format_to)

