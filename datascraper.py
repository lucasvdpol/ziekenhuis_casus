import requests
from bs4 import BeautifulSoup

def main():
    url = "https://lci.rivm.nl/richtlijnen/brmo"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    article = soup.find ("div" ,{"id" : "paragraph_Algemene-voorzorgsmaatregelen"})
    lists = article.find_all("ul")
    for list in lists:
        items = list.find_all("li")
        for item in items:
            print (item.text)
            print ()
            #print (article)
if __name__ == '__main__':
    main()