from selenium import webdriver
#from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import requests


class Player():

    def __itit__(self):
        self.name = ""
        self.link = ""
        self.height = ""
        self.weight = ""
        self.born = ""
"""
    def get_details(self,names , links):
        #name = self.name
        #link = self.link
        full_info = {}
        i=0
        for na in names:
            full_info[na] = links[i]
            i+=1
        return full_info            
"""
def players_details():
    driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
    driver.get("http://www.nba.com/players/")
    html_text = driver.page_source

    #html_text = urlopen("http://www.nba.com/players/")
    bsObj = BeautifulSoup(html_text , 'lxml')

 
    div = bsObj.find("div" , {"id":"player-list"})
    players_list = []
    for a in div.find_all("a"):
        span = a.find("span" ,class_="name-label")
        one_player = Player()
        one_player.name = span.text
        one_player.link = a['href']
        players_list.append(one_player)
    driver.quit()
    return players_list


def get_details_for_all_players(players_list):

    driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
    for e in players_list[0:2]:
        url = e.link

        driver.get("http://www.nba.com"+url)
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


        e.height = height
        e.weight = weight
        e.born = born


    driver.quit()
    return (players_list)


driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
driver.get("http://www.nba.com/players/alex/abrines/203518")

html_doc = driver.page_source

soup = BeautifulSoup(html_doc , "lxml")

section = soup.find("section" , class_="nba-player-header__item nba-player-header__headshot")
img = section.find("img")

fil = open("alex.jpg","wb")
fil.write(requests.get(img['src']).content)

fil.close()
driver.quit()
    
