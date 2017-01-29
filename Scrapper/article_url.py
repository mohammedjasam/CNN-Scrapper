articles = []
with open('', 'r') as f:
	url = f.readlines()
	for u in url:
		articles.append(u)


unique_articles = sorted(set(articles))

if(len(articles) != len(unique_articles)):
	with open('article_list', 'w') as f:
		for url in unique_articles:
			f.write(url)

