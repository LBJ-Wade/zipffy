import sys
import operator
import matplotlib.pyplot as plt
import numpy as np
import re

if len(sys.argv) !=3:
    print('Usage: python zipffy.py text_to_analyse.txt num_words_to_plot')
    sys.exit(-1)

words = {}
with open(sys.argv[1], 'r') as f:
    for word in f.read().lower().split(): #assume case-insensitive
        cleaned_word = re.sub('[^a-z]+','',word) # remove non-alphabetic characters
        if cleaned_word not in words:
            if not cleaned_word == '':
                words[cleaned_word] = 1
        else:
            words[cleaned_word] += 1
ranked_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
print(ranked_words)

N = int(sys.argv[2])
if N > len(words):
    print('Only have {0} words, plotting all.'.format(len(words)))

plt.plot([i[1] for i in ranked_words[:N]])
plt.xticks(np.arange(1,N+1),[i[0] for i in ranked_words[:N]])
# 1/x scaled to meet first point. Could do an actual regression or something
plt.plot(ranked_words[0][1]/np.arange(1,N+1))

plt.show()
