# include bs4 library
from bs4 import BeautifulSoup as Soup

# include urllib library
import urllib.request

response = urllib.request.urlopen('http://www.nfl.com/scores/2016/REG17')

html = response.read()

soup = Soup(html, "lxml")

##print(soup.prettify())
##print(soup.find_all('a'))

##print(soup.a['game-center-link'])

## <div class="highlight-link">
## <a href="/gamecenter/2017010100/2016/REG17/saints@falcons#menu=highlights|contentId:0ap3000000767814&amp;tab=analyze">

## soup = Soup('http://www.nfl.com/scores/2016/REG17', 'html.parser')

##print(soup.prettify())

soup.findall("a", {"class" : "class=game-center-link"})


##print(soup.findall("a", { "class" : "class" : "game-center-link"}))

# def myfunction():
#     print("Hello World!");
# myfunction();
