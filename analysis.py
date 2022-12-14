import nltk
nltk.download('punkt')

from preprocess import remove_punct, to_lowercase, remove_stopwords, lemmatize, lemmatizer_verify
from plots import word_hifreq_chart, word_lofreq_chart

"""
Unsure if downloads below need to be run locally >1 time
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
"""
# -----------------------------------------------------------------------------------------------

# Opening and reading the file
f = open('/Users/cdanza/Documents/Coding/GitHub/PLEXUS2022/medicine.txt','r', encoding='utf8')
raw = f.read()

# -----------------------------------------------------------------------------------------------

# Still testing -> adverbs not always lemmatizing, dwarves = 32
tok = nltk.word_tokenize(raw)
rp = remove_punct(tok)
lo = to_lowercase(rp)
rs = remove_stopwords(lo)
lm = lemmatize(rs)

lemmatizer_verify('medicine', 'medicines', lm, rs)

# -----------------------------------------------------------------------------------------------

# Display data


word_hifreq_chart(lm)
word_hifreq_chart(rs)
# word_lofreq_chart(lemmatized_corpus)
