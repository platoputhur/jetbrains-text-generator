from nltk import RegexpTokenizer

regex_tokenizer = RegexpTokenizer('[A-z]+')
sentence = input()
index = int(input())
tokens = regex_tokenizer.tokenize(sentence)
print(tokens[index])
