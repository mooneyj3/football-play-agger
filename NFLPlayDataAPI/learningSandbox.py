import nflgame

games = nflgame.games(2016, week=1)

for game in games:
    print(game)

