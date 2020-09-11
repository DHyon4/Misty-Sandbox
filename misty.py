import math
import random


class NFLTeam:
    def __init__(self, city, name, stadium, record_2019):
        self.city = city
        self.name = name
        self.stadium = stadium
        self.record_2019 = record_2019


class Ravens(NFLTeam):
    def __init__(self):
        super().__init__(city="Baltimore",
                         name="Ravens",
                         stadium="M&T Bank Stadium",
                         record_2019=(14, 2, 0))


class Steelers(NFLTeam):
    def __init__(self):
        super().__init__(city="Pittsburgh",
                         name="Steelers",
                         stadium="Heinz Field",
                         record_2019=(8, 8, 0))


class Browns(NFLTeam):
    def __init__(self):
        super().__init__(city="Cleveland",
                         name="Browns",
                         stadium="FirstEnergy Stadium",
                         record_2019=(6, 10, 0))


class Bengals(NFLTeam):
    def __init__(self):
        super().__init__(city="Cincinnati",
                         name="Bengals",
                         stadium="Paul Brown Stadium",
                         record_2019=(2, 14, 0))


class Texans(NFLTeam):
    def __init__(self):
        super().__init__(city="Houston",
                         name="Texans",
                         stadium="NRG Stadium",
                         record_2019=(10, 6, 0))


class Titans(NFLTeam):
    def __init__(self):
        super().__init__(city="Tennessee",
                         name="Titans",
                         stadium="Nissan Stadium",
                         record_2019=(9, 7, 0))


class Colts(NFLTeam):
    def __init__(self):
        super().__init__(city="Indianapolis",
                         name="Colts",
                         stadium="Lucas Oil Stadium",
                         record_2019=(7, 9, 0))


class Jaguars(NFLTeam):
    def __init__(self):
        super().__init__(city="Jacksonville",
                         name="Jaguars",
                         stadium="TIAA Bank Field",
                         record_2019=(6, 10, 0))


class Patriots(NFLTeam):
    def __init__(self):
        super().__init__(city="New England",
                         name="Patriots",
                         stadium="Gillette Stadium",
                         record_2019=(12, 4, 0))


class Jets(NFLTeam):
    def __init__(self):
        super().__init__(city="New York",
                         name="Jets",
                         stadium="MetLife Stadium",
                         record_2019=(7, 9, 0))


class Dolphins(NFLTeam):
    def __init__(self):
        super().__init__(city="Miami",
                         name="Dolphins",
                         stadium="Hard Rock Stadium",
                         record_2019=(5, 11, 0))


class Bills(NFLTeam):
    def __init__(self):
        super().__init__(city="Buffalo",
                         name="Bills",
                         stadium="Bills Stadium",
                         record_2019=(10, 6, 0))


class Chiefs(NFLTeam):
    def __init__(self):
        super().__init__(city="Kansas City",
                         name="Chiefs",
                         stadium="Arrowhead Stadium",
                         record_2019=(12, 4, 0))


class Broncos(NFLTeam):
    def __init__(self):
        super().__init__(city="Denver",
                         name="Broncos",
                         stadium="Empower Field at Mile High",
                         record_2019=(7, 9, 0))


class Raiders(NFLTeam):
    def __init__(self):
        super().__init__(city="Las Vegas",
                         name="Raiders",
                         stadium="Allegiant Stadium",
                         record_2019=(7, 9, 0))


class Chargers(NFLTeam):
    def __init__(self):
        super().__init__(city="Los Angeles",
                         name="Chargers",
                         stadium="SoFi Stadium",
                         record_2019=(5, 11, 0))


class Packers(NFLTeam):
    def __init__(self):
        super().__init__(city="Green Bay",
                         name="Packers",
                         stadium="Lambeau Field",
                         record_2019=(13, 3, 0))


class Vikings(NFLTeam):
    def __init__(self):
        super().__init__(city="Minnesota",
                         name="Vikings",
                         stadium="U.S. Bank Stadium",
                         record_2019=(10, 6, 0))


class Bears(NFLTeam):
    def __init__(self):
        super().__init__(city="Chicago",
                         name="Bears",
                         stadium="Soldier Field",
                         record_2019=(8, 8, 0))


class Lions(NFLTeam):
    def __init__(self):
        super().__init__(city="Detroit",
                         name="Lions",
                         stadium="Ford Field",
                         record_2019=(3, 12, 1))


class Saints(NFLTeam):
    def __init__(self):
        super().__init__(city="New Orleans",
                         name="Saints",
                         stadium="Mercedes-Benz Superdome",
                         record_2019=(13, 3, 0))


class Falcons(NFLTeam):
    def __init__(self):
        super().__init__(city="Atlanta",
                         name="Falcons",
                         stadium="Mercedes-Benz Stadium",
                         record_2019=(7, 9, 0))


class Buccaneers(NFLTeam):
    def __init__(self):
        super().__init__(city="Tampa Bay",
                         name="Buccaneers",
                         stadium="Raymond James Stadium",
                         record_2019=(7, 9, 0))


class Panthers(NFLTeam):
    def __init__(self):
        super().__init__(city="Carolina",
                         name="Panthers",
                         stadium="Bank of America Stadium",
                         record_2019=(5, 11, 0))


class Eagles(NFLTeam):
    def __init__(self):
        super().__init__(city="Philadelphia",
                         name="Eagles",
                         stadium="Lincoln Financial Field",
                         record_2019=(9, 7, 0))


class Giants(NFLTeam):
    def __init__(self):
        super().__init__(city="New York",
                         name="Giants",
                         stadium="MetLife Stadium",
                         record_2019=(4, 12, 0))


class WashingtonFootballTeam(NFLTeam):
    def __init__(self):
        super().__init__(city="Washington",
                         name="Football Team",
                         stadium="FedExField",
                         record_2019=(3, 13, 0))


class Cowboys(NFLTeam):
    def __init__(self):
        super().__init__(city="Dallas",
                         name="Cowboys",
                         stadium="AT&T Stadium",
                         record_2019=(8, 8, 0))


class FortyNiners(NFLTeam):
    def __init__(self):
        super().__init__(city="San Francisco",
                         name="49ers",
                         stadium="Levi's Stadium",
                         record_2019=(13, 3, 0))


class Seahawks(NFLTeam):
    def __init__(self):
        super().__init__(city="Seattle",
                         name="Seahawks",
                         stadium="CenturyLink Field",
                         record_2019=(11, 5, 0))


class Rams(NFLTeam):
    def __init__(self):
        super().__init__(city="Los Angeles",
                         name="Rams",
                         stadium="SoFi Stadium",
                         record_2019=(9, 7, 0))


class Cardinals(NFLTeam):
    def __init__(self):
        super().__init__(city="Arizona",
                         name="Cardinals",
                         stadium="State Farm Stadium",
                         record_2019=(5, 10, 1))


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


def calculate_prediction():
    """Calculate the predicted outcome of a given matchup between two teams."""
    raw_prediction = away_team.record_2019[0] / (home_team.record_2019[0] + 2)
    # the + 2 represents home field advantage
    final_prediction = math.ceil(raw_prediction)
    return final_prediction


prediction = calculate_prediction()

if prediction > 1:
    winner = away_team
else:
    winner = home_team

msg = (f"Matchup:\t\t\t\t{away_team.city} {away_team.name} vs. {home_team.city} {home_team.name}\n"
       f"Location:\t\t\t\t{home_team.stadium}\n"
       f"Predicted winner:\t\t{winner.name} by {prediction}")

print(msg)
