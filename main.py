def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    count_each_character(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def words_counter(text):
    split_text = text.split()
    numebr_of_words = len(split_text)
    return numebr_of_words

def count_each_character(text):
    lowered_text = text.lower()
    split_lower_text = lowered_text.split()
    word_dictionary = {}
    for words in split_lower_text:
        for word in words:
            if word in word_dictionary:
                word_dictionary[word] +=1
            else:
                word_dictionary[word] = 1
            
    print(word_dictionary)


main()