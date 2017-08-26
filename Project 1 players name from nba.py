from selenium import webdriver

from bs4 import BeautifulSoup

driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
driver.get("http://www.nba.com/players/")
html_text = driver.page_source
bsObj = BeautifulSoup(html_text , 'lxml')

players = []
div = bsObj.find("div" , {"id":"player-list"})

for a in div.find_all("a"):
    span = a.find("span" ,class_="name-label")
    players.append(span.text)


print(players)
