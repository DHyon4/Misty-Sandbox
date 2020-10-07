class NFLTeam:
    def __init__(self, city, name, stadium, stadium_location, record_2019):
        self.city = city
        self.name = name
        self.stadium = stadium
        self.stadium_location = stadium_location
        self.record_2019 = record_2019


class Ravens(NFLTeam):
    def __init__(self):
        super().__init__(city="Baltimore",
                         name="Ravens",
                         stadium="M&T Bank Stadium",
                         stadium_location="Baltimore, Maryland",
                         record_2019=(14, 2, 0))


class Steelers(NFLTeam):
    def __init__(self):
        super().__init__(city="Pittsburgh",
                         name="Steelers",
                         stadium="Heinz Field",
                         stadium_location="Pittsburgh, Pennsylvania",
                         record_2019=(8, 8, 0))


class Browns(NFLTeam):
    def __init__(self):
        super().__init__(city="Cleveland",
                         name="Browns",
                         stadium="FirstEnergy Stadium",
                         stadium_location="Cleveland, Ohio",
                         record_2019=(6, 10, 0))


class Bengals(NFLTeam):
    def __init__(self):
        super().__init__(city="Cincinnati",
                         name="Bengals",
                         stadium="Paul Brown Stadium",
                         stadium_location="Cincinnati, Ohio",
                         record_2019=(2, 14, 0))


class Texans(NFLTeam):
    def __init__(self):
        super().__init__(city="Houston",
                         name="Texans",
                         stadium="NRG Stadium",
                         stadium_location="Houston, Texas",
                         record_2019=(10, 6, 0))


class Titans(NFLTeam):
    def __init__(self):
        super().__init__(city="Tennessee",
                         name="Titans",
                         stadium="Nissan Stadium",
                         stadium_location="Nashville, Tennessee",
                         record_2019=(9, 7, 0))


class Colts(NFLTeam):
    def __init__(self):
        super().__init__(city="Indianapolis",
                         name="Colts",
                         stadium="Lucas Oil Stadium",
                         stadium_location="Indianapolis, Indiana",
                         record_2019=(7, 9, 0))


class Jaguars(NFLTeam):
    def __init__(self):
        super().__init__(city="Jacksonville",
                         name="Jaguars",
                         stadium="TIAA Bank Field",
                         stadium_location="Jacksonville, Florida",
                         record_2019=(6, 10, 0))


class Patriots(NFLTeam):
    def __init__(self):
        super().__init__(city="New England",
                         name="Patriots",
                         stadium="Gillette Stadium",
                         stadium_location="Foxborough, Massachusetts",
                         record_2019=(12, 4, 0))


class Jets(NFLTeam):
    def __init__(self):
        super().__init__(city="New York",
                         name="Jets",
                         stadium="MetLife Stadium",
                         stadium_location="East Rutherford, New Jersey",
                         record_2019=(7, 9, 0))


class Dolphins(NFLTeam):
    def __init__(self):
        super().__init__(city="Miami",
                         name="Dolphins",
                         stadium="Hard Rock Stadium",
                         stadium_location="Miami Gardens, Florida",
                         record_2019=(5, 11, 0))


class Bills(NFLTeam):
    def __init__(self):
        super().__init__(city="Buffalo",
                         name="Bills",
                         stadium="Bills Stadium",
                         stadium_location="Orchard Park, New York",
                         record_2019=(10, 6, 0))


class Chiefs(NFLTeam):
    def __init__(self):
        super().__init__(city="Kansas City",
                         name="Chiefs",
                         stadium="Arrowhead Stadium",
                         stadium_location="Kansas City, Missouri",
                         record_2019=(12, 4, 0))


class Broncos(NFLTeam):
    def __init__(self):
        super().__init__(city="Denver",
                         name="Broncos",
                         stadium="Empower Field at Mile High",
                         stadium_location="Denver, Colorado",
                         record_2019=(7, 9, 0))


class Raiders(NFLTeam):
    def __init__(self):
        super().__init__(city="Las Vegas",
                         name="Raiders",
                         stadium="Allegiant Stadium",
                         stadium_location="Paradise, Nevada",
                         record_2019=(7, 9, 0))


class Chargers(NFLTeam):
    def __init__(self):
        super().__init__(city="Los Angeles",
                         name="Chargers",
                         stadium="SoFi Stadium",
                         stadium_location="Inglewood, California",
                         record_2019=(5, 11, 0))


class Packers(NFLTeam):
    def __init__(self):
        super().__init__(city="Green Bay",
                         name="Packers",
                         stadium="Lambeau Field",
                         stadium_location="Green Bay, Wisconsin",
                         record_2019=(13, 3, 0))


class Vikings(NFLTeam):
    def __init__(self):
        super().__init__(city="Minnesota",
                         name="Vikings",
                         stadium="U.S. Bank Stadium",
                         stadium_location="Minneapolis, Minnesota",
                         record_2019=(10, 6, 0))


class Bears(NFLTeam):
    def __init__(self):
        super().__init__(city="Chicago",
                         name="Bears",
                         stadium="Soldier Field",
                         stadium_location="Chicago, Illinois",
                         record_2019=(8, 8, 0))


class Lions(NFLTeam):
    def __init__(self):
        super().__init__(city="Detroit",
                         name="Lions",
                         stadium="Ford Field",
                         stadium_location="Detroit, Michigan",
                         record_2019=(3, 12, 1))


class Saints(NFLTeam):
    def __init__(self):
        super().__init__(city="New Orleans",
                         name="Saints",
                         stadium="Mercedes-Benz Superdome",
                         stadium_location="New Orleans, Louisiana",
                         record_2019=(13, 3, 0))


class Falcons(NFLTeam):
    def __init__(self):
        super().__init__(city="Atlanta",
                         name="Falcons",
                         stadium="Mercedes-Benz Stadium",
                         stadium_location="Atlanta, Georgia",
                         record_2019=(7, 9, 0))


class Buccaneers(NFLTeam):
    def __init__(self):
        super().__init__(city="Tampa Bay",
                         name="Buccaneers",
                         stadium="Raymond James Stadium",
                         stadium_location="Tampa, Florida",
                         record_2019=(7, 9, 0))


class Panthers(NFLTeam):
    def __init__(self):
        super().__init__(city="Carolina",
                         name="Panthers",
                         stadium="Bank of America Stadium",
                         stadium_location="Charlotte, North Carolina",
                         record_2019=(5, 11, 0))


class Eagles(NFLTeam):
    def __init__(self):
        super().__init__(city="Philadelphia",
                         name="Eagles",
                         stadium="Lincoln Financial Field",
                         stadium_location="Philadelphia, Pennsylvania",
                         record_2019=(9, 7, 0))


class Giants(NFLTeam):
    def __init__(self):
        super().__init__(city="New York",
                         name="Giants",
                         stadium="MetLife Stadium",
                         stadium_location="East Rutherford, New Jersey",
                         record_2019=(4, 12, 0))


class WashingtonFootballTeam(NFLTeam):
    def __init__(self):
        super().__init__(city="Washington",
                         name="Football Team",
                         stadium="FedExField",
                         stadium_location="Landover, Maryland",
                         record_2019=(3, 13, 0))


class Cowboys(NFLTeam):
    def __init__(self):
        super().__init__(city="Dallas",
                         name="Cowboys",
                         stadium="AT&T Stadium",
                         stadium_location="Arlington, Texas",
                         record_2019=(8, 8, 0))


class FortyNiners(NFLTeam):
    def __init__(self):
        super().__init__(city="San Francisco",
                         name="49ers",
                         stadium="Levi's Stadium",
                         stadium_location="Santa Clara, California",
                         record_2019=(13, 3, 0))


class Seahawks(NFLTeam):
    def __init__(self):
        super().__init__(city="Seattle",
                         name="Seahawks",
                         stadium="CenturyLink Field",
                         stadium_location="Seattle, Washington",
                         record_2019=(11, 5, 0))


class Rams(NFLTeam):
    def __init__(self):
        super().__init__(city="Los Angeles",
                         name="Rams",
                         stadium="SoFi Stadium",
                         stadium_location="Inglewood, California",
                         record_2019=(9, 7, 0))


class Cardinals(NFLTeam):
    def __init__(self):
        super().__init__(city="Arizona",
                         name="Cardinals",
                         stadium="State Farm Stadium",
                         stadium_location="Glendale, Arizona",
                         record_2019=(5, 10, 1))
