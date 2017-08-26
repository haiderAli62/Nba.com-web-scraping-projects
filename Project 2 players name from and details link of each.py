from selenium import webdriver
#from urllib.request import urlopen
from bs4 import BeautifulSoup

class Player():

    def __itit__(self):
        self.name = ""
        self.link = ""

    def get_details(self,names , links):
        #name = self.name
        #link = self.link
        full_info = {}
        i=0
        for na in names:
            full_info[na] = links[i]
            i+=1

        return full_info            
            
        



def players_details():
    driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
    driver.get("http://www.nba.com/players/")
    html_text = driver.page_source

    #html_text = urlopen("http://www.nba.com/players/")
    bsObj = BeautifulSoup(html_text , 'lxml')
    all_players = []
    players = []
    links = []
    div = bsObj.find("div" , {"id":"player-list"})

    for a in div.find_all("a"):
        span = a.find("span" ,class_="name-label")
        one_player = Player()
        one_player.name = span.text
        one_player.link = a['href']
        links.append(a['href'])
        players.append(span.text)
        all_players.append(one_player)
    for p in all_players:
        print(p.name)
        print(p.link)
   # print(all_players)

    driver.quit()

    
    #return one_player.get_details(players , links)
    return (all_players)
   


players_details()
