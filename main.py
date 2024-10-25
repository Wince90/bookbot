def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = words_counter(text)
    text_dict = count_each_character(text)
    sorted_text = sort_dictionary(text_dict)
    print_report(sorted_text, book_path, number_of_words)



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
            
    return word_dictionary

def sort_dictionary(dictionary):
    sorted_scores = dict(sorted(dictionary.items(), key=lambda a: a[1], reverse=True))
    return sorted_scores

def print_report(process_text, book_path, words_number):
    tuple_text = process_text.items()
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_number} words found in the document\n")
    for text in tuple_text:
        if text[0].isalpha():
            print(f"The '{text[0]}' character was found {text[1]} times")
    print("--- End report ---")

main()