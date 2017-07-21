"""

example:
    /gamecenter/2016081152/2016/PRE1/redskins@falcons

http://www.nfl.com/gamecenter/2016081152/2016/PRE1/redskins@falcons#menu=gameinfo&tab=analyze&analyze=playbyplay

https://www.reddit.com/r/NFLstatheads/comments/59drb1/how_to_query_nfls_liveupdate_json_data/
http://www.nfl.com/liveupdate/game-center/2016081152/2016081152_gtd.json

"""

import urllib.request


domain = "http://www.nfl.com"
tail = "#menu=gameinfo&tab=analyze&analyze=playbyplay"
sample = "/gamecenter/2016081152/2016/PRE1/redskins@falcons"


def getHTMLPage(url):
    print(url.split("/"))
    urllib.request.urlretrieve(domain + url + tail, "afile.html")





getHTMLPage(sample)