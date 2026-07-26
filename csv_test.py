import csv


teamA = []
teamB = []


# Read players from the CSV file
with open("./match_stats.csv", "r", encoding="utf-8", newline="") as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        if row[1] == "TEAM-A":
            teamA.append(row)

        elif row[1] == "TEAM-B":
            teamB.append(row)


def calculate_mvp_score(player):
    """Calculate the MVP score of one player."""

    return (
        player[0]
        + (player[1] * 1.5)
        + (player[2] * 2)
        + (player[4] * 1.2)
        - (player[3] * 1.5)
    )


def find_max_score(scores):
    """Find the highest MVP score and its list index."""

    if len(scores) == 0:
        return None, None

    max_score = scores[0]
    max_index = 0

    for index in range(1, len(scores)):
        if scores[index] > max_score:
            max_score = scores[index]
            max_index = index

    return max_score, 

def calculate_average_score(scores):
    """Calculate the average MVP score."""

    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


def abbreviate_name(full_name):
    """Create an abbreviation from the player's full name."""

    words = full_name.split()
    abbreviation = ""

    for word in words:
        abbreviation = abbreviation + word[0]

    return abbreviation.upper()


# Combine the players of both teams
all_players = teamA + teamB

# This list stores every calculated MVP score
all_mvp_scores = []


# Calculate the MVP score of every player
for player in all_players:
    player_stats = []

    player_stats.append(int(player[5]))  # Points
    player_stats.append(int(player[6]))  # Assists
    player_stats.append(int(player[7]))  # Steals
    player_stats.append(int(player[8]))  # Turnovers
    player_stats.append(int(player[9]))  # Rebounds

    result = calculate_mvp_score(player_stats)

    all_mvp_scores.append(result)

    print(f"{player[4]} MVP Score: {result:.1f}")


# Find the highest MVP score
highest_score, mvp_index = find_max_score(all_mvp_scores)


# Find the player who owns the highest score
mvp_player = all_players[mvp_index]

mvp_name = mvp_player[4]
mvp_team = mvp_player[2]
mvp_abbreviation = abbreviate_name(mvp_name)


# Print all results
print("\nAll MVP Scores:")
print(all_mvp_scores)

print("\n========== MATCH MVP ==========")
print("MVP Name:", mvp_name)
print("MVP Abbreviation:", mvp_abbreviation)
print("MVP Team:", mvp_team)
print(f"MVP Score: {highest_score:.1f}")

