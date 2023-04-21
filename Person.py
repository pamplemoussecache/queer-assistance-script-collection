#!/usr/bin/env python3
import csv
import secrets
from random import randint

import names
import random_address

states = ["MO", "KS", "NE", "IA", "WI"]


def make_email(first_name, last_name):
    email_endings = ["@hotmail.com", "@yahoo.com", "@gmail.com", "@aol.com"]
    email_end = secrets.choice(email_endings)

    assembled_email = ""

    pick_email_method = randint(0, 4)
    if pick_email_method == 0:
        assembled_email = first_name[0] + last_name + email_end
    elif pick_email_method == 1:
        assembled_email = first_name + "." + last_name + email_end
    elif pick_email_method == 2:
        assembled_email = first_name + last_name + email_end
    else:
        assembled_email = first_name + last_name + str(randint(0, 9)) + email_end

    return assembled_email


def make_phone_number(state="MO"):
    area_codes = {
        "MO": ["314", "557", "417", "573", "636", "660", "816"],
        "KS": ["316", "620", "785", "913"],
        "NE": ["308", "402", "531"],
        "IA": ["319", "515", "563", "641", "712"],
        "WI": ["262", "274", "414", "353", "608", "715", "534", "920"],
    }

    phone_number = secrets.choice(area_codes[state])

    for i in range(7):
        phone_number += str(randint(0, 9))

    return phone_number


missouri_data = list(
    csv.DictReader(open("data_sets/Missouri_Zip_Codes_by_County_City.csv"))
)


class Person:
    def __init__(self, role=None):
        self.first_name = names.get_first_name()
        self.last_name = names.get_last_name()
        self.address = {
            "street": random_address.real_random_address()["address1"]
        } | secrets.choice(missouri_data)
        self.email = make_email(self.first_name, self.last_name)
        self.phone_number = make_phone_number(secrets.choice(states))
        self.role = None  # TODO fix this

    def print_stats(self):
        print(f"First name: {self.first_name}\n")
        print(f"Last name: {self.last_name}\n")
        print(f"Address: {self.address['street']}\n")
        print(f"City: {self.address['city']}\n")
        print(f"State: MO\n")
        print(f"Zip code: {self.address['zip code']}\n")
        print(f"email address: {make_email(self.first_name, self.last_name).lower()}\n")
        print(f"phone number: {make_phone_number()}\n")
