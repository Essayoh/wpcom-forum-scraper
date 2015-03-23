import requests
import bs4
import shutil
import os
from time import strftime

#didn't actually need to split these up, next iteration can be joined
root_url = 'https://en.forums.wordpress.com'
index_url = root_url + "/forum/support"
date = strftime("%Y-%m-%d")

check_data = os.path.exists("data/" + date + ".txt")

if check_data == False:
	file=open(os.path.join("data/", date + ".txt"), 'w')


def get_page_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text)
    return [a.attrs.get('href') for a in soup.select('td a')]

topic_urls = get_page_urls()

#hacky removal of sticky threads, future iteration = check if sticky, don't scrape 
topic_urls.remove('https://en.forums.wordpress.com/topic/wordpresscom-forums-community-standards')
topic_urls.remove('https://en.forums.wordpress.com/topic/forums-faq-getting-started-in-the-forums')
topic_urls.remove('https://en.forums.wordpress.com/topic/forums-in-other-languages-not-english')

for url in topic_urls:
	response = requests.get(url)
	soup = bs4.BeautifulSoup(response.text)
	for topic in soup.find_all(class_="post"):
		with open(os.path.join("data/", date + ".txt"), "a") as workfile:
   			workfile.write(topic.get_text().encode('utf-8'))
