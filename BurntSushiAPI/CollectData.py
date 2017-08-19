import nflgame

games = nflgame.games(2013, week=1, kind='REG')

players = nflgame.combine_game_stats(games)

for p in players.limit(10):
    #http://pdoc.burntsushi.net/nflgame/player.m.html
    #print(p.name, p.formatted_stats())
    print(p.player, p.rushing_att)

