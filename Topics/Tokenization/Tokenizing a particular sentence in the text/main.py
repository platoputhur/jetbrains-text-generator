from nltk import sent_tokenize, RegexpTokenizer
text = input()
index = input()
sentences = sent_tokenize(text)
regex_tokenizer = RegexpTokenizer("[A-z']+")
print(regex_tokenizer.tokenize(sentences[int(index)]))


