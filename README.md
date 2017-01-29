# CNN article scraper

This script scrapes CNN article pages for their word frequency.

## How to Run

python3 scrapper.py

## Requirements:

* Python 3.5.2
* website_list file contains a newline separated lists of CNN urls. Note, the CNN articles must have 'zn-body__paragraph' as the div class for the article.
* beautifulsoup4 (4.5.1)

## Output:

A data file called data.csv is saved. It contains a list of word frequencies associated with each article