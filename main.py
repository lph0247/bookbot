from stats import (
    get_num_words, count_char, sort_list)
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path, num_words, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def check_args():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

def main():
    check_args()
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_set = count_char(text)
    sorted = sort_list(char_set)
    print_report(book_path,num_words,sorted)

main()