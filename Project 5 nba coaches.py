from selenium import webdriver

from bs4 import BeautifulSoup

driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
driver.get("http://www.nba.com/news/coaches/")
html_text = driver.page_source
bsObj = BeautifulSoup(html_text , 'lxml')

sec = bsObj.find("section" , {"id":"nbaArticleContent"})


for a in sec.find_all("a"):
    print(a.find_previous_sibling().text.replace(':','')+' ---> '+a.text)


"""
for child in sec.findChildren():
    for grandchild in child.findChildren():
        print(grandchild.text)


"""
