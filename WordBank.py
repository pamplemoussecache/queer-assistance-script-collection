#!/usr/bin/env python3
import sys
from random import sample
from secrets import choice
from collections import defaultdict

from data_sets import (
    MO_HOSPITALS, 
    MO_SCHOOLS, 
)   
from Person import Person

categories = ["medical", "school"]

medical_verbs = ["prescribed", "is prescribing", "gave", "is giving"]
medical_things = [
    "hormones",
    "estrogen",
    "estrogen patches",
    "estrodol",
    "testosterone",
    "T",
    "estrogen shots",
    "testosterone shots",
    "testosterone jelly",
]

locations = {
    "medical": ["practice", "hospital", "office", "clinic"],
    "school": ["school", "class", "school system", "high school"],
}
for category in locations:
    for location in category:
        data_set = MO_HOSPITALS if location == "hospital" else MO_SCHOOLS
        locations[category].append(f"{location} ({choice(data_set)})")


communication_verbs = ["told", "confessed", "said", "informed", "reported", "mentioned"]

school_classes = [
    "math",
    "science",
    "biology",
    "physics",
    "chemistry",
    "earth science",
    "environmental science",
    "zoology",
    "botany",
    "anatomy",
    "physiology",
    "genetics",
    "ecology",
    "meteorology",
    "oceanography",
    "geology",
    "astronomy",
    "statistics",
    "calculus",
    "algebra",
    "geometry",
    "trigonometry",
    "differential equations",
    "economics",
    "macroeconomics",
    "microeconomics",
    "history",
    "geography",
    "world history",
    "US history",
    "government",
    "political science",
    "psychology",
    "sociology",
    "anthropology",
    "philosophy",
    "English literature",
    "creative writing",
    "French",
    "linguistics",
    "computer science",
    "PE",
]

sports = [
    "bobsledding",
    "synchronized swimming",
    "dragon boat racing",
    "water polo",
    "mountain biking",
    "snowboarding",
    "archery",
    "wingsuit flying",
    "ice climbing",
    "extreme ironing",
    "yachting",
    "sailing",
    "powerlifting",
    "strongman",
    "dodgeball",
    "spearfishing",
    "wakeboarding",
    "kitesurfing",
    "flyboarding",
    "parkour",
    "rock climbing",
    "obstacle course racing",
    "roller derby",
    "underwater hockey",
    "sled dog racing",
]
sports_descriptors = {
    "male": ["boy's", "boys", "boys'", "men's", "mens", "guys', 'guys's, 'guys'"],
    "female": [
        "girls'",
        "girl's",
        "girls",
        "women's",
        "womens",
        "ladies",
        "ladys",
        "ladies'",
        "ladies's",
    ],
    "generic": ["competitive", "varsity", "junior varsity"],
}
sport_action_verbs = ["play", "compete", "participate"]

person = defaultdict(list)
for school_class in sample(list(school_classes), 5):
    person["school"].append(f"{school_class} teacher")


words_for_guys = ["boy", "young man", "guy"]
words_for_girls = ["girl", "young lady", "lady", "young woman"]

mood_words = [
    "worried",
    "excited",
    "afraid",
    "angry",
    "concerned",
    "ecstatic",
    "devastated",
    "furious",
    "terrified",
    "elated",
    "enraged",
    "overjoyed",
    "heartbroken",
    "livid",
    "petrified",
    "thrilled",
    "indignant",
    "horrified",
    "exhilarated",
    "despairing",
    "incensed",
]

opinion_words = ["against", "in support of"]

persons = {
    "medical": [
        "patient",
        "doctor",
        "physician",
        "nurse practitioner",
        "medical provider",
        "GP",
        "PCP",
    ],
    "school": [
        "student",
        "teacher",
        "administrator",
        "principal",
        "teaching aid",
        "school nurse",
    ],
    "child": [
        "son",
        "daughter",
        "kid",
        "child",
        "nephew",
        "niece",
        "nibling",
        "granddaughter",
        "grandchild",
        "grandson",
    ],
    "community": [
        "neighbor",
        "pastor",
        "teacher",
        "coach",
        "cousin",
        "aunt",
        "uncle",
        "babysitter",
        "dentist",
        "doctor",
        "barber",
        "hairdresser",
        "tutor",
        "music teacher",
        "dance instructor",
        "coworker",
        "boss",
    ],
}
# TODO: Fix
# for category in persons:
#     for person in category:
#         persons[category].append(
#             f"the {person} of my {choice(persons['community'])}"
#         )
#         persons[category].append(f"my {choice(choice(persons))}'s {person}")

verbs = {
    "action": [
        "skydive",
        "scuba dive",
        "bungee jump",
        "learn to surf",
        "climb a mountain",
        "go zorbing",
        "take a trapeze class",
        "take a survival course",
        "do acroyoga",
        "learn archery",
        "take a fencing class",
        "try parkour",
        "learn circus arts",
        "go horseback riding",
        "learn to juggle",
        "try paddleboarding",
        "do tai chi",
        "take a yoga class",
        "try aerial silks",
        "watch TV shows",
        "play video games",
        "read comics",
        "build a sandcastle",
        "knit a scarf",
        "write love letters",
        "try new foods",
        "explore a city",
        "attend concerts",
        "play board games",
        "watch movies",
        "write poetry",
        "attend a stand-up comedy show",
        "solve puzzles",
        "paint by numbers",
        "listen to music",
        "build with Lego bricks",
        "collect stamps",
        "play with slime",
        "make balloon animals",
        "participate in a flash mob",
        "collect rocks",
        "build the Statue of Liberty with lincoln logs",
    ],
    "communication": [
        "told",
        "confessed to",
        "said",
        "informed",
        "reported to",
        "mentioned to",
        "shared with",
    ],
}

class WordBank:
    def __init__(self):
        self.complainer = Person()
        self.child = Person("child")
        self.target = Person()
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
        adj = choice(
            [f" {s_d} " for s_d in sports_descriptors['generic']] + [" "]
        )   

        return f"{gendered_adj}{adj}{sport} team"

    def get_person(self, category):
        return choice(persons[category])

    def get_location(self, category):
        return choice(locations[category])

    def get_verb(self, type_of_verb):
        return choice(verbs[type_of_verb])

    def get_stance(self):
        return choice(opinion_words)
