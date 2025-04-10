from stats import char_count, word_count,to_sort
import sys 

def main():
    text = ""
    filepath = ""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    with open(filepath) as file:
        text = file.read()

    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    count = word_count(text)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    ch_count = char_count(text)
    chars = to_sort(ch_count)
    for char in chars:
        print(f"{char[0]}: {char[1]}")
    print("============= END ===============")


main()
