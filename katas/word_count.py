import re
def count_words(sentence):
    """
    Counts the number of words in a given sentence.

    Args:
        sentence: the input string (a sentence)

    Returns:
        the number of words in the sentence
    """
    sentence = sentence.replace("'","")
    sentence = re.findall(r'\b[a-zA-Z]+\b', sentence.replace("_",' '))

    return len(sentence)


if __name__ == '__main__':
    sentence = "I have 99 problems,but a code ain't one! ."
    word_count = count_words(sentence)
    print(word_count)  # 8 should be printed