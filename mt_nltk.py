#%%
import nltk, re, os
from nltk import word_tokenize, pos_tag



#%%
os.listdir('.')

#%%
f = open('Medical transcripts/text1.txt')
raw = f.read()
text1_tokenize = word_tokenize(raw)
text1_postags = pos_tag(text1_tokenize)
text1_postags



# %%

grammar = "NP: {<DT>?<JJ>*<NN><IN>(<NNS>|<NN>)}"

chunk_parser = nltk.RegexpParser(grammar)

tree = chunk_parser.parse(text1_postags)

tree

# %%

