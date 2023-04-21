#!/usr/bin/env python3
from data_sets.missouri_data import mo_hospitals, mo_schools
from Person import Person
from secrets import choice
import sys

relationships = {
    "medical" : ["doctor", "physician", "nurse practitioner", "medical provider", "GP", "PCP"],
    "personal" : ["aunt", "uncle", "cousin", "collegue", "coworker", "boss", "son", "daughter", "neighbor", "friend"],
    "school": ["teacher", "art teacher", "science teacher", "math teacher", "history teacher", "econ teacher", "chemistry teacher", "chem teacher", "principal", "coach"]
}

medical_verbs = ["prescribed", "is prescribing", "gave", "is giving"]
medical_things = ["hormones", "estrogen", "estrogen patches", "estrodol", "testosterone", "T", "estrogen shots", "testosterone shots", "testosterone jelly"]

verbs = ["skydive", "scuba dive", "bungee jump", "learn to surf", "climb a mountain", "go zorbing", "take a trapeze class", "take a survival course", "do acroyoga", "learn archery", "take a fencing class", "try parkour", "learn circus arts", "go horseback riding", "learn to juggle", "try paddleboarding", "do tai chi", "take a yoga class", "try aerial silks", "watch TV shows", "play video games", "read comics", "build a sandcastle", "knit a scarf", "write love letters", "try new foods", "explore a city", "attend concerts", "play board games", "watch movies", "write poetry", "attend a stand-up comedy show", "solve puzzles", "paint by numbers", "listen to music", "build with Lego bricks", "collect stamps", "play with slime", "make balloon animals", "participate in a flash mob", "collect rocks", "build the Statue of Liberty with lincoln logs"]
school_classes = ["math", "science", "biology", "physics", "chemistry", "earth science", "environmental science", "zoology", "botany", "anatomy", "physiology", "genetics", "ecology", "meteorology", "oceanography", "geology", "astronomy", "statistics", "calculus", "algebra", "geometry", "trigonometry", "differential equations", "economics", "macroeconomics", "microeconomics", "history", "geography", "world history", "US history", "government", "political science", "psychology", "sociology", "anthropology", "philosophy", "English literature", "creative writing", "French", "linguistics", "computer science", "PE"]
sports = ["bobsledding", "synchronized swimming", "dragon boat racing", "water polo", "mountain biking", "snowboarding", "archery", "wingsuit flying", "ice climbing", "extreme ironing", "yachting", "sailing", "powerlifting", "strongman", "dodgeball", "spearfishing", "wakeboarding", "kitesurfing", "flyboarding", "parkour", "rock climbing", "obstacle course racing", "roller derby", "underwater hockey", "sled dog racing"]
sports_descriptors = {
    "male": ["boy's", "boys", "boys'", "men's", "mens", "guys', 'guys's, 'guys'"],
    "female": ["girls'", "girl's", "girls", "women's", "womens", "ladies", "ladys", "ladies'", "ladies's"],
    "generic": ["competitive", "varsity", "junior varsity"]}
words_for_guys = ["boy", "young man", "guy"]
words_for_girls = ["girl", "young lady", "lady", "young woman"]
sport_action_verbs = ["play", "compete", "participate"]
mood_words = ["worried", "excited", "afraid", "angry", "concerned", "ecstatic", "devastated", "furious", "terrified", "elated", "enraged", "overjoyed", "heartbroken", "livid", "petrified", "thrilled", "indignant", "horrified", "exhilarated", "despairing", "incensed"]
    
class WordBank :
    def __init__(self):
        child = Person()
        authority = Person()
        verb = choice(verbs)
        school_class = choice(school_classes)
        sport = choice(sports)
        sports_descriptor = choice(sports_descriptors)
        school_class = choice(school_classes)
        verb_phrase = choice(verbs)
        guy = choice(words_for_guys)
        girl = choice(words_for_girls)
        sport_action_verb = choice(sport_action_verbs)

    def get_mood_word():
        return choice(mood_words)
    
    def get_sports_team(gender=choice(["male", "female"]), sport=choice(sports)):
        gendered_adj = choice(sports_descriptors[gender])
        adj = choice(f" {sports_descriptors['generic']} " + [" "])

        return f"{gendered_adj}{adj}{sport} team"


def gen_school_predicate(w=WordBank()):
    sentence_fragments = [
        f"announced that they're allowing transgender kids {w.verb} to as a {w.school_class} credit",
        f"is allowing a {w.guy} to {w.sport_action_verb} on the {w.get_sports_team('female')}",
        f"is letting a {w.guy} {w.sport_action_verb} on the {w.get_sports_team('female')}",
        f"is allowing a {w.girl} to {w.sport_action_verb} on the {w.get_sports_team('male')}",
        f"is letting a {w.girl} {w.sport_action_verb} on the {w.get_sports_team('male')}",
    ]
    return choice(sentence_fragments)

def outrage_clause(w=WordBank()):
    sentence_fragments = [
        f"and I'm {w.get_mood_word()}{choice([' and {w.get_mood_word()', ''])})"
    ]

where = ["my"]
for person in relationships["personal"]:
    where.append(f"{person}")

medical_locations = ["practice", "hospital", "office", "clinic"]

def hatespeech_complaint_generator(num_complaints=1):
    for i in range(num_complaints) :
        print("==========================")
        Complainer().print_stats()    
        print(f"Complaint: \n")
        print(choice([medical_complaint, school_complaint])())

def medical_complaint():
    person = choice(relationships["personal"])
    physician = choice(relationships["medical"])
    verb = choice(medical_verbs)
    object = choice(medical_things)
    hospital = choice(mo_hospitals)
    personal_details = Complainer()
    location = choice(medical_locations)
    county = personal_details.address["county"]

    option1 = f"My {person}'s {physician} {verb} {object}{choice([' to them', ' to some of their patients', ' to children', 'to teenagers', 'to kids over 12', ''])}. I am {choice(['worried about', 'concerned about', 'questioning', 'horrified by'])} the {choice(['longterm damage', 'ethical considerations', 'disregarding of parental wishes', 'legality'])} {choice(['in that decision', 'of this', 'of the policy at this hospital'])}. The {physician} {choice(['practices at','works at', 'is employed at', 'is employed by'])} {hospital}."
    option2 = f"A {physician} named {personal_details.first_name} {personal_details.last_name} at {hospital} {choice(['asked me for my pronouns', 'asked what my pronouns were', 'offered ' + choice(['me', f'my {person}']) + ' gender affirming care'])}. This was {choice(['deeply unsettling', 'so unprofessional of them', 'really uncomfortable for me'])} and is {choice(['a violation of the Missouri Constitution', 'against the law', 'not okay', 'horrible to do', 'inappropriate'])}."
    option3 = f"My {person}'s {physician}{choice([(' at ' + hospital), (' (' + hospital + ')'), (' ('+ personal_details.first_name + ' ' + personal_details.last_name + ')'), ''])} {choice(['confessed to', 'told', 'said', 'informed'])} them that the {location} {verb} {object} to {choice(['autistic adults who claim to be trans', 'teenagers over 14', 'kids under 16', 'children who have been diagnosed with depression', 'depressed adults', 'teenage boys with autism', 'autistic kids'])}. {choice([f'I have reported it to {county} County but no one has gotten back to us.', (f'My {person} is ' + choice(['worried about', 'concerned about', 'questioning', 'horrified by']) + ' the ' + choice(['longterm damage', 'ethical considerations']) + ' of ' + choice(['these medical interventions', 'this policy']) + choice(['.', ' and so am I.']))])}"
    option4 = f"My {person} {personal_details.first_name} {personal_details.last_name}'s {physician}{choice(['', ' (who works at ' + hospital + ')'])} asked them at their last appointment if they wanted {object}. " + choice(["I didn't know where else to report it, but I'm worried.", ('My ' + person + ' would never take ' + object + '. I don\'t know why they asked.'), 'That\'s against the new law, isn\'t it?'])

    return(choice([option1, option2, option3, option4]))

def school_complaint():
    school_actions = [f"announced that they're allowing transgender kids to {choice(sports_verbs)} as a PE credit", "is telling children they can change their name for roll call to affirm their gender", "is letting boys use the girls changing room", "is allowing girls to use the boys changing room"]
    sports = ["soccer", "lacrosse", "bowling"]
    coed_sports = ["mountain boarding", "parcour", "gymnastics", "wrestling", "weightlifting", "swimming", "golf"]
    boy_sports = ["football", "baseball"]
    girl_sports = ["volleyball", "softball"]
    personA = Complainer()
    personB = Complainer()
    county = personA.address["county"]

    for sport in sports:
        for word in words_for_guys:
            for sport in (sports + girl_sports):
                school_actions.append(f"is allowing a {word} play on the {choice(['girl', 'women'])}'s {sport} team")
            for sport in coed_sports:
                school_actions.append(f"is letting a {word} compete as a {choice(['girl', 'woman'])} on the {sport} team")
        for word in words_for_gals:
            for sport in (sports + boy_sports):
                school_actions.append(f"is letting a {word} play on the {choice(['guy', 'boy', 'men'])}'s {sport} team")
            for sport in coed_sports:
                school_actions.append(f"is allowing a {word} compete as a {choice(['guy', 'boy', 'men'])} on the {sport} team")

    person = choice(["son", "daughter", "neighbor's kid", "neighbour's daughter", "neighbor's son", "friend's son", "friend's kid"])
    teacher = choice(relationships["school"])
    action = choice(school_actions)
    school = choice(mo_schools)

    return f"My {person}'s" + choice(['', ' (' + personA.first_name + " " + personA.last_name + ')']) + f" {teacher}" + choice(['', ' (' + personB.first_name + " " + personB.last_name + ')']) + f" {action}. My {person} {choice(['goes to', 'attends'])} {school}{choice(['', ' in '+ county +' County'])}."


hatespeech_complaint_generator(int(sys.argv[1]))



