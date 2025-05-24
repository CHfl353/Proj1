import re

def read_matches(filename):
    matches = []
    with open(filename, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]
        match_header = re.match(r'^(.+?)\s+(\d+)\s*-\s*(\d+)\s+(.+)$', line)
        if match_header:
            home, homeGoals, awayGoals, away = match_header.groups()
            homeGoals, awayGoals = int(homeGoals), int(awayGoals)
            i += 1
            goals = []
            redCards = []
            while i < len(lines):
                l = lines[i]
                # Red card
                rc = re.match(r'^(\d+)\s*Minute\s*Red Card\s+(.+)$', l, re.IGNORECASE)
                if rc:
                    minute, team = int(rc.group(1)), rc.group(2).strip()
                    redCards.append({"minute": minute, "team": "home" if team == home.strip() else "away"})
                    i += 1
                    continue
                # Goal
                goal = re.match(r'^(\d+)\s*-\s*(\d+)\s+(\d+)\s*Minute', l, re.IGNORECASE)
                if goal:
                    score1, score2, minute = int(goal.group(1)), int(goal.group(2)), int(goal.group(3))
                    # Figure out which team scored
                    if score1 > score2:
                        scorer = "home"
                    elif score2 > score1:
                        scorer = "away"
                    else:  # Draw? Use previous state or skip
                        scorer = None
                    if scorer:
                        goals.append({"minute": minute, "team": scorer})
                    i += 1
                    continue
                # 0 - 0 result, or line does not match expected, break
                if not l or re.match(r'^.+?\s+\d+\s*-\s*\d+\s+.+$', l):
                    break
                i += 1
            matches.append({
                "home": home.strip(),
                "away": away.strip(),
                "homeGoals": homeGoals,
                "awayGoals": awayGoals,
                "goals": goals,
                "redCards": redCards
            })
        else:
            i += 1
    return matches