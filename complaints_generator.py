#!/usr/bin/env python3
from missouri_data import mo_hospitals, mo_schools
from Complainer import Complainer
from secrets import choice
import sys

relationships = {
    "medical" : ["doctor", "physician", "nurse practitioner", "medical provider", "GP", "PCP"],
    "personal" : ["aunt", "uncle", "cousin", "collegue", "coworker", "boss", "son", "daughter", "neighbor", "friend"],
    "school": ["teacher", "art teacher", "science teacher", "math teacher", "history teacher", "econ teacher", "chemistry teacher", "chem teacher", "principal", "coach"]
}

words_for_guys = ["boy", "young man", "guy"]
words_for_gals = ["girl", "young lady", "lady", "young woman"]

medical_verbs = ["prescribed", "is prescribing", "gave", "is giving"]
medical_things = ["hormones", "estrogen", "estrogen patches", "estrodol", "testosterone", "T", "estrogen shots", "testosterone shots", "testosterone jelly"]

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
    school_actions = ["announced that they're allowing transgender kids to use whatever bathroom they want", "is telling children they can change their name for roll call to affirm their gender", "is letting boys use the girls changing room", "is allowing girls to use the boys changing room"]
    sports = ["soccer", "lacrosse", "bowling"]
    coed_sports = ["tennis", "track", "gymnastics", "wrestling", "weightlifting", "swimming", "golf"]
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



