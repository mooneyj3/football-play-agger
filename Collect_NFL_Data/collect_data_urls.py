from bs4 import BeautifulSoup as Soup
import urllib.request
import urllib
import sys, os, json
import time

# Collecting url's from schedules listings:  http://www.nfl.com/schedules/2018/REG17

# dict/json structure
# { [[year]]:
#      PRE: {
#          [[week]]: [[id]]


base_url = 'http://www.nfl.com/schedules/'

years = [2018]
seasons = ['PRE', 'REG', 'POST']

# PRE (0, 4)
pre_range = range(0, 5)

# REG (1, 17)
reg_range = range(1, 18)

# POST (NA)
post_range = None


def fetch_ids_from_game_center_schedule(url):
    """

    :returns  dictionary of weeks with their corresponding game id's as a list { WEEK , [[ID]] }
    """
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = Soup(html, "lxml")
    ids = {}
    for i in soup.find_all("a", class_="gc-btn", href=True):
        # as of 4/7/2019, it returns something this: http://www.nfl.com/gamecenter/2018080251/2018/PRE0/bears@ravens
        href_split = i['href'].split("/")
        if len(href_split) == 0:
            continue

        game_id = href_split[4]
        game_ssn = href_split[6]
        game_yr = href_split[5]

        if game_ssn.startswith("PRE") or game_ssn.startswith("REG"):
            game_wk = game_ssn[3:].zfill(2)
            game_ssn = game_ssn[0:3]
        elif game_ssn.startswith("POST"):
            game_wk = game_ssn[4:].zfill(2)
            game_ssn = game_ssn[0:4]

        dict_key = game_yr + "_" + game_ssn + "_" + game_wk

        if dict_key not in ids.keys():
            ids[dict_key] = [game_id]
        else:
            ids[dict_key].append(game_id)

        # print(href_split)
        # print(game_ssn, game_wk, game_id)
        # ids.append(href_split[4])

    return ids


def get_id_dict_by_year(year):

    result = {year: {"PRE": {}, "REG": {}, "POST": {}}}

    for ssn in seasons:
        print("Processing:", ssn)
        # example: http://www.nfl.com/schedules/2018/REG17
        page = base_url + str(year) + "/" + ssn
        wk_range = pre_range if ssn == "PRE" else reg_range if ssn == "REG" else post_range

        if ssn == "POST":
            wk_page = page
            ids = fetch_ids_from_game_center_schedule(wk_page)
            result[year][ssn].update(ids)

        else:
            for wk in wk_range:
                wk_page = page + str(wk)
                ids = fetch_ids_from_game_center_schedule(wk_page)
                result[year][ssn].update(ids)

    return result


if __name__ == '__main__':
    target_year = 2009
    id_dict = get_id_dict_by_year(target_year)

    # for item in id_dict[target_year]['REG']:

    filename = '../game_id_data/' + str(target_year) + '_ids.json'
    with open(filename, 'w') as outfile:
        json.dump(id_dict, outfile)





