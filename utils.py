def capitalize_first_letter(phrase):
    phrase_words = phrase.split()
    capitalized_phrase = phrase_words[0][0].upper() + phrase_words[0][1:]
    for w in phrase_words[1:]:
        capitalized_phrase += f" {w}"
    return capitalized_phrase