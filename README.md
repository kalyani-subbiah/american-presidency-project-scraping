# American Presidency Project - Web scraping

Scraping the American Presidency Project Website for presidential speeches and documents. The function scrapes from the search page.

Search page: https://www.presidency.ucsb.edu/advanced-search

Description: "The American Presidency Project, non-profit and non-partisan, is the leading source of presidential documents on the internet.  Our rapidly-growing collection is hosted at the University of California, Santa Barbara."

#### Usage:
###### Parameter: url
Select url:
1) Go to American Presidency Project website and click on the search button on the top right
(OR) Go to url above
2) Adjust search settings as desired
3) Copy url

###### Parameter: max_page_count
Note down page number from last page of table. 

Function stores json files with 100 documents each and a master json file with all of the documents.
To save on memory, adjust max_page_count to lower value.

