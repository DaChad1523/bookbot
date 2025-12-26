import sys
from stats import (
    get_book_text,
    get_num_words,
    get_char_count,
    chars_dict_to_sorted_list
)

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    text = get_book_text(file_path)
    word_count = get_num_words(text)
    char_count_dict = get_char_count(text)
    sorted_chars = chars_dict_to_sorted_list(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()




