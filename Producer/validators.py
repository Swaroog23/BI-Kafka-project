from typing import List


def validate_strings_are_numeric(values: List[str]):
    for value in values:
        if not value.isnumeric():
            raise ValueError(f"Value must be numeric! {value}")


def validate_number_of_events(value: int):
    if 100_000 < value or value < 0:
        raise ValueError(f"Number of events must be within 100 thousand and 1! {value}")


def validate_delay(min_delay: int, max_delay: int):
    if min_delay >= max_delay:
        raise ValueError("Minimal delay cannot be bigger that max delay!")
