# Write your code here
import random
import string

import regex

from nltk import WhitespaceTokenizer, trigrams
from collections import Counter, defaultdict


def main():
    filename = input()
    # filename = '/Users/defiant/Downloads/corpus.txt'
    tokens: list = []
    trigrams_as_bigram_dict: dict = defaultdict(list)
    tokenizer = WhitespaceTokenizer()
    with open(filename, 'r', encoding='utf-8') as corpus:
        for line in corpus:
            tokens += tokenizer.tokenize(line)
    tokens_as_trigrams = list(trigrams(tokens))
    trigrams_as_bigrams = [(f"{x} {y}", z) for x, y, z in tokens_as_trigrams]
    # Creating the dict with heads and list of tails
    for key, value in trigrams_as_bigrams:
        trigrams_as_bigram_dict[key].append(value)
    sentence_count = 0
    while sentence_count < 10:
        # Getting the sentence starting word
        start_phrase = get_a_sentence_starting_token(trigrams_as_bigram_dict)
        full_sentence = start_phrase
        for _ in range(2, 4):
            current_word = get_next_word(start_phrase, trigrams_as_bigram_dict)
            full_sentence = f"{full_sentence} {current_word}"
            head_tokens = tokenize_based_on_whitespace(full_sentence)
            start_phrase = " ".join(head_tokens[-2:])
        while 1:
            current_word = get_next_word(start_phrase, trigrams_as_bigram_dict)
            if check_if_last_letter_is_a_sentence_ending_punctuation(current_word):
                full_sentence = f"{full_sentence} {current_word}"
                print(full_sentence)
                break
            else:
                full_sentence = f"{full_sentence} {current_word}"
                head_tokens = tokenize_based_on_whitespace(full_sentence)
                start_phrase = " ".join(head_tokens[-2:])
        sentence_count += 1


def get_next_word(current_token, current_bigram) -> str:
    list_of_tails = current_bigram[current_token]
    while len(list_of_tails) == 0:
        current_token = get_a_sentence_starting_token(current_bigram)
        list_of_tails = current_bigram[current_token]
    tail_count = Counter(list_of_tails).values()
    result = random.choices(list(set(list_of_tails)), list(tail_count))
    return result[0]


def get_a_sentence_starting_token(current_bigram):
    random_phrase = random.choice(list(current_bigram.keys()))
    capital_flag = True if random_phrase[0] in string.ascii_uppercase else False
    punctuation_flag = check_if_last_letter_is_a_sentence_ending_punctuation(random_phrase)
    while capital_flag is False or punctuation_flag is True:
        random_phrase = random.choice(list(current_bigram.keys()))
        capital_flag = True if random_phrase[0] in string.ascii_uppercase else False
        punctuation_flag = check_if_last_letter_is_a_sentence_ending_punctuation(random_phrase)
    return random_phrase


def check_if_last_letter_is_a_sentence_ending_punctuation(phrase):
    if regex.match(r'.*?[!.?]\s?', phrase) is None:
        return False
    else:
        return True


def tokenize_based_on_whitespace(token) -> list:
    tokenizer = WhitespaceTokenizer()
    return tokenizer.tokenize(token)


if __name__ == '__main__':
    main()
