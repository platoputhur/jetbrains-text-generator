from nltk import WordPunctTokenizer

wp_tokenizer = WordPunctTokenizer()
sentence = input()
tokens = wp_tokenizer.tokenize(sentence)
print(tokens)
