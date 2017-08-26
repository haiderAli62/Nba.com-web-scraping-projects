from selenium import webdriver

from bs4 import BeautifulSoup

driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
driver.get("http://www.nba.com/players/edmond/sumner/1628410")
html_text = driver.page_source
bsObj = BeautifulSoup(html_text , 'lxml')

height = ""
weight = ""
h_tag = bsObj.find_all("p" , class_ = "nba-player-vitals__top-heading")
#print(h_tag.text)
i = 0
while(i <=1):
    for sib in h_tag[i].findNextSiblings():
        if(i==0):
            height += sib.text
        elif(i==1):
            weight += sib.text

    i=i+1
        
span_tag = bsObj.find("span" , class_="nba-player-vitals__bottom-info")
born = span_tag.text


#w_tag = bsObj.find("p" ,class_ = "nba-player-vitals__top-heading")
#print(w_tag.text)
#for wig in w_tag.findNextSiblings():
 #   weight +=wig.text

driver.quit()
print(height)
print(weight)
print (born)
