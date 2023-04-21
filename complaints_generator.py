#!/usr/bin/env python3
from random import randint, sample
from secrets import choice

from data_sets import MO_HOSPITALS, MO_SCHOOLS, NCTE_MO_STATE_REPORT, STATES_OF_DENIAL
from Person import Person
from WordBank import WordBank, categories, location, person


def capitalize_first_letter(phrase):
    phrase_words = phrase.split()
    capitalized_phrase = phrase_words[0].title()
    for w in phrase_words[1:]:
        capitalized_phrase += f" {w}"
    return capitalized_phrase


class Complaint:
    def __init__(self, category=None, num_sentences=None):
        self.w = WordBank()
        self.complaint = ""
        self.num_sentences = num_sentences or randint(1, 4)
        self.category = category or choice(categories)
        self.child = "my child"  # TODO: randomize

        for i in range(self.num_sentences):
            if self.num_sentences == 1:
                self.complaint += capitalize_first_letter(self.get_punchy_sentence())
            elif i == 0:
                self.complaint += capitalize_first_letter(self.get_starting_sentence())
            # TODO: Write
            # elif i == (self.num_sentences - 1):
            #     self.complaint += self.get_ending_sentence()
            else:
                self.complaint += capitalize_first_letter(self.get_sentence())

    def __str__(self):
        return f"{self.complaint}"

    def get_mood_fragment(self):
        w = self.w
        second_mood = f" and {w.get_mood_word()}"
        return (
            choice(["I am", "I'm"]) + f" {w.get_mood_word()}{choice([second_mood, ''])}"
        )

    def get_school_predicate(self):
        w = self.w
        sentence_fragments = [
            f"announced that they're allowing transgender kids {w.action} to as a {w.school_class} credit",
            f"is allowing a {w.guy} to {w.sport_action_verb} on the {w.get_sports_team('female')}",
            f"is letting a {w.guy} {w.sport_action_verb} on the {w.get_sports_team('female')}",
            f"is allowing a {w.girl} to {w.sport_action_verb} on the {w.get_sports_team('male')}",
            f"is letting a {w.girl} {w.sport_action_verb} on the {w.get_sports_team('male')}",
            f"is telling students that they can grow up to become professional {choice([w.get_person('community'), w.get_person('school'), w.get_person('medical')])}s",
        ]
        return choice(sentence_fragments)

    def get_effect_fragment(self, category=None):
        category = category or choice(["school", "medical"])
        w = self.w
        sentence_fragments = [
            f"about the level of communication between staff and parents",
            f"about the lack of diversity in the {w.get_location(category)}'s curriculum",
            f"about the accessibility of the {w.get_location(category)}'s facilities",
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
            f'at the thought of {w.get_person(category)}s not receiving proper {"instructional" if category == "school" else "medical"} attention',
            f"at the thought of outdated equipment and technology at the school",
            f"by the lack of transparency in decision-making processes at the {w.get_location(category)}",
            f"by the potential dangers of instituting this policy given the limited access to mental health resources at the {w.get_location(category)}",
            f"at the thought of insufficient training for staff members",
            f"at the thought of inadequate facilities for {w.get_person(category)}s",
            f"by the lack of diversity and inclusivity at the {w.get_location(category)}",
            f"at the thought of resulting bullying and harassment from {w.get_person(category)}s potentially going unaddressed",
            f'at the thought of budget cuts affecting quality of {"education" if category == "school" else "care"}',
            f"at the thought of inadequate accommodations for {w.get_person(category)}s with disabilities",
            f"at the prospect of a high {w.get_person(category)} turnover rate at the {w.get_location(category)} as a result",
        ]
        return choice(sentence_fragments)

    def get_starting_sentence(self):
        w = self.w
        communicated_to = w.get_verb("communication")
        child = self.child
        community_member = w.get_person("community")
        target = w.get_person("school")
        action = self.get_school_predicate()
        i_feel = self.get_mood_fragment()
        about_effects = self.get_effect_fragment("school")

        options = [
            f"{child} {communicated_to} me that their {target} {action}.",
            f"{child} {communicated_to} me that their {target} {action} and {i_feel}.",
            f"{child} {communicated_to} me that their {target} {action} and {i_feel} {about_effects}.",
            f"{i_feel} because my {community_member} told me that {child}'s {target} {action}.",
            f"{i_feel} because {child} {communicated_to} me that the {target} {action}.",
        ]
        return choice(options)

    def get_sentence(self):
        w = self.w
        communicated_to = w.get_verb("communication")
        child = self.child
        community_member = w.get_person("community")
        target = choice([w.get_person("school"), w.get_location("school")])
        action = self.get_school_predicate()
        i_feel = self.get_mood_fragment()
        about_effects = self.get_effect_fragment("school")
        opinion = w.get_stance()

        options = [
            f" Also, {i_feel} that the Attorney General's office isn't taking a stronger stance {opinion} {target} doing this kind of thing.",
            f" I emailed {target} about my feelings but they were unresponsive.",
            f" We the parents of this community are {w.get_mood_word()} about the lack of oversight from the {w.get_person('school')}.",
            f" Is it even legal for {target}s to make that decision without consulting the parents?",
            f" The {target} also {self.get_effect_fragment('school')}.",
        ]
        return choice(options)

    def get_punchy_sentence(self):
        w = self.w
        sentences = (
            [
                f" Did you know that {choice(NCTE_MO_STATE_REPORT)}?",
                f" I expect your call at {w.complainer.phone_number}.",
                f" What is the Missouri government going to do about the fact that?",
                f" This is a violation of the Missouri state law and I will not stand for it.",
                f" I can't believe that our government is standing for this.",
            ]
            + NCTE_MO_STATE_REPORT
            + STATES_OF_DENIAL
        )
        return choice(sentences)


print(Complaint())
