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


def sort_on(dict):
    for k in dict:
        return dict[k]

    raise Exception("empty dictionary")


def sort_dict(dictionary):
    count_list = list()

    for k in dictionary:
        d = {}
        d[k] = dictionary[k]
        count_list.append(d)

    count_list.sort(reverse=True, key=sort_on)
    return count_list
