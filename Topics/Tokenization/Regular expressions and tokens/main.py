from nltk import RegexpTokenizer

text = input()
rxt = RegexpTokenizer("[A-z'-]+")
print(rxt.tokenize(text))