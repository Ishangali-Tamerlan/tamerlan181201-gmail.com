word =input ()
word = word[:word.find('h')] + word[word.rfind('h') + 1 :]
print(word)
