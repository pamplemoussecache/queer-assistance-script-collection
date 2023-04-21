#!/usr/bin/env python3
import sys
from collections import defaultdict
from random import sample
from secrets import choice

from data_sets import MO_HOSPITALS, MO_SCHOOLS, verbs, school_classes, sports, sports_descriptors, words_for_guys, words_for_girls, sport_action_verbs, mood_words, persons, locations, opinion_words

from Person import Person

class WordBank:
    def __init__(self):
        #self.complainer = Person()
        #self.child = Person("child")
        #self.target = Person()
        self.location = self.get_location(choice(["medical", "school"]))
        self.action = choice(verbs["action"])
        self.school_class = choice(school_classes)
        self.sport = choice(sports)
        self.sports_descriptor = choice(sports_descriptors["generic"])
        self.school_class = choice(school_classes)
        self.verb_phrase = choice(verbs[choice(["action", "communication"])])
        self.guy = choice(words_for_guys)
        self.girl = choice(words_for_girls)
        self.sport_action_verb = choice(sport_action_verbs)

    def get_mood_word(self):
        return choice(mood_words)

    def get_sports_team(self, gender=None, sport=None):
        gender = gender or choice(["male", "female"])
        sport = sport or choice(sports)
        gendered_adj = choice(sports_descriptors[gender])
        adj = choice([f" {s_d} " for s_d in sports_descriptors["generic"]] + [" "])

        return f"{gendered_adj}{adj}{sport} team"

    def get_person(self, category=None):
        if category == None:
            category = choice(category)
        return choice(persons[category])

    def get_location(self, category):
        return choice(locations[category])

    def get_verb(self, type_of_verb):
        return choice(verbs[type_of_verb])

    def get_stance(self):
        return choice(opinion_words)

    def get_specific_location(self, location):
        return choice(MO_HOSPITALS if location == "hospital" else MO_SCHOOLS)
