"""
GetGameURLs.py

Collects and aggregates NFL gamecenter URL's.
Each game has a unique game center URL
Gamecenter URL's have the following format:
    http://www.nfl.com/scores/YYYY/SSNWK

Where YYYY is the year, SSN is the season (PRE, REG, POST), and WK is the week

    http://www.nfl.com/scores/2016/REG17

"""

# include bs4 library
from bs4 import BeautifulSoup as Soup

# include urllib library
import urllib.request

# class variables
home = "http://www.nfl.com/scores/"

"""
# sample code
response = urllib.request.urlopen('http://www.nfl.com/scores/2016/REG17')

html = response.read()

soup = Soup(html, "lxml")

# Need to find all <a class="game-center-link" href="...">
for i in soup.find_all("a", class_="game-center-link", href=True):
    print(i['href'])
"""

# callee to generate Game URL files
def generateGameURLs(startYear, endYear):
    for year in range(startYear, endYear):

        # get PRE season URL's for current year
        for week in range(1, 4):
            url = home + str(year) + "/PRE" + str(week)
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = Soup(html, "lxml")
            for i in soup.find_all("a", class_="game-center-link", href=True):
                print(i['href'])
                
        # get REG season URL's for current year
        for week in range(1, 17):
            url = home + str(year) + "/REG" + str(week)
        
        # get POST season URL's for current year
        for week in range(18, 22):
            url = home + str(year) + "/POST" + str(week)
                
        