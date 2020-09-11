import random


class NFLTeam:
    def __init__(self, city, name, stadium):
        self.city = city
        self.name = name
        self.stadium = stadium


class Ravens(NFLTeam):
    def __init__(self):
        super().__init__(city="Baltimore", name="Ravens", stadium="M&T Bank Stadium")


class Steelers(NFLTeam):
    def __init__(self):
        super().__init__(city="Pittsburgh", name="Steelers", stadium="Heinz Field")


class Browns(NFLTeam):
    def __init__(self):
        super().__init__(city="Cleveland", name="Browns", stadium="FirstEnergy Stadium")


class Bengals(NFLTeam):
    def __init__(self):
        super().__init__(city="Cincinnati", name="Bengals", stadium="Paul Brown Stadium")


class Texans(NFLTeam):
    def __init__(self):
        super().__init__(city="Houston", name="Texans", stadium="NRG Stadium")


class Titans(NFLTeam):
    def __init__(self):
        super().__init__(city="Tennessee", name="Titans", stadium="Nissan Stadium")


class Colts(NFLTeam):
    def __init__(self):
        super().__init__(city="Indianapolis", name="Colts", stadium="Lucas Oil Stadium")


class Jaguars(NFLTeam):
    def __init__(self):
        super().__init__(city="Jacksonville", name="Jaguars", stadium="TIAA Bank Field")


class Patriots(NFLTeam):
    def __init__(self):
        super().__init__(city="New England", name="Patriots", stadium="Gillette Stadium")


class Jets(NFLTeam):
    def __init__(self):
        super().__init__(city="New York", name="Jets", stadium="MetLife Stadium")


class Dolphins(NFLTeam):
    def __init__(self):
        super().__init__(city="Miami", name="Dolphins", stadium="Hard Rock Stadium")


class Bills(NFLTeam):
    def __init__(self):
        super().__init__(city="Buffalo", name="Bills", stadium="Bills Stadium")


class Raiders(NFLTeam):
    def __init__(self):
        super().__init__(city="Las Vegas", name="Raiders", stadium="Allegiant Stadium")


class Chiefs(NFLTeam):
    def __init__(self):
        super().__init__(city="Kansas City", name="Chiefs", stadium="Arrowhead Stadium")


class Chargers(NFLTeam):
    def __init__(self):
        super().__init__(city="Los Angeles", name="Chargers", stadium="SoFi Stadium")


class Broncos(NFLTeam):
    def __init__(self):
        super().__init__(city="Denver", name="Broncos", stadium="Empower Field at Mile High")


class Packers(NFLTeam):
    def __init__(self):
        super().__init__(city="Green Bay", name="Packers", stadium="Lambeau Field")


class Vikings(NFLTeam):
    def __init__(self):
        super().__init__(city="Minnesota", name="Vikings", stadium="U.S. Bank Stadium")


class Bears(NFLTeam):
    def __init__(self):
        super().__init__(city="Chicago", name="Bears", stadium="Soldier Field")


class Lions(NFLTeam):
    def __init__(self):
        super().__init__(city="Detroit", name="Lions", stadium="Ford Field")


class Saints(NFLTeam):
    def __init__(self):
        super().__init__(city="New Orleans", name="Saints", stadium="Mercedes-Benz Superdome")


class Falcons(NFLTeam):
    def __init__(self):
        super().__init__(city="Atlanta", name="Falcons", stadium="Mercedes-Benz Stadium")


class Buccaneers(NFLTeam):
    def __init__(self):
        super().__init__(city="Tampa Bay", name="Buccaneers", stadium="Raymond James Stadium")


class Panthers(NFLTeam):
    def __init__(self):
        super().__init__(city="Carolina", name="Panthers", stadium="Bank of America Stadium")


class Eagles(NFLTeam):
    def __init__(self):
        super().__init__(city="Philadelphia", name="Eagles", stadium="Lincoln Financial Field")


class Giants(NFLTeam):
    def __init__(self):
        super().__init__(city="New York", name="Giants", stadium="MetLife Stadium")


class WashingtonFootballTeam(NFLTeam):
    def __init__(self):
        super().__init__(city="Washington", name="Football Team", stadium="FedExField")


class Cowboys(NFLTeam):
    def __init__(self):
        super().__init__(city="Dallas", name="Cowboys", stadium="AT&T Stadium")


class FortyNiners(NFLTeam):
    def __init__(self):
        super().__init__(city="San Francisco", name="49ers", stadium="Levi's Stadium")


class Seahawks(NFLTeam):
    def __init__(self):
        super().__init__(city="Seattle", name="Seahawks", stadium="CenturyLink Field")


class Rams(NFLTeam):
    def __init__(self):
        super().__init__(city="Los Angeles", name="Rams", stadium="SoFi Stadium")


class Cardinals(NFLTeam):
    def __init__(self):
        super().__init__(city="Arizona", name="Cardinals", stadium="State Farm Stadium")


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
team_1 = vs_teams[0]
team_2 = vs_teams[1]
print(f"Matchup:  {team_1.city} {team_1.name} vs. {team_2.city} {team_2.name}")
print(f"Location: {team_2.stadium}")
