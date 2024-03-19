#%%
import nltk, re
nltk.download("all")
from nltk import word_tokenize, pos_tag


#%%
f = open('Medical transcripts/text1.txt')
raw = f.read()
parags = list(enumerate(p for p in raw.split("\n\n")))
print(parags[0][1])

p0_tokenize = word_tokenize(parags[0][1])
print(p0_tokenize)
p0_postags = pos_tag(p0_tokenize)
p0_postags





# %%

grammar = "NP: {<NN><IN>(<NNS>)}"

chunk_parser = nltk.RegexpParser(grammar)

tree = chunk_parser.parse(p0_postags)

tree.draw()

# %%

