def count_words(string):
    return len(string.split())


def num_of_characters(string):
    character_dict = {}

    for character in string:
        lower = character.lower()

        if lower in character_dict:
            character_dict[lower] += 1
        else:
            character_dict[lower] = 1

    return character_dict
