import urllib
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords

#string websites
websites = ""

#for each website in website list
with open('website_list', 'r') as f:
    websites = f.readlines()

#for each website in website list
for url in websites:
    print url
    #url = "http://www.cnn.com/2017/01/24/politics/donald-trump-chicago-carnage/index.html"
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    #print(text.encode('utf-8'))
    all_words = {text.encode('utf-8')}
    content = re.sub(r'^"|"$', '', text.encode('utf-8'))
    content = content.lower()
    punctuations = ["?", "'", ".", ",", '"', "%", "-", "&", "$", "|", ":", ";", ")", "("]
    #word_with_digits = content.replace("'", "").replace(".", "").replace("-", "").replace(",","").replace(";", "").replace('"', "").replace("!", "").replace(":", "").replace("?", "").replace("%", "")
    for symbol in punctuations:
        #print symbol
        content = content.replace(symbol, " ")
    final_word = ''.join([i for i in content if not i.isdigit()])
    final_word = re.split('\s+', final_word)
    #print[word for word in final_word if word not in stopwords.words('english')]
    final_word = [word for word in final_word if word not in stopwords.words('english')]
    final_word = [item.replace('\xc2\xa0', ' ')for item in final_word]
    final_word = [item.replace('\xe2\x84\xa2', ' ')for item in final_word]
    final_word = [item.replace('com\xc2\xa9', ' ')for item in final_word]
    final_word = [item.replace('\xc2\xa9', ' ')for item in final_word]
    print final_word
    #print final_word

    # For every word in the article
	for word in strings.split():
		word = word.lower()
		word_count += 1
		# Increase word frequency by 1
		if word in word_list:
			word_list[word] += 1
		else:
			word_list[word] = 1

		# Add word to complete word list
		if word not in all_words:
			all_words.append(word)

	# Add title and word/frequency to dictionary
	web_to_words[title] = word_list

	# Add to word count list
	total_words.append(word_count)


# Create csv document
with open("data.csv", 'w') as csvfile:
	# csv formatting
	writer = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	# Write all of the words to the top row
	space_with_all_words = ['SITE', 'WORD COUNT'] + all_words
	writer.writerow(space_with_all_words)

	# For each word
	for site, word_count in zip(web_to_words, total_words):
		# List of every word on the site
		words = web_to_words[site]

		# List of the frequency of all of the words in the same order as all_words is in
		word_frequency = []

		# For every word
		for word in all_words:
			# If in site, append frequency, if not, append a 0
			if word in words:
				word_frequency.append(words[word])
			else:
				word_frequency.append(0)

		test = [site] + [word_count] + word_frequency
		# Write site title and word frequency as a row in csv
		writer.writerow(test)
