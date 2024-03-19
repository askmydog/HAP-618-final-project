#%%
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, word_tokenize, book
# from nltk.book import *
from nltk import corpus
from nltk.corpus import brown, inaugural, reuters

#%%

porter = PorterStemmer()

print(porter.stem('play'))
print(porter.stem('playing'))
print(porter.stem('plays'))

print(porter.stem("communication"))

#%%

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("plays", "v"))
print(lemmatizer.lemmatize("played", "v"))
print(lemmatizer.lemmatize("play", "v"))
print(lemmatizer.lemmatize("playing", "v"))

print(lemmatizer.lemmatize("communication", "v"))

#%%
text = "GeeksforGeeks is a Computer Science platform."
tok_text = word_tokenize(text)
tags = tokens_tag = pos_tag(tok_text)
tags

#%%

def one_hot_encode(text):
    words = text.split()
    vocabulary = set(words)
    word_to_index = {word: i for i, word in enumerate(vocabulary)}
    one_hot_encoded = []
    for word in words:
        one_hot_vector = [0]*len(vocabulary)
        one_hot_vector[word_to_index[word]]=1
        one_hot_encoded.append(one_hot_vector)

    return one_hot_encoded, word_to_index, vocabulary

example_text = "cat in the hat dog on the mat bird in the tree"

one_hot_encoded, word_to_index, vocabulary = one_hot_encode(example_text)
print("Vocabulary:", vocabulary)
print("Word to Index Mapping:", word_to_index)
print("One-Hot Encoded Matrix:")
for word, encoding in zip(example_text.split(), one_hot_encoded):
    print(f"{word}: {encoding}")



#%%

corpus.gutenberg.fileids()

emma = nltk.Text(corpus.gutenberg.words('austen-emma.txt'))

emma.concordance('surprize')

# %%
macbeth_sents = corpus.gutenberg.sents('shakespeare-macbeth.txt')

longest_len = max(len(s) for s in macbeth_sents)
[s for s in macbeth_sents if len(s) == longest_len]

#%%
news_text = brown.words(categories = 'news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ":", fdist[m], end=" ")
# %%

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)

# %%
inaugural.fileids()
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target)
)
cfd.plot()
# %%
text = '''he accepted the position 
of
vice
chairman
of 
Carlyle 
Group 
,
a
merchant
banking
concern
.
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()
# %%
