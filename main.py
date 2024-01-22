def main():
    path = "books/frankenstein.txt"
    file_contents = get_text(path)
    report_letters(path, file_contents)

def report_letters(path, file_contents):
    words_count = count_words(file_contents)
    dict = count_letters(file_contents)

    print(f"--- Begin report of {path} ---")
    print(f"{words_count} words found in the document")

    for d in sorted(dict, key=dict.get, reverse=True):
        print(f"The {d} character was found {dict[d]} times")
    print("--- End report ---")

def count_letters(text):
    dict = {}
    for t in text:
        if t.isalpha():
            tl = t.lower()
            if tl in dict:
                dict[tl] += 1
            else:
                dict[tl] = 1
    return dict

def count_words(text):
    return len(text.split())

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


main()