import os
from random import randrange
from urllib.request import urlopen
from bs4 import BeautifulSoup

#extract data of first td element of every td in the html table
#return list of all first cells
def extract_data(table):
    result = []
    for row in table.find_all('tr'):
        firstCel = True
        for cell in row.find_all('td'):
            if firstCel:
                companyName = cell.text
                companyName = companyName.lower()
                result.append(companyName.replace(" ", "").replace(".", "").strip())
                firstCel = False
    return result


sep = os.path.sep

#Scraping of company names and common nouns with BeatifulSoup in order to generate random package names that appear realistic

#Largest companies by revenue from https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue
website = urlopen("file:" + os.getcwd() + sep + "companies.html")
soup = BeautifulSoup(website, 'html.parser')
companiesTable = soup.find_all('table')[0]
companies = extract_data(companiesTable)

#List of common nouns from https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx
website = urlopen("file:" + os.getcwd() + sep + "nouns.html")
soup = BeautifulSoup(website, 'html.parser')
nounsTable = soup.find_all('table')[0]
nouns = extract_data(nounsTable)

for i in range(100):
    print("Package name " + str(i + 1) + ": com." + companies[randrange(len(companies))] + '.' + nouns[randrange(len(companies))])
