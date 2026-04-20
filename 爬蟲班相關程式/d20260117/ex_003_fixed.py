import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
import spacy
text = "This is a sample sentence, with punctuation!"
print(word_tokenize(text))

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
print([token.text for token in doc])
