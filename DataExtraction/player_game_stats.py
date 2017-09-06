
class PlayerGameStats:
    defense_ast  = 0.0
    defense_ffum = 0.0
    defense_int  = 0.0
    defense_sk   = 0.0
    defense_tkl  = 0.0

    fumbles_lost = 0.0
    fumbles_rcv  = 0.0
    fumbles_tot  = 0.0
    fumbles_trcv = 0.0
    fumbles_yds  = 0.0

    kicking_fga     = 0.0
    kicking_fgm     = 0.0
    kicking_fgyds   = 0.0
    kicking_totpfg  = 0.0
    kicking_xpa     = 0.0
    kicking_xpb     = 0.0
    kicking_xpmade  = 0.0
    kicking_xpmissed = 0.0
    kicking_xptot   = 0.0

    kickret_avg = 0.0
    kickret_lng = 0.0
    kickret_ret = 0.0
    kickret_tds = 0.0

    passing_att    = 0.0
    passing_cmp    = 0.0
    passing_ints   = 0.0
    passing_tds    = 0.0
    passing_twopta = 0.0
    passing_twoptm = 0.0
    passing_yds    = 0.0

    punting_avg = 0.0
    punting_i20 = 0.0
    punting_lng = 0.0
    punting_pts = 0.0
    punting_yds = 0.0

    puntret_avg = 0.0
    puntret_lng = 0.0
    puntret_ret = 0.0
    puntret_tds = 0.0

    receiving_lng    = 0.0
    receiving_rec    = 0.0
    receiving_tds    = 0.0
    receiving_twopta = 0.0
    receiving_twoptm = 0.0
    receiving_yds    = 0.0

    rushing_att    = 0.0
    rushing_lng    = 0.0
    rushing_name   = 0.0
    rushing_tds    = 0.0
    rushing_twopta = 0.0
    rushing_twoptm = 0.0
    rushing_yds    = 0.0

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

    def defense_stats(self, defense_ast, defense_ffum, defense_int, defense_sk, defense_tkl):
        self.defense_ast = defense_ast
        self.defense_ffum = defense_ffum
        self.defense_int = defense_int
        self.defense_sk = defense_sk
        self.defense_tkl = defense_tkl

    def fumbles_stats(self, fumbles_lost, fumbles_rcv, fumbles_tot, fumbles_trcv, fumbles_yds):
        self.fumbles_lost = fumbles_lost
        self.fumbles_rcv = fumbles_rcv
        self.fumbles_tot = fumbles_tot
        self.fumbles_trcv = fumbles_trcv
        self.fumbles_yds = fumbles_yds

    def kicking_stats(self, kicking_fga, kicking_fgm, kicking_fgyds, kicking_totpfg, kicking_xpa,
                      kicking_xpb, kicking_xpmade, kicking_xpmissed, kicking_xptot):
        self.kicking_fga = kicking_fga
        self.kicking_fgm = kicking_fgm
        self.kicking_fgyds = kicking_fgyds
        self.kicking_totpfg = kicking_totpfg
        self.kicking_xpa = kicking_xpa
        self.kicking_xpb = kicking_xpb
        self.kicking_xpmade = kicking_xpmade
        self.kicking_xpmissed = kicking_xpmissed
        self.kicking_xptot = kicking_xptot

    def kickret_stats(self, kickret_avg, kickret_lng, kickret_ret,kickret_tds):
        self.kickret_avg = kickret_avg
        self.kickret_lng = kickret_lng
        self.kickret_ret = kickret_ret
        self.kickret_tds = kickret_tds


    def passing_stats(self, passing_att, passing_cmp, passing_ints, passing_tds,
                      passing_twopta, passing_twoptm, passing_yds):
        self.passing_att = passing_att
        self.passing_cmp = passing_cmp
        self.passing_ints = passing_ints
        self.passing_tds = passing_tds
        self.passing_twopta = passing_twopta
        self.passing_twoptm = passing_twoptm
        self.passing_yds = passing_yds

    def punting_stats(self, punting_avg, punting_i20, punting_lng, punting_pts, punting_yds):
        self.punting_avg = punting_avg
        self.punting_i20 = punting_i20
        self.punting_lng = punting_lng
        self.punting_pts = punting_pts
        self.punting_yds = punting_yds

    def puntret_stats(self, puntret_avg, puntret_lng, puntret_ret, puntret_tds):
        self.puntret_avg = puntret_avg
        self.puntret_lng = puntret_lng
        self.puntret_ret = puntret_ret
        self.puntret_tds = puntret_tds


    def receiving_stats(self, receiving_lng, receiving_rec, receiving_tds, receiving_twopta,
                        receiving_twoptm, receiving_yds):
        self.receiving_lng = receiving_lng
        self.receiving_rec = receiving_rec
        self.receiving_tds = receiving_tds
        self.receiving_twopta = receiving_twopta
        self.receiving_twoptm = receiving_twoptm
        self.receiving_yds    = receiving_yds

    def rushing_stats(self, rushing_att, rushing_lng, rushing_name, rushing_tds, rushing_twopta,
                      rushing_twoptm, rushing_yds):
        self.rushing_att = rushing_att
        self.rushing_lng = rushing_lng
        self.rushing_name = rushing_name
        self.rushing_tds = rushing_tds
        self.rushing_twopta = rushing_twopta
        self.rushing_twoptm = rushing_twoptm
        self.rushing_yds    = rushing_yds
