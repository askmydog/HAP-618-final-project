import nltk, re, os
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

#%%
os.listdir('.')

#%%
f = open('Medical transcripts/text1.txt')
raw = f.read()
for l in raw.split("\n\n"):
    print(l)


# %%

text1_tokenize = word_tokenize(raw)

# %%
