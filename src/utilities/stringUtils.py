import re


def replace_locator_placeholders(locator: str, value_list: list):
    from src.constants import TestConstants
    match = re.findall(TestConstants.LOCATOR_PLACEHOLDER_PATTERN, locator)
    for i in range(len(match)):
        locator = locator.replace(match[i], value_list[i])
    return locator


def get_clean_phone_number(phone_number: str):
    for c in ["(", ")", "-"]:
        phone_number = phone_number.replace(c, "")
    return phone_number
