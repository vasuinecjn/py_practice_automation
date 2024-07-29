from faker import Faker

from src.utilities.stringUtils import get_clean_phone_number

f = Faker()
f.phone_number()
print(get_clean_phone_number(r"(282)702-1471"))