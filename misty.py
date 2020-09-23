import random

from team_data import Ravens, Steelers, Browns, Bengals, Texans, Titans, Colts, Jaguars, Patriots, Jets, Dolphins, \
    Bills, Chiefs, Broncos, Raiders, Chargers, Packers, Vikings, Bears, Lions, Saints, Falcons, Buccaneers, Panthers, \
    Eagles, Giants, WashingtonFootballTeam, Cowboys, FortyNiners, Seahawks, Rams, Cardinals
from utils import NFLStatUtils

nfl = {
    "AFC": {
        "North": [Ravens(), Steelers(), Browns(), Bengals()],
        "South": [Texans(), Titans(), Colts(), Jaguars()],
        "East": [Patriots(), Jets(), Dolphins(), Bills()],
        "West": [Raiders(), Chiefs(), Chargers(), Broncos()],
    },
    "NFC": {
        "North": [Packers(), Vikings(), Bears(), Lions()],
        "South": [Saints(), Falcons(), Buccaneers(), Panthers()],
        "East": [Eagles(), Giants(), WashingtonFootballTeam(), Cowboys()],
        "West": [FortyNiners(), Seahawks(), Rams(), Cardinals()],
    },
}
afc = list(list(nfl.values())[0].values())
nfc = list(list(nfl.values())[1].values())
flattened_afc = [divisional_team for division in afc for divisional_team in division]
flattened_nfc = [divisional_team for division in nfc for divisional_team in division]
all_teams = flattened_afc + flattened_nfc
vs_teams = random.sample(all_teams, 2)
away_team = vs_teams[0]
home_team = vs_teams[1]
# home_team = nfl["AFC"]["East"][1]  # New York Jets, 7 - 9 record
# away_team = nfl["AFC"]["South"][2]  # Indianapolis Colts, 7 - 9 record

winner = NFLStatUtils.calculate_predicted_winner(away_team, home_team)

point_spread = NFLStatUtils.calculate_point_spread(away_team, home_team)

msg = (f"{'Matchup:':<30}{away_team.city} {away_team.name} vs. {home_team.city} {home_team.name}\n"
       f"{'Location:':<30}{home_team.stadium}; {home_team.stadium_location}\n"
       f"{f'{away_team.name} 2019 record:':<30}{away_team.record_2019[0]}-{away_team.record_2019[1]}-{away_team.record_2019[2]}\n"
       f"{f'{home_team.name} 2019 record:':<30}{home_team.record_2019[0]}-{home_team.record_2019[1]}-{home_team.record_2019[2]}\n"
       f"{'Predicted winner:':<30}{winner.name}\n"
       f"{'Point spread:':<30}{point_spread}")

print(msg)
