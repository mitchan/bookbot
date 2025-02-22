from stats import count_words, num_of_characters


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    content = get_book_text("./books/frankenstein.txt")

    word_count = count_words(content)
    print(f"{word_count} words found in the document")

    character_dict = num_of_characters(content)
    print(character_dict)

    # print(content)


main()
