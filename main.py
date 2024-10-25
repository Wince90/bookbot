def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(f'{words_counter(text)}')


def get_book_text(path):
    with open(path) as f:
        return f.read()

def words_counter(text):
    split_text = text.split()
    numebr_of_words = len(split_text)
    return numebr_of_words


main()