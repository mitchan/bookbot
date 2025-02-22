from stats import count_words, num_of_characters, sort_dict
from sys import argv, exit


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    content = get_book_text(argv[1])

    word_count = count_words(content)
    character_dict = num_of_characters(content)
    sorted_list = sort_dict(character_dict)

    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")

    for v in sorted_list:
        for k in v:
            if k.isalpha():
                print(f"{k}: {v[k]}")

    print("============= END ===============")


main()
