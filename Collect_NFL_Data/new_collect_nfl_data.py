from bs4 import BeautifulSoup as Soup
import urllib.request
import urllib
import sys, os, json

game_id_file = '../game_id_data/2018_ids.json'


def get_play_data_jsons(game_id_dict, output_dir):
    url_prefix = "http://www.nfl.com/liveupdate/game-center/"
    url_suffix = "_gtd.json"
    for key, games in game_id_dict.items():
        for game_id in games:
            # url format: http://www.nfl.com/liveupdate/game-center/{...id...}/{...id...}_gtd.json
            # example   : http://www.nfl.com/liveupdate/game-center/2016081152/2016081152_gtd.json
            source_file_name = game_id + url_suffix
            request_url = url_prefix + game_id + "/" + source_file_name
            dest_file = output_dir + key + '_' + source_file_name
            urllib.request.urlretrieve(request_url, dest_file)


if __name__ == '__main__':
    print("run")
    with open(game_id_file) as json_file:
        games = json.load(json_file)

    year = list(games.keys())[0]

    pre_season = games[year]['PRE']
    reg_season = games[year]['REG']
    post_season = games[year]['POST']

    print(pre_season.keys())
    print(reg_season.keys())
    print(post_season.keys())

    # output_dir = 'D:/NFL Data Project/data_sources/play_by_play/'
    output_dir = 'D:/NFL Data Project/data_sources/test/'

    get_play_data_jsons(pre_season, output_dir)
    get_play_data_jsons(reg_season, output_dir)
    get_play_data_jsons(post_season, output_dir)


