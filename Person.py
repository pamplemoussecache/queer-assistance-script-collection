#!/usr/bin/env python3
import csv
from secrets import choice
from random import randint
from json import dumps

import names
import random_address

from WordBank import WordBank
from data_sets.words import categories, states


def make_email(first_name, last_name):
    email_endings = ["@hotmail.com", "@yahoo.com", "@gmail.com", "@aol.com"]
    email_end = choice(email_endings)

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

    return assembled_email.lower()


def make_phone_number(state="MO"):
    area_codes = {
        "MO": ["314", "557", "417", "573", "636", "660", "816"],
        "KS": ["316", "620", "785", "913"],
        "NE": ["308", "402", "531"],
        "IA": ["319", "515", "563", "641", "712"],
        "WI": ["262", "274", "414", "353", "608", "715", "534", "920"],
    }

    phone_number = choice(area_codes[state])

    for i in range(7):
        phone_number += str(randint(0, 9))

    return phone_number


missouri_data = list(
    csv.DictReader(open("data_sets/Missouri_Zip_Codes_by_County_City.csv"))
)


class Person:
    def __init__(self, role_type="", referring_pronoun="my"):
        self.word_bank = WordBank()
        self.first_name = names.get_first_name()
        self.last_name = names.get_last_name()
        self.address = {
            "street": random_address.real_random_address()["address1"]
        } | choice(missouri_data)
        self.email = make_email(self.first_name, self.last_name)
        self.phone_number = choice(["", make_phone_number(choice(states))])
        self.role = self.assign_role(role_type, referring_pronoun)
        self.referring_pronoun = referring_pronoun

    def assign_role(self, role_type, referring_word="my"):
        role_type = role_type or choice(categories)
        word_bank = self.word_bank
        
        optionA = f"{referring_word}"
        optionB = f"the {word_bank.get_person(role_type)}"
        
        for i in range(randint(0,3)):
            optionA += f" {word_bank.get_person()}'s"
            if (i > 0):
                optionB += f" of the {word_bank.get_person()}"
        
        optionA += f" {word_bank.get_person(role_type)}"
        optionB += f" of {referring_word} {word_bank.get_person(role_type)}"

        return choice([optionA, optionB])
    
    def to_json(self):
        p = {"first_name": self.first_name, "last_name": self.last_name, "address": dumps(self.address), "email": self.email, "phone_number": self.phone_number}
        return p

    def print_stats(self):
        print(f"First name: {self.first_name}\n")
        print(f"Last name: {self.last_name}\n")
        print(f"Address: {self.address['street']}\n")
        print(f"City: {self.address['city']}\n")
        print(f"State: MO\n")
        print(f"Zip code: {self.address['zip code']}\n")
        print(f"email address: {make_email(self.first_name, self.last_name).lower()}\n")
        print(f"phone number: {make_phone_number()}\n")
        print(f"role: {self.role}")
