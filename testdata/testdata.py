import random
import pathlib
from pathlib import Path


class User1:
    email = "randomemail" + str(random.randint(111, 1111)) + "@gmail.com"
    first_name = "Abra"
    last_name = "Cadabra"
    password = "QwErTyUi"
    birth_year = "1997"
    address = "Address"
    city = "City"
    postcode = "23455"
    country = "United States"
    phone = "2345678"


class ContactUsData:
    file_path = str(Path(pathlib.Path.cwd() / 'testdata' / 'ContactUs form.txt'))
    subject_heading = "Customer service"
    email = "hello@gmail.com"
    order = "12345678"
    message = "Some message, abracadabra"


if __name__ == '__main__':
    print(str(Path(pathlib.Path.cwd())))
