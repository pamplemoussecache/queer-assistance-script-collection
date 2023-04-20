
#!/usr/bin/env python3
from data_sets import mo_schools, mo_hospitals, states_of_denial, ncte_mo_state_report,
from Person import Person
from secrets import choice
from random import sample
import sys

categories = ["medical", "school"]

medical_verbs = ["prescribed", "is prescribing", "gave", "is giving"]
medical_things = ["hormones", "estrogen", "estrogen patches", "estrodol", "testosterone", "T", "estrogen shots", "testosterone shots", "testosterone jelly"]

locations = {"medical" : ["practice", "hospital", "office", "clinic"],
             "school": ["school", "class", "school system", "high school"]
}
for category in locations:
    for location in category:
        data_set = mo_hospitals if location == "hospital" else mo_schools
        locations[category].append(f"{location} ({choice(data_set)})")


communication_verbs = ["told", "confessed", 'said', 'informed', "reported", "mentioned"]

school_classes = ["math", "science", "biology", "physics", "chemistry", "earth science", "environmental science", "zoology", "botany", "anatomy", "physiology", "genetics", "ecology", "meteorology", "oceanography", "geology", "astronomy", "statistics", "calculus", "algebra", "geometry", "trigonometry", "differential equations", "economics", "macroeconomics", "microeconomics", "history", "geography", "world history", "US history", "government", "political science", "psychology", "sociology", "anthropology", "philosophy", "English literature", "creative writing", "French", "linguistics", "computer science", "PE"]

sports = ["bobsledding", "synchronized swimming", "dragon boat racing", "water polo", "mountain biking", "snowboarding", "archery", "wingsuit flying", "ice climbing", "extreme ironing", "yachting", "sailing", "powerlifting", "strongman", "dodgeball", "spearfishing", "wakeboarding", "kitesurfing", "flyboarding", "parkour", "rock climbing", "obstacle course racing", "roller derby", "underwater hockey", "sled dog racing"]
sports_descriptors = {
    "male": ["boy's", "boys", "boys'", "men's", "mens", "guys', 'guys's, 'guys'"],
    "female": ["girls'", "girl's", "girls", "women's", "womens", "ladies", "ladys", "ladies'", "ladies's"],
    "generic": ["competitive", "varsity", "junior varsity"]}
sport_action_verbs = ["play", "compete", "participate"]

for school_class in sample(list(school_classes), 5):
    person["school"].append(f"{school_class} teacher")


words_for_guys = ["boy", "young man", "guy"]
words_for_girls = ["girl", "young lady", "lady", "young woman"]

mood_words = ["worried", "excited", "afraid", "angry", "concerned", "ecstatic", "devastated", "furious", "terrified", "elated", "enraged", "overjoyed", "heartbroken", "livid", "petrified", "thrilled", "indignant", "horrified", "exhilarated", "despairing", "incensed"]



class WordBank :
    def __init__(self):
        complainer = Person()
        child = Person("child")
        target = Person()
        location = self.get_location()
        action = choice(verbs)
        school_class = choice(school_classes)
        sport = choice(sports)
        sports_descriptor = choice(sports_descriptors)
        school_class = choice(school_classes)
        verb_phrase = choice(verbs)
        guy = choice(words_for_guys)
        girl = choice(words_for_girls)
        sport_action_verb = choice(sport_action_verbs)
    
    opinion_words = ["against", "in support of"]
    
    persons = { 
            "medical": ["patient", "doctor", "physician", "nurse practitioner", "medical provider", "GP", "PCP"],
            "school": ["student", "teacher", "administrator", "principal", "teaching aid", "school nurse"],
            "child": ["son", "daughter", "kid", "child", "nephew", "niece", "nibling", "granddaughter", "grandchild", "grandson"],
            "community": ["neighbor", "pastor", "teacher", "coach", "cousin", "aunt", "uncle", "babysitter", "dentist", "doctor", "barber", "hairdresser", "tutor", "music teacher", "dance instructor", "coworker", "boss"]}
    for category in persons:
        for person in category:
            persons[category].append(f"the {person} of my {choice(persons['community'])}")
            persons[category].append(f"my {choice(choice(persons))}'s {person}")
    
    locations = {
        "medical" : ["practice", "hospital", "office", "clinic"],
        "school": ["school", "class", "school system", "high school"]
    }

    verbs = {
        "action": ["skydive", "scuba dive", "bungee jump", "learn to surf", "climb a mountain", "go zorbing", "take a trapeze class", "take a survival course", "do acroyoga", "learn archery", "take a fencing class", "try parkour", "learn circus arts", "go horseback riding", "learn to juggle", "try paddleboarding", "do tai chi", "take a yoga class", "try aerial silks", "watch TV shows", "play video games", "read comics", "build a sandcastle", "knit a scarf", "write love letters", "try new foods", "explore a city", "attend concerts", "play board games", "watch movies", "write poetry", "attend a stand-up comedy show", "solve puzzles", "paint by numbers", "listen to music", "build with Lego bricks", "collect stamps", "play with slime", "make balloon animals", "participate in a flash mob", "collect rocks", "build the Statue of Liberty with lincoln logs"], 
        "communication": ["told", "confessed to", 'said', 'informed', "reported to", "mentioned to", "shared with"]}
    
    def get_mood_word():
        return choice(mood_words)
    
    def get_sports_team(gender=choice(["male", "female"]), sport=choice(sports)):
        gendered_adj = choice(sports_descriptors[gender])
        adj = choice(f" {sports_descriptors['generic']} " + [" "])

        return f"{gendered_adj}{adj}{sport} team"

    def get_person(self, category):
        return choice(self.persons[category])
    
    def get_location(self, category):
        return choice(locations[category])
    
    def get_verb(self, type_of_verb):
        return choice(self.verbs[type_of_verb])
    
    def get_stance(self):
        return choice(self.opinion_words)