from bs4 import BeautifulSoup
import urllib.request
import json
import os


def APP_scrape(url = "https://www.presidency.ucsb.edu/advanced-search?field-\
			 keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bd\
			 ate%5D=&person2=&category2%5B%5D=&items_per_page=100", president=
			 "trump", max_page_count = 100):
	"""
	Function to scrape documents from American Presidency Project. The function
	scrapes documents from table in search page. 
	Function stores documents in json files at 100 documents per json file.
	Function reports progress by printing page count and document count.
	Sound alarm is commented and can be enabled.

	Args:
        url (string) = url of search page. Documents from table in search page 
        			   will be scraped.
        president (string): president's name for naming outfile
        max_page_count (int): maximum number of pages in table to be scraped
        					  (default: 100)
       
    Returns:
        None
	"""
	# stores number of pages scraped
	page_count = 0

	#stores number of documents scraped
	c = 0

	while page_count < max_page_count:

		#dict to store documents in a page
		documents = {}
		print("\n \n ---------------PAGE COUNT: ", page_count)
		#url of search page
		url = url + "&page=" + str(page_count)
		html_page = urllib.request.urlopen(url)
		soup = BeautifulSoup(html_page, "lxml")
		#find links in table
		data = soup.findAll('div',attrs={'class':"view-content"})
		for div in data:
			links = div.findAll('a')
			for a in links:	
				#not considering links to the president's page, only links to 
				#documents		
				if '/people/president' != str(a['href'])[:17]:
					#dictionary to store details of documents
					link = {}
					#url of document
					url_1 = "https://www.presidency.ucsb.edu" + a['href']
					html_1 = urllib.request.urlopen(url_1)
					soup_1 = BeautifulSoup(html_1, "lxml")	
					#store date	
					date = soup_1.findAll('span',attrs={'class':"date-display-s\
														ingle"})
					for d in date:
						link['date'] = d.text
					#store president's name
					person = soup_1.findAll('div',attrs={'class':"field-title"})
					for p in person:
						link["president"] = p.text
					#store title of document
					title = soup_1.findAll('div',attrs={'class':"field-ds-doc-t\
													    itle"})
					for t in title:
						link["title"] = t.text
					#store categories of document
					category = soup_1.findAll('a',attrs={'property':"rdfs:label \
											              skos:prefLabel"})				
					if len(category) > 0:
						link['category'] = []
						for x in category:
							link['category'].append(x.text)
					#store text of document
					text1 = soup_1.findAll('div',attrs={'class':"field-docs-con\
													    tent"})
					for t in text1:
						link["text"] = t.text	
					if link:
						c += 1
						print("DOC COUNT: ", c)
					#store document to master dict
					documents[c] = link
	#created outfile with specified president's name
	filename = president + str(page_count) + ".json"
	with open(filename, 'w') as fp:
		#dump json in dictionary
		json.dump(documents, fp)
	#os.system('say "your program has finished"')

	page_count += 1

#os.system('say "your program has finished"')
#os.system('say "your program has finished"')
#os.system('say "your program has finished"')




