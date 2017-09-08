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
import DataExtraction.player_game_stats

# quick URL utility
prefix = "http://www.nfl.com/liveupdate/game-center/"
suffix = "_gtd.json"
def URLString(ID):
    return prefix + str(ID) + "/" + str(ID) + suffix

# used to get ID out of gamecenter URL
def getID(URL):
    fields = URL.split("/")
    return fields[2]

def processJSON(game_id, URL):
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
        game_id_str = str(game_id)
        #pprint(data)
        #pprint(data[str(ID)]['away'])

        player_dict = {}

        # location: home or away
        loc = 'away'

        # loop through home/away items in JSON
        i = 0
        while i < 2:
            # determine team name based on location
            team_abbr = data[game_id_str][loc]['abbr']

            # playtypes will be one of:  defense, fumbles, kicking, kickret, passing, punting, puntret, receiving, rushing
            for playtype in data[game_id_str][loc]['stats']:
                # skip 'team' summary playtype
                if playtype == 'team':
                    continue
                # loop through each player within a specified play type
                for player_id in data[game_id_str][loc]['stats'][playtype]:
                    # if player does not exist, create and add to player_dict
                    if player_id not in player_dict:
                        curr_player = DataExtraction.player_game_stats.PlayerGameStats\
                            (game_id, player_id, data[game_id_str][loc]['stats'][playtype][player_id]['name'],
                             team_abbr, loc)
                        player_dict[player_id] = curr_player
                    else:
                        curr_player = player_dict[player_id]

                    # process current stats field for player
                    # defense
                    if playtype == 'defense':
                        curr_player.defense_stats(
                            data[game_id_str][loc]['stats'][playtype][player_id]['ast'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['ffum'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['int'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['sk'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['tkl']
                        )

                    # fumbles
                    elif playtype == 'fumbles':
                        curr_player.fumbles_stats(
                            data[game_id_str][loc]['stats'][playtype][player_id]['lost'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['rcv'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['tot'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['trcv'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['yds']
                        )

                    # kicking
                    elif playtype == 'kicking':
                        curr_player.kicking_stats(
                            data[game_id_str][loc]['stats'][playtype][player_id]['fga'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['fgm'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['fgyds'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['totpfg'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['xpa'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['xpb'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['xpmade'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['xpmissed'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['xptot']
                        )

                    # kickret
                    elif playtype == 'kickret':
                        curr_player.kickret_stats(
                            data[game_id_str][loc]['stats'][playtype][player_id]['avg'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['lng'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['ret'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['tds']
                        )

                    # passing
                    elif playtype == 'passing':
                        curr_player.passing_stats(
                            data[game_id_str][loc]['stats'][playtype][player_id]['att'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['cmp'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['ints'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['tds'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['twopta'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['twoptm'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['yds']
                        )

                    # punting
                    elif playtype == 'punting':
                        curr_player.punting_stats(
                            data[game_id_str][loc]['stats'][playtype][player_id]['avg'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['i20'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['lng'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['pts'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['yds']
                        )

                    # puntret
                    elif playtype == 'puntret':
                        curr_player.puntret_stats(
                            data[game_id_str][loc]['stats'][playtype][player_id]['avg'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['lng'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['ret'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['tds']
                        )

                    # receiving
                    elif playtype == 'receiving':
                        curr_player.receiving_stats(
                            data[game_id_str][loc]['stats'][playtype][player_id]['lng'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['rec'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['tds'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['twopta'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['twoptm'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['yds'],
                        )
                    # rushing
                    elif playtype == 'rushing':
                        curr_player.rushing_stats(
                            data[game_id_str][loc]['stats'][playtype][player_id]['att'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['lng'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['name'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['tds'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['twopta'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['twoptm'],
                            data[game_id_str][loc]['stats'][playtype][player_id]['yds']
                        )
            i += 1
            loc = 'home'



        print(player_dict)



        # away/home:
        #   defense, fumbles, kicking, kickret, passing, punting, puntret, receiving, rushing,

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



