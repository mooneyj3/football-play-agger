"""
The json's are available as follows
http://www.nfl.com/liveupdate/game-center/2016081152/2016081152_gtd.json

/gamecenter/2009091000/2009/REG1/titans@steelers
sample ID:  2009091000

play categories
    defense, fumbles, kicking, kickret, passing, punting, puntret, receiving, rushing,

$YEAR/$PLAYER.train.csv
$YEAR/$PLAYER.dev.csv
$YEAR/$PLAYER.test.csv

"""
import json, urllib.request
from pprint import pprint

# quick URL utility
prefix = "http://www.nfl.com/liveupdate/game-center/"
suffix = "_gtd.json"
def URLString(ID):
    return prefix + str(ID) + "/" + str(ID) + suffix

# used to get ID out of gamecenter URL
def getID(URL):
    fields = URL.split("/")
    return fields[2]

def processJSON(ID, URL):
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
        #pprint(data)
        pprint(data[str(ID)]['away'])

def addPlayerStatsToFile(year, dict):
    # $Year/$Player.$type.csv
    # type in [train, dev, test]
    print(str(year))

# test zone
inp = "/gamecenter/2009091000/2009/REG1/titans@steelers"
out = getID(inp)
print(out)
print(URLString(out))
processJSON(out, URLString(out))

