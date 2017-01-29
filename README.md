# CNN Scraper

This script scrapes CNN article pages for their word frequency and then creates a data matrix which is later subjected to various similarity functions to analyze the similarity of the articles.

## How to Run
Scripted in Python 3.6

"python3 scrapper.py"

## Requirements:

* Python 3.5.2+
* "article_list" contains all the list of urls which can be obtained by running the crawler "article_url"
* beautifulsoup4 (4.5.1)
* lxml
* nltk

## Output:

A data file called data.csv is saved. It contains a list of word frequencies associated with each article.
Output files of Euclidean, Jaccard and Cosine Distances are generated to analyze the similarity of the articles.
