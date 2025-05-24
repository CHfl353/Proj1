import random
from analysis import generate_enhanced_analysis

def predict_enhanced_matches(standings, matches):
    teams = [team['name'] for team in standings]
    existing = set(f"{m['home']}-{m['away']}" for m in matches)
    predictions = []
    analyses = {team['name']: generate_enhanced_analysis(team, standings) for team in standings}
    for i, home in enumerate(teams):
        for j, away in enumerate(teams):
            if i != j and f"{home}-{away}" not in existing:
                ha, aa = analyses[home], analyses[away]
                homeStrength = (
                    ha['formScore'] * 0.3 + ha['offensiveScore'] * 0.25 + ha['defensiveScore'] * 0.25 +
                    ha['disciplineScore'] * 0.1 + ha['mentalStrength'] * 0.1 + 0.2
                )
                awayStrength = (
                    aa['formScore'] * 0.3 + aa['offensiveScore'] * 0.25 + aa['defensiveScore'] * 0.25 +
                    aa['disciplineScore'] * 0.1 + aa['mentalStrength'] * 0.1
                )
                diff = homeStrength - awayStrength
                rand = (random.random() - 0.5) * 0.4
                if diff + rand > 0.3:
                    homeGoals = max(1, round(2 + ha['offensiveScore'] * 2 + random.random()))
                    awayGoals = max(0, round(aa['offensiveScore'] * 1.5 + random.random() * 0.8))
                elif diff + rand < -0.3:
                    homeGoals = max(0, round(ha['offensiveScore'] * 1.5 + random.random() * 0.8))
                    awayGoals = max(1, round(2 + aa['offensiveScore'] * 2 + random.random()))
                else:
                    homeGoals = max(0, round(1 + ha['offensiveScore'] + random.random()))
                    awayGoals = max(0, round(1 + aa['offensiveScore'] + random.random()))
                redProb = (2 - ha['disciplineScore'] - aa['disciplineScore']) * 0.1
                willRed = random.random() < redProb
                predictions.append({
                    'home': home, 'away': away, 'homeGoals': homeGoals, 'awayGoals': awayGoals,
                    'willHaveRedCard': willRed, 'confidence': abs(diff) * 100
                })
    return predictions

def calculate_final_standings(current, predictions):
    teams = {team['name']: dict(team) for team in current}
    for m in predictions:
        teams[m['home']]['played'] += 1
        teams[m['away']]['played'] += 1
        teams[m['home']]['goalsFor'] += m['homeGoals']
        teams[m['home']]['goalsAgainst'] += m['awayGoals']
        teams[m['away']]['goalsFor'] += m['awayGoals']
        teams[m['away']]['goalsAgainst'] += m['homeGoals']
        if m['homeGoals'] > m['awayGoals']:
            teams[m['home']]['wins'] += 1
            teams[m['home']]['points'] += 3
            teams[m['away']]['losses'] += 1
        elif m['homeGoals'] < m['awayGoals']:
            teams[m['away']]['wins'] += 1
            teams[m['away']]['points'] += 3
            teams[m['home']]['losses'] += 1
        else:
            teams[m['home']]['draws'] += 1
            teams[m['home']]['points'] += 1
            teams[m['away']]['draws'] += 1
            teams[m['away']]['points'] += 1
    for team in teams.values():
        team['goalDiff'] = team['goalsFor'] - team['goalsAgainst']
    return sorted(teams.values(), key=lambda t: (-t['points'], -t['goalDiff'], -t['goalsFor']))