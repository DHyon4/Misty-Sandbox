from team_data import NFLTeam


class NFLStatUtils:
    @staticmethod
    def calculate_predicted_winner(away_team: NFLTeam, home_team: NFLTeam):
        """Calculate the predicted winner of a given matchup between two teams.
        :param away_team: The away team.
        :param home_team: The home team.
        """
        away_team_wins = away_team.record_2019[0]
        home_team_wins = home_team.record_2019[0]
        # if home_team.QBR >= away_team.QBR:
        #     home_team_wins += 1
        # elif home_team.QBR < away_team.QBR:
        #     away_team_wins += 1
        if home_team.has_playoff_experience:
            home_team_wins = +0.75
        if away_team.has_playoff_experience:
            away_team_wins += 0.74

        if home_team_wins >= away_team_wins:
            # home field advantage is if both teams have equal records, the home team will win
            return home_team
        elif home_team_wins < away_team_wins:
            return away_team

    @staticmethod
    def calculate_point_spread(away_team, home_team):
        point_spread = abs(away_team.record_2019[0] - home_team.record_2019[0])
        if point_spread == 0:
            point_spread += 1
        return point_spread
