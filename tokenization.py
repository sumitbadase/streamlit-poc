corpus = """Hello welcome, to Sumit Badase's world of Natural Language Processing.
Please do watch the video till the end.
"""

print(corpus)

##Tokenization
from nltk.tokenize import sent_tokenize
sent_tokenizes = sent_tokenize(corpus)
print(sent_tokenizes)