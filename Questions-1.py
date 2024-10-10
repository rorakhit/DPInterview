

from concurrent.futures import process


def process_text_to_unique(a):
    words = a.split(",")
    print(words)
    altered_words = []
    for word in words:
        lower_word = word.lower()
        stripped_word = lower_word.strip()
        altered_words.append(stripped_word)
    print("2nd: {}".format(altered_words))
    unique_words = []
    for word in altered_words:
        if word not in unique_words:
            unique_words.append(word)

    return unique_words

a = process_text_to_unique("boston, Boston, bos, New York, new york, NYC, Alberta")

print(a)