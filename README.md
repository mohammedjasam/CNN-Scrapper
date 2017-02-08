# CNN Scraper

This script scrapes CNN article pages for their word frequency and then creates a data matrix which is later subjected to various similarity functions to analyze the similarity of the articles.

## How to Run
Scripted in Python 3.6 but needs python 2.7+ too :)
* Run "python3 scrapper.py"
* Use the Data.csv in Similarity Analyzer Folder
* Run "python3 Parallel.py" (This step needs python 2.7, so make sure you've installed them both)

## Requirements:

* "article_list" contains all the list of urls which can be obtained by running the crawler "article_url"
* beautifulsoup4 (4.5.1)
* lxml
* nltk
* SciPy

## Output:

A data file called data.csv is saved. It contains a list of word frequencies associated with each article.
Output files of Euclidean, Jaccard and Cosine Distances are generated to analyze the similarity of the articles.
