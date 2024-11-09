from textblob import TextBlob

'''
from newspaper import Article
import nltk
nltk.download('punkt')


url = 'https://www.mirror.co.uk/news/uk-news/child-murderer-due-release-dad-32440689'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)
'''


# Read the text from a file or any other source
with open('mytext.txt', 'r') as f:
    text = f.read()

# Analyze sentiment using TextBlob
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

# Determine the appropriate response
if sentiment > 0:
    print("Positive sentiment! 😄")
elif sentiment < 0:
    print("Negative sentiment. 😔")
else:
    print("Neutral sentiment. 😐")

