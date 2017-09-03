
class PlayerGameStats:
    def __init__(self, game_id, player_id, name, team, loc):
        self.game_id = game_id
        self.player_id = player_id
        self.name = name
        self.team = team
        self.loc = loc

    def __repr__(self):
        return '%s: {%s, %s, %s, %s}' % (self.player_id,
                                     self.game_id,
                                     self.name,
                                     self.team,
                                     self.loc)

