text = open('read.txt', encoding='utf-8').read()
print(text)

import string
# converting the text to lower case text.
# removing all the punctuations

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
print(cleaned_text)

tokenized_words = word_tokenize(cleaned_text)

final_words = []

for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

print(final_words)

emotion_list = []
with open('emotions.txt') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

from collections import Counter

print(emotion_list)
w = Counter(emotion_list)
print(w)

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
