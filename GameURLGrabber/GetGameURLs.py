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

# callee to generate Game URL files
def generateGameURLs(startYear, endYear):
    for year in range(startYear, endYear + 1):

        # get PRE season URL's for current year
        season = "PRE"
        print("Getting year: " + str(year) + "\t season: " + season + "...")
        for week in range(1, 4 + 1):
            url = home + str(year) + "/" + season + str(week)
            storeURLsToFile(url, year, season)
        print("complete\n")
                
        # get REG season URL's for current year
        season = "REG"
        print("Getting year: " + str(year) + "\t season: " + season)
        for week in range(1, 17 + 1):
            url = home + str(year) + "/" + season + str(week)
            storeURLsToFile(url, year, season)
        print("complete\n")
        
        # get POST season URL's for current year
        season = "POST"
        print("Getting year: " + str(year) + "\t season: " + season + "...")
        for week in range(18, 22 + 1):
            url = home + str(year) + "/" + season + str(week)
            storeURLsToFile(url, year, season)
        print("complete\n")
                
def storeURLsToFile(url, year, season):
    filename = "./URLFiles/" + str(year) + "_" + season + "_gamecenterURLs.csv"
    f = open(filename, 'a')
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = Soup(html, "lxml")
    for i in soup.find_all("a", class_="game-center-link", href=True):
        # print(i['href'])
        f.write(i['href'] + "\n")
    f.close()

generateGameURLs(2016, 2016)
