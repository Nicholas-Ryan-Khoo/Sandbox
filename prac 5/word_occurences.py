OCCURRENCE_COUNT = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = OCCURRENCE_COUNT.get(word, 0)
    OCCURRENCE_COUNT[word] = frequency + 1

words = list(OCCURRENCE_COUNT.keys())
words.sort()

max_length = max((len(word) for word in words))

for word in words:
    print("{:{}} : {}".format(word, max_length, OCCURRENCE_COUNT[word]))
