# http://www.nfl.com/scores/2013/REG1
from bs4 import BeautifulSoup as Soup
import urllib.request


def list_games(year, season_type):
    """
    Generates a list of urls given the year and season type for indivudial games on nfl.com
    :param year: year for the games season
    :param season_type: Regular = REG1, Post = POST18, Pre = PRE1
    :return: list of urls for games from a given season and year.
    --Kurtpr
    """
    result = []  # List of urls of games for given year and season
    # Url formatted to use year and season type provided
    url_base = "http://www.nfl.com/scores/{0}/{1}".format(year, season_type)
    play_by_play_url = "#menu=gameinfo%7CcontentId%3A0ap3000000702842&tab=analyze&analyze=playbyplay"
    nfl = urllib.request.urlopen(url_base)
    # Provide the HTML returned from our URL to BeautifulSoup
    html_nfl_games = nfl.read()
    soup = Soup(html_nfl_games)

    for link in soup.find_all("a"):
        ref = link.get("href")
        if "@" in ref and "highlights" not in ref:
            result.append("http://www.nfl.com/" + ref + play_by_play_url)

    return result


if __name__ == "__main__":
    li = list_games("2016", "REG1")
    for game in li:
        print(game)
