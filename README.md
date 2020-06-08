# HTML-To-WordCloud
This program scrapes text off of any HTML webpage or local file, processes the content, and generates a wordcloud over a mask of an existing image.

Features:
- Scrapes text from any URL or local HTML file
- Loads a list of stopwords that are removed from the dataset
  - Easily appended (see comment on line 30 of HTMLtoWordCloud.py)
- Creates a plot showing the 30 most used words in the dataset and their frequencies
- Reads a local image file to create a shape for the wordcloud
- Generates the wordcloud


A big thanks to the developers of the external Python libraries used: NLTK, PIL, Numpy, BeautifulSoup, WordCloud, MatPlotLib

The example in the repository is of Fyodor Dostoevsky's novel Crime and Punishment generated over a mask image of a hatchet.
Thanks to Project Gutenberg for hosting the novel. 
![Hatchet](https://github.com/AaronHenry/HTML-To-WordCloud/blob/master/CnPHatchet.png)
![Plot](https://github.com/AaronHenry/HTML-To-WordCloud/blob/master/CnPPlot.png)
![Axe](https://github.com/AaronHenry/HTML-To-WordCloud/blob/master/axe.jpg)

