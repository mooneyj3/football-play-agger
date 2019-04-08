"""
This downloads all NFL json data for years provided in main
@author: Jonny Mooneyham
"""

from bs4 import BeautifulSoup as Soup
import urllib.request
import urllib
import sys, os, json

nfl_scores_url = "http://www.nfl.com/scores/"


def get_game_ids(start_year, end_year, season_type):
    game_ids = {}
    for year in range(start_year, end_year + 1):
        if season_type == "PRE":
            start_week = 1
            end_week = 4
        elif season_type == "REG":
            start_week = 1
            end_week = 17
        elif season_type == "POST":
            start_week = 18
            end_week = 22
        else:
            print("Invalid season_type")
            sys.exit(0)

        print("Getting game ids for year: " + str(year) + "\t season: " + season_type + "...")
        for week in range(start_week, end_week + 1):
            score_summary_url = nfl_scores_url + str(year) + "/" + season_type + str(week)
            key = "{yr}_{seas_tp}_{wk:02d}".format(yr=str(year), seas_tp=season_type, wk=week)
            id_list = fetch_ids_from_game_center_weekly_summary(score_summary_url)
            game_ids[key] = id_list

    return game_ids


def fetch_ids_from_game_center_weekly_summary(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = Soup(html, "lxml")
    ids = []
    for i in soup.find_all("a", class_="game-center-link", href=True):
        href_split = i['href'].split("/")
        ids.append(str(href_split[2]))
    return ids


def get_play_data_jsons(game_id_dict, output_dir):
    prefix = "http://www.nfl.com/liveupdate/game-center/"
    suffix = "_gtd.json"
    for key, games in game_id_dict.items():
        for game_id in games:
            # url format: http://www.nfl.com/liveupdate/game-center/{...id...}/{...id...}_gtd.json
            # example   : http://www.nfl.com/liveupdate/game-center/2016081152/2016081152_gtd.json
            source_file_name = game_id + suffix
            request_url = prefix + game_id + "/" + source_file_name
            dest_file = output_dir + key + '_' + source_file_name
            urllib.request.urlretrieve(request_url, dest_file)


def main():
    # setup output directory
    dir = input("Where do you want json files to go? --> ")
    if dir[-1] != '\\':
        print("adding \\ to dir: " + dir)
        dir = dir + '\\'

    if not os.path.isdir(dir):
        print("Not a valid directory!")
        sys.exit(0)

    start_year = 2018
    end_year = 2018

    pre_game_ids = get_game_ids(start_year, end_year, 'PRE')
    reg_game_ids = get_game_ids(start_year, end_year, 'REG')
    post_game_ids = get_game_ids(start_year, end_year, 'POST')

    get_play_data_jsons(pre_game_ids, dir)
    get_play_data_jsons(reg_game_ids, dir)
    get_play_data_jsons(post_game_ids, dir)


if __name__ == '__main__':
    main()



