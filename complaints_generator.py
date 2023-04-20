#!/usr/bin/env python3
from missouri_hospitals_offices import mo_hospitals
from Complainer import Complainer
from secrets import choice
import sys

relationships = {
    "medical" : ["doctor", "physician", "nurse practitioner", "medical provider", "GP", "PCP"],
    "personal" : ["aunt", "uncle", "mother", "son", "daughter", "neighbor", "friend"],
    "school": ["child's teacher", "daughter's teacher", "son's principal", "daughter's principal", "coach"]
}

# personal_actions = ["cut their daughter's hair off because she says she's a boy", "is letting their son wear dresses to school", "calling her daughter by a boy's name", "calling their son by a girl's name", "painted their son's nails", "told their daughter it was okay to use the men's restroom", "told their son they could use the women's bathroom at school"]

# words_for_guys = ["boy", "young man", "guy"]
# words_for_gals = ["girl", "young lady", "lady", "young woman"]

# school_actions = ["announced that they're allowing transgender kids to use whatever bathroom they want", "letting children change their names for roll call", "letting boys use the girls changing room", "letting girls use the boys changing room"]
# sports = ["soccer", "lacrosse", "bowling"]
# coed_sports = ["tennis", "track", "gymnastics", "wrestling", "weightlifting", "swimming", "golf"]
# boy_sports = ["football", "baseball"]
# girl_sports = ["volleyball", "softball"]

# for sport in sports:
#     for word in words_for_guys:
#         for sport in [sports + girl_sports]:
#             school_actions.append(f"letting a {word} play on the {choice('girl', 'women')}'s {sport} team")
#         for sport in coed_sports:
#             school_actions.append(f"letting a {word} compete as a {choice('girl', 'woman')} on the {sport} team")
#     for word in words_for_gals:
#         for sport in [sports + boy_sports]:
#             school_actions.append(f"letting a {word} play on the {choice('guy', 'boy', 'men')}'s {sport} team")
#         for sport in coed_sports:
#             school_actions.append(f"letting a {word} compete as a {choice('guy', 'boy', 'men')} on the {sport} team")


medical_verbs = ["prescribed", "is prescribing", "gave", "is giving"]
medical_things = ["hormones", "estrogen", "estrogen patches", "estrodol", "testosterone", "T", "estrogen shots", "testosterone shots", "testosterone jelly"]

where = ["my"]
for person in relationships["personal"]:
    where.append(f"{person}")

medical_locations = ["practice", "hospital", "office", "clinic"]

def hatespeech_complaint_generator(num_complaints=1, relationship_type=None):
    for i in range(num_complaints) :
        print("==========================")
        Complainer().print_stats()    
        print(f"Complaint: \n\n{medical_complaint()}")
        # if relationship_type == "medical":
        #     print(medical_complaint())
        # elif relationship_type == "personal":
        #     print(personal_complaint())
        # elif relationship_type == "school":
        #     print(school_complaint())
        # else:
        #     print(random.choice([medical_complaint,personal_complaint, school_complaint]))

def medical_complaint():
    person = choice(relationships["personal"])
    physician = choice(relationships["medical"])
    verb = choice(medical_verbs)
    object = choice(medical_things)
    hospital = choice(mo_hospitals)
    personal_details = Complainer()
    location = choice(medical_locations)
    county = personal_details.address["county"]

    option1 = f"My {person}'s {physician} {verb} {object} {choice([' to them', ' to some of their patients', ' to children', 'to teenagers', 'to kids over 12', ''])}. I am {choice(['worried about', 'concerned about', 'questioning', 'horrified by'])} the {choice(['longterm damage', 'ethical considerations', 'disregarding of parental wishes', 'legality'])} {choice(['in that decision', 'of this', 'of the policy at this hospital'])}. The {physician} {choice(['practices at','works at', 'is employed at', 'is employed by'])} {hospital}."
    option2 = f"A {physician} named {personal_details.first_name} {personal_details.last_name} at {hospital} {choice(['asked me for my pronouns', 'asked what my pronouns were', 'offered ' + choice(['me', f'my {person}']) + ' gender affirming care'])}. This was {choice(['deeply unsettling', 'so unprofessional of them', 'really uncomfortable for me'])} and is {choice(['a violation of the Missouri Constitution', 'against the law', 'not okay', 'horrible to do', 'inappropriate'])}."
    option3 = f"My {person}'s {physician}{choice([(' at ' + hospital), (' (' + hospital + ')'), (' ('+ personal_details.first_name + ' ' + personal_details.last_name + ')'), ''])} {choice(['confessed to', 'told', 'said', 'informed'])} them that the {location} {verb} {object} to {choice(['autistic adults who claim to be trans', 'teenagers over 14', 'kids under 16', 'children who have been diagnosed with depression', 'depressed adults', 'teenage boys with autism', 'autistic kids'])}. {choice([f'I have reported it to {county} County but no one has gotten back to us.', (f'My {person} is ' + choice(['worried about', 'concerned about', 'questioning', 'horrified by']) + ' the ' + choice(['longterm damage', 'ethical considerations']) + ' of ' + choice(['these medical interventions', 'this policy']) + choice(['.', ' and so am I.']))])}"
    option4 = f"My {person} {personal_details.first_name} {personal_details.last_name}'s {physician}{choice(['', ' (who works at ' + hospital + ')'])} asked them at their last appointment if they wanted {object}. " + choice(["I didn't know where else to report it, but I'm worried.", ('My ' + person + ' would never take ' + object + '. I don\'t know why they asked.'), 'That\'s against the new law, isn\'t it?'])

    return(choice([option1, option2, option3, option4]))


hatespeech_complaint_generator(int(sys.argv[1]))



