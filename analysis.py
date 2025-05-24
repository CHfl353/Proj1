def calculate_advanced_standings(matches):
    teams = {}
    for match in matches:
        for team_name in [match['home'], match['away']]:
            if team_name not in teams:
                teams[team_name] = {
                    'name': team_name, 'played': 0, 'wins': 0, 'draws': 0, 'losses': 0,
                    'goalsFor': 0, 'goalsAgainst': 0, 'goalDiff': 0, 'points': 0,
                    'earlyGoals': 0, 'lateGoals': 0, 'firstHalfGoals': 0, 'secondHalfGoals': 0,
                    'redCardsFor': 0, 'redCardsAgainst': 0,
                    'matchesWithRedCards': 0, 'pointsWithRedCards': 0, 'pointsWithoutRedCards': 0,
                    'gamesWithRedCards': 0, 'gamesWithoutRedCards': 0,
                    'averageGoalsFor': 0, 'averageGoalsAgainst': 0,
                    'comebacks': 0, 'collapsesToDefeat': 0
                }
    for match in matches:
        home, away = teams[match['home']], teams[match['away']]
        home['played'] += 1
        away['played'] += 1
        home['goalsFor'] += match['homeGoals']
        home['goalsAgainst'] += match['awayGoals']
        away['goalsFor'] += match['awayGoals']
        away['goalsAgainst'] += match['homeGoals']

        for goal in match['goals']:
            team = home if goal['team'] == 'home' else away
            if goal['minute'] <= 15: team['earlyGoals'] += 1
            if goal['minute'] >= 75: team['lateGoals'] += 1
            if goal['minute'] <= 45: team['firstHalfGoals'] += 1
            else: team['secondHalfGoals'] += 1

        home_red = sum(1 for c in match['redCards'] if c['team'] == 'home')
        away_red = sum(1 for c in match['redCards'] if c['team'] == 'away')
        home['redCardsFor'] += home_red
        home['redCardsAgainst'] += away_red
        away['redCardsFor'] += away_red
        away['redCardsAgainst'] += home_red
        matchHasRed = home_red > 0 or away_red > 0

        # Points and results
        homePoints = awayPoints = 0
        if match['homeGoals'] > match['awayGoals']:
            home['wins'] += 1
            away['losses'] += 1
            homePoints = 3
        elif match['homeGoals'] < match['awayGoals']:
            away['wins'] += 1
            home['losses'] += 1
            awayPoints = 3
        else:
            home['draws'] += 1
            away['draws'] += 1
            homePoints = awayPoints = 1
        home['points'] += homePoints
        away['points'] += awayPoints

        if matchHasRed:
            home['matchesWithRedCards'] += 1
            away['matchesWithRedCards'] += 1
            home['pointsWithRedCards'] += homePoints
            away['pointsWithRedCards'] += awayPoints
            home['gamesWithRedCards'] += 1
            away['gamesWithRedCards'] += 1
        else:
            home['pointsWithoutRedCards'] += homePoints
            away['pointsWithoutRedCards'] += awayPoints
            home['gamesWithoutRedCards'] += 1
            away['gamesWithoutRedCards'] += 1

        # Comebacks/collapses
        home_leading = away_leading = 0
        home_score = away_score = 0
        for goal in match['goals']:
            if goal['team'] == "home":
                home_score += 1
                if home_score > away_score and away_leading > 0:
                    home['comebacks'] += 1
                    away['collapsesToDefeat'] += 1
                home_leading = int(home_score > away_score)
                away_leading = 0
            else:
                away_score += 1
                if away_score > home_score and home_leading > 0:
                    away['comebacks'] += 1
                    home['collapsesToDefeat'] += 1
                away_leading = int(away_score > home_score)
                home_leading = 0

    for team in teams.values():
        team['goalDiff'] = team['goalsFor'] - team['goalsAgainst']
        team['averageGoalsFor'] = team['goalsFor'] / team['played'] if team['played'] else 0
        team['averageGoalsAgainst'] = team['goalsAgainst'] / team['played'] if team['played'] else 0
    return sorted(teams.values(), key=lambda t: (-t['points'], -t['goalDiff'], -t['goalsFor']))

def generate_enhanced_analysis(team, standings):
    position = [t['name'] for t in standings].index(team['name']) + 1
    formScore = (team['wins'] * 3 + team['draws']) / (team['played'] * 3) if team['played'] else 0
    form = "Excellent" if formScore >= 0.7 else "Good" if formScore >= 0.5 else "Average" if formScore >= 0.3 else "Poor"
    early = team['earlyGoals'] / team['goalsFor'] if team['goalsFor'] else 0
    late = team['lateGoals'] / team['goalsFor'] if team['goalsFor'] else 0
    firstHalf = team['firstHalfGoals'] / team['goalsFor'] if team['goalsFor'] else 0
    redCardImpact = ((team['pointsWithRedCards'] / team['gamesWithRedCards']) if team['gamesWithRedCards'] else 0) - \
                    ((team['pointsWithoutRedCards'] / team['gamesWithoutRedCards']) if team['gamesWithoutRedCards'] else 0)
    discipline = max(0, 1 - (team['redCardsFor'] / max(team['played'], 1)) * 2)
    mental = ((team['comebacks'] - team['collapsesToDefeat']) / team['played']) if team['played'] else 0
    defense = max(0, 1 - (team['goalsAgainst'] / team['played']) / 3) if team['played'] else 0
    offense = min(1, (team['goalsFor'] / team['played']) / 3) if team['played'] else 0
    consistency = max(0, 1 - abs(team['wins'] - team['losses']) / team['played'] * 0.5) if team['played'] else 0
    return {
        'position': position, 'form': form, 'formScore': min(max(formScore, 0), 1),
        'defensiveScore': min(max(defense, 0), 1), 'offensiveScore': min(max(offense, 0), 1),
        'consistencyScore': min(max(consistency, 0), 1), 'disciplineScore': min(max(discipline, 0), 1),
        'mentalStrength': min(max((mental + 1) / 2, 0), 1), 'earlyGoalRatio': early, 'lateGoalRatio': late, 
        'firstHalfRatio': firstHalf, 'redCardImpact': redCardImpact,
        'timingStrength': (early + late) / 2,
        'seasonPrediction': (
            "Title contender" if position <= 2 else
            "Top 4 finish" if position <= 4 else
            "Mid-table finish" if position <= 6 else
            "Lower-table finish"
        )
    }