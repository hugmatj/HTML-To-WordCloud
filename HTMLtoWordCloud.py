# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 07:29:28 2020

@author: AaronHenry

Crime and Punihsment by Fyodor Dostoevsky 
Provided by Gutenberg Project
"""

import nltk
import numpy as np
from PIL import Image

""" place your URL or file:c/// here """
import urllib.request
response =  urllib.request.urlopen('https://www.gutenberg.org/files/2554/2554-h/2554-h.htm')
html = response.read()



from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)


tokens = [t for t in text.split()]
print(tokens)

""" add any words you wish to delete from the scraped content here using sr.append() """
words = set(nltk.corpus.words.words())
from nltk.corpus import stopwords
sr= stopwords.words('english')
sr.append('like')
sr.append('said')
clean_tokens = tokens[:]
for token in tokens:
    if token in sr or token not in words:
        
        clean_tokens.remove(token)
        
reduced_tokens = list(word.lower() for word in clean_tokens if word.isalpha() and len(word) > 3 and len(word) < 15)

""" makes a nice plot for you to visualize what words are most common """
freq = nltk.FreqDist(reduced_tokens)

freq.plot(30, cumulative=False)

""" shape image for the wordcloud mask """
char_mask = np.array(Image.open("C:/Users/aaron/.spyder-py3/axe.jpg"))    
##image_colors = ImageColorGenerator(char_mask)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wc = WordCloud(max_words=150, margin=1, background_color='black',
               scale=1, relative_scaling = 0.25, color_func=lambda *args, **kwargs: (255,255,255), mask=char_mask, width=400, height=400,
               random_state=1).generate(' '.join(reduced_tokens))


plt.figure(figsize=(20,10))
plt.imshow(wc)
plt.axis("off")
plt.show()

