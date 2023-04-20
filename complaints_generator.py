#!/usr/bin/env python3
from data_sets import mo_schools, mo_hospitals, states_of_denial, ncte_mo_state_report
from Person import Person
from secrets import choice
from random import randint, sample
import sys
from WordBank import WordBank, location, person, categories

def capitalize_first_letter(word):
    return ' '.join(word[0].upper() + word[1:] for word in s.split())

class Complaint:
    def __init__(self, category=choice(categories), num_sentences=randint(1,5)):
        w = WordBank()
        complaint = ""
        category = category

        for i in range(num_sentences):
            if num_sentences == 1:
                complaint += self.get_punchy_sentence()
            elif i == 0:
                complaint += self.get_starting_sentence(category, w)
            elif i == (num_sentences - 1):
                complaint += self.get_ending_sentence(category, w)
            else:
                complaint += self.get_sentence(category, w)

    def __str__(self):
        return f"{self.complaint}"        

    def get_mood_fragment(w=WordBank()):
        return choice(['I am', 'I\'m']) + f" {w.get_mood_word()}{choice([format(' and %s',w.get_mood_word()), ''])}"
    
    def get_school_predicate(self):
        sentence_fragments = [
            f"announced that they're allowing transgender kids {w.verb} to as a {w.school_class} credit",
            f"is allowing a {w.guy} to {w.sport_action_verb} on the {w.get_sports_team('female')}",
            f"is letting a {w.guy} {w.sport_action_verb} on the {w.get_sports_team('female')}",
            f"is allowing a {w.girl} to {w.sport_action_verb} on the {w.get_sports_team('male')}",
            f"is letting a {w.girl} {w.sport_action_verb} on the {w.get_sports_team('male')}",
        ]
        return choice(sentence_fragments)
    
    def get_effect_fragment(self, category=choice(["school", "medical"])):
        w = self.w
        sentence_fragments = [
            f"about the level of communication between staff and parents",
            f"about the lack of diversity in the {w.get_location(category)}'s curriculum",
            f"about the accessibility of the {w.w.get_location(category)}'s facilities",
            f"about the level of support provided for {w.get_person(category)}s with disabilities",
            f"about the adequacy of the {w.get_location(category)}'s safety measures",
            f"about the impact of the {w.get_location(category)}'s policies on mental health",
            f"about the level of transparency in the {w.get_location(category)}'s decision-making",
            f"about the potential for discrimination by {w.get_person(category)}s at the {w.get_location(category)}",
            f"about the quality of the {w.get_location(category)}'s academic programs",
            f"about the adequacy of the {w.get_location(category)}'s technology resources",
            f"about the effectiveness of the {w.get_location(category)}'s disciplinary policies",
            f"about the level of parent involvement in the {w.get_location(category)}",
            f"about the potential for favoritism among {w.get_person(category)}s at the {w.get_location(category)}",
            f"about the level of resources provided for extracurricular activities",
            f"about the effectiveness of the {w.get_location(category)}'s counseling services",
            f"about the adequacy of the {w.get_location(category)}'s financial aid policies",
            f"about the level of support provided for non-native speakers",
            f"about the level of support provided for {w.get_person(category)}s experiencing homelessness",
            f"about the impact of the {w.get_location(category)}'s policies on {w.get_person(category)}s' mental and emotional wellbeing",
            f"about the adequacy of the {w.get_location(category)}'s training for staff on diversity and inclusion",
            f"by the lack of communication from the {w.get_location(category)} on this decision",
            f"at the thought of inadequate resources for {w.get_person(category)}s",
            f"at the idea of this increasing the amount of confusing bureaucracy at the {w.get_location(category)}",
            f"at the thought of {w.get_person(category)}s not receiving proper {'instructional' if category == "school" else "medical"} attention",
            f"at the thought of outdated equipment and technology at the school",
            f"by the lack of transparency in decision-making processes at the {w.get_location(category)}",
            f"by the potential dangers of instituting this policy given the limited access to mental health resources at the {w.get_location(category)}",
            f"at the thought of insufficient training for staff members",
            f"at the thought of inadequate facilities for {w.get_person(category)}s",
            f"by the lack of diversity and inclusivity at the {w.get_location(category)}",
            f"at the thought of resulting bullying and harassment from {w.get_person(category)}s potentially going unaddressed",
            f"at the thought of budget cuts affecting quality of {"education" if category == "school" else "care"}",
            f"at the thought of inadequate accommodations for {w.get_person(category)}s with disabilities",
            f"at the prospect of a high {w.get_person(category)} turnover rate at the {w.get_location(category)} as a result"
        ]
        return choice(sentence_fragments)

    def get_starting_sentence(self):
        w = self.w
        communicated_to = w.get_verb("communication")
        child = self.child
        community_member = w.get_person("community")
        target = choice([w.get_person('school'), w.get_location('school')])
        action = self.get_school_predicate(w)
        i_feel = self.get_mood_fragment(w)
        about_effects = self.get_effect_fragment("school")

        options = [
            f"{child} {communicated_to} me that their {target} {action}.",
            f"{child} {communicated_to} me that their {target} {action} and {i_feel}.",
            f"{child} {communicated_to} me that their {target} {action} and {i_feel} {about_effects}.",
            f"{i_feel} because my {community_member} told me that {child}'s {target} {action}.",
            f"{i_feel} because {child} {communicated_to} me that the {target} {action}."
            ]
        return choice(options)
    
    def get_sentence(self):
        w = self.w
        communicated_to = w.get_verb("communication")
        child = self.child
        target = self.target
        community_member = w.get_person("community")
        target = choice([w.get_person('school'), w.get_location('school')])
        action = self.get_school_predicate(w)
        i_feel = self.get_mood_fragment(w)
        about_effects = self.get_effect_fragment("school")
        opinion = w.get_opinion()

        options = [
            f"Also, {i_feel} that the Attorney General's office should be taking a harder stance {opinion} {target} doing this kind of thing.",
            f"I emailed {target} about my feelings but they were unresponsive.",

            f"My {child} {communicated_to} me that their {target} {action} and {i_feel}.",
            f"My {child} {communicated_to} me that their {target} {action} and {i_feel} {about_effects}.",
            f"{i_feel} because my {community_member} told me that their {child}'s {target} {action}.",
            f"{i_feel} because my {child} {communicated_to} me that their {target} {action}."
            ]
        
        return choice(options)

    def get_punchy_sentence(self):
        sentences = [
            f"Did you know that {choice(ncte_mo_state_report)}?",
            f"I expect your call at {w.complainer.phone_number}.",
            f"What is the Missouri government going to do about the fact that {}?",
            f"This is a violation of the Missouri state law and I will not stand for it.",
            f"I can't believe that our government is standing for this."
        ].append(map(capitalize_first_letter + ".", ncte_mo_state_report + states_of_denial))
        return choice(sentences)
    

# def hatespeech_complaint_generator(num_complaints=1):
#     for i in range(num_complaints) :
#         print("==========================")
#         Complainer().print_stats()    
#         print(f"Complaint: \n")
#         print(choice([medical_complaint, school_complaint])())

# def medical_complaint():
#     person = choice(relationships["personal"])
#     physician = choice(relationships["medical"])
#     verb = choice(medical_verbs)
#     object = choice(medical_things)
#     hospital = choice(mo_hospitals)
#     personal_details = Complainer()
#     location = choice(medical_locations)
#     county = personal_details.address["county"]

#     option1 = f"My {person}'s {physician} {verb} {object}{choice([' to them', ' to some of their patients', ' to children', 'to teenagers', 'to kids over 12', ''])}. I am {choice(['worried about', 'concerned about', 'questioning', 'horrified by'])} the {choice(['longterm damage', 'ethical considerations', 'disregarding of parental wishes', 'legality'])} {choice(['in that decision', 'of this', 'of the policy at this hospital'])}. The {physician} {choice(['practices at','works at', 'is employed at', 'is employed by'])} {hospital}."
#     option2 = f"A {physician} named {personal_details.first_name} {personal_details.last_name} at {hospital} {choice(['asked me for my pronouns', 'asked what my pronouns were', 'offered ' + choice(['me', f'my {person}']) + ' gender affirming care'])}. This was {choice(['deeply unsettling', 'so unprofessional of them', 'really uncomfortable for me'])} and is {choice(['a violation of the Missouri Constitution', 'against the law', 'not okay', 'horrible to do', 'inappropriate'])}."
#     option3 = f"My {person}'s {physician}{choice([(' at ' + hospital), (' (' + hospital + ')'), (' ('+ personal_details.first_name + ' ' + personal_details.last_name + ')'), ''])} {choice(['confessed to', 'told', 'said', 'informed'])} them that the {location} {verb} {object} to {choice(['autistic adults who claim to be trans', 'teenagers over 14', 'kids under 16', 'children who have been diagnosed with depression', 'depressed adults', 'teenage boys with autism', 'autistic kids'])}. {choice([f'I have reported it to {county} County but no one has gotten back to us.', (f'My {person} is ' + choice(['worried about', 'concerned about', 'questioning', 'horrified by']) + ' the ' + choice(['longterm damage', 'ethical considerations']) + ' of ' + choice(['these medical interventions', 'this policy']) + choice(['.', ' and so am I.']))])}"
#     option4 = f"My {person} {personal_details.first_name} {personal_details.last_name}'s {physician}{choice(['', ' (who works at ' + hospital + ')'])} asked them at their last appointment if they wanted {object}. " + choice(["I didn't know where else to report it, but I'm worried.", ('My ' + person + ' would never take ' + object + '. I don\'t know why they asked.'), 'That\'s against the new law, isn\'t it?'])

#     return(choice([option1, option2, option3, option4]))

# def school_complaint():
#     school_actions = [f"announced that they're allowing transgender kids to {choice(sports_verbs)} as a PE credit", "is telling children they can change their name for roll call to affirm their gender", "is letting boys use the girls changing room", "is allowing girls to use the boys changing room"]
#     sports = ["soccer", "lacrosse", "bowling"]
#     coed_sports = ["mountain boarding", "parcour", "gymnastics", "wrestling", "weightlifting", "swimming", "golf"]
#     boy_sports = ["football", "baseball"]
#     girl_sports = ["volleyball", "softball"]
#     personA = Complainer()
#     personB = Complainer()
#     county = personA.address["county"]

#     for sport in sports:
#         for word in words_for_guys:
#             for sport in (sports + girl_sports):
#                 school_actions.append(f"is allowing a {word} play on the {choice(['girl', 'women'])}'s {sport} team")
#             for sport in coed_sports:
#                 school_actions.append(f"is letting a {word} compete as a {choice(['girl', 'woman'])} on the {sport} team")
#         for word in words_for_gals:
#             for sport in (sports + boy_sports):
#                 school_actions.append(f"is letting a {word} play on the {choice(['guy', 'boy', 'men'])}'s {sport} team")
#             for sport in coed_sports:
#                 school_actions.append(f"is allowing a {word} compete as a {choice(['guy', 'boy', 'men'])} on the {sport} team")

#     person = choice(["son", "daughter", "neighbor's kid", "neighbour's daughter", "neighbor's son", "friend's son", "friend's kid"])
#     teacher = choice(relationships["school"])
#     action = choice(school_actions)
#     school = choice(mo_schools)

#     return f"My {person}'s" + choice(['', ' (' + personA.first_name + " " + personA.last_name + ')']) + f" {teacher}" + choice(['', ' (' + personB.first_name + " " + personB.last_name + ')']) + f" {action}. My {person} {choice(['goes to', 'attends'])} {school}{choice(['', ' in '+ county +' County'])}."


# hatespeech_complaint_generator(int(sys.argv[1]))



print(Complaint())