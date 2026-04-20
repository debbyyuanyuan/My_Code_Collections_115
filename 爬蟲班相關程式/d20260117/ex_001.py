import nltk, spaCy
nltk.download('punkt')
from nltk.tokenize import word_tokenize
text = "This is a sample sentence, with punctuation!"
print(word_tokenize(text))
 
