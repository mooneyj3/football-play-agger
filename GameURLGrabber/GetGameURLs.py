# include bs4 library
from bs4 import BeautifulSoup as Soup

# include urllib library
import urllib.request
response = urllib.request.urlopen('http://www.nfl.com/scores/2016/REG17')

html = response.read()

soup = Soup(html, "lxml")

print(soup.prettify())



## soup = Soup('http://www.nfl.com/scores/2016/REG17', 'html.parser')

##print(soup.prettify())

# def myfunction():
#     print("Hello World!");
# myfunction();
