class NFLStatUtils:
    @staticmethod
    def calculate_predicted_winner(away_team, home_team):
        """Calculate the predicted winner of a given matchup between two teams.
        :param away_team: The away team.
        :param home_team: The home team.
        """
        away_team_wins = away_team.record_2019[0]
        home_team_wins = home_team.record_2019[0]
        if home_team_wins >= away_team_wins:
            return home_team
        elif home_team_wins < away_team_wins:
            return away_team

    @staticmethod
    def calculate_point_spread(away_team, home_team):
        point_spread = abs(away_team.record_2019[0] - home_team.record_2019[0])
        if point_spread == 0:
            point_spread += 1
        return point_spread
