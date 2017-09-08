"""
Given a year and a file path as input

$YEAR/$PLAYER.train.csv
$YEAR/$PLAYER.dev.csv
$YEAR/$PLAYER.test.csv

8 training
4 dev
4 test
"""

from pathlib import Path
import csv

file_location = Path(input("File output location: "))
# TODO: add file location checks

if not file_location.exists():
    print("error: invalid path")
    exit(0)

year = input("Input year (2009 - 2016): ")
if int(year) not in range(2009, 2016 + 1):
    print("invalid year")
    exit(0)

file_location = file_location.joinpath(str(year))
try:
    file_location.mkdir(exist_ok=False)
except FileExistsError:
    print("Warning: folder for specified year already exists")

# get a collection of all the game_id's for weeks:
#   1-8   training
#   9-12  dev
#   13-16 test


"""
for each game id
    get collection from get_play_data_in_JSON
    process each player in the collection
        if player file exits
            add line with stats
        if player file does not exist
            create and update with stats
"""

