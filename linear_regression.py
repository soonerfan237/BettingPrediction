import get_inputs
import pandasql as ps

def linear_regression(input_file):

    bettinglines = get_inputs.get_bettinglines_df(input_file)
    bettinglines = bettinglines[["Date", "Home Team", "Away Team", "Home Score", "Away Score"]]
    bettinglines = bettinglines.rename(columns={'Home Team': 'HomeTeam', 'Away Team': 'AwayTeam', 'Home Score': 'HomeScore', 'Away Score': 'AwayScore'})
    #TODO: alias team names to account for relocations
    query_avg_home_offense = """SELECT HomeTeam, avg(HomeScore) as avg_HomeScore FROM bettinglines group by HomeTeam"""
    avg_home_offense = ps.sqldf(query_avg_home_offense, locals())
    query_avg_away_offense = """SELECT AwayTeam, avg(AwayScore) as avg_AwayScore FROM bettinglines group by AwayTeam"""
    avg_away_offense = ps.sqldf(query_avg_away_offense, locals())

    query_join_bettinglines = """SELECT bl.*, avg_HomeScore, avg_AwayScore 
    FROM bettinglines bl
    LEFT JOIN avg_home_offense aho on bl.HomeTeam=aho.HomeTeam
    LEFT JOIN avg_away_offense aao on bl.HomeTeam=aao.AwayTeam"""

    bettlinglines2 = ps.sqldf(query_join_bettinglines, locals())

    for row in bettinglines:
        bettinglines_hometeam_homegames = bettinglines[bettinglines.HomeTeam.eq(row["HomeTeam"])] #filtering data frame for just historical home games related to the current rows home team
        mean = bettinglines_hometeam_homegames.HomeScore.mean()
        print("loop")
    query_teams = """SELECT distinct HomeTeam FROM bettinglines"""
    teams = ps.sqldf(query_teams, locals())
    for team in teams["HomeTeam"]:
        bettinglines2 = bettinglines[bettinglines.HomeTeam.eq(team)]
        print("loop")
    print("done")

    return