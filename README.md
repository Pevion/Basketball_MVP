# Basketball MVP Calculator

## About the Project

This repository contains a Python program that calculates the Most Valuable Player (MVP) of a basketball match.

The program reads player statistics from `match_stats.csv`, calculates an MVP score for every player, and displays the player with the highest score.

The MVP score is calculated using:

- Points
- Assists
- Steals
- Rebounds
- Turnovers

Turnovers reduce the score, while the other statistics increase it.

## Features

- Reads player information from a CSV file
- Separates players into two teams
- Calculates an MVP score for every player
- Calculates the average MVP score
- Finds the player with the highest MVP score
- Creates an abbreviation from the MVP’s name
- Displays the MVP’s name, team, abbreviation, and score
- Handles an empty score list safely

## Project Files

- `csv_test.py` — contains the main Python program
- `match_stats.csv` — contains the basketball player statistics
- `.gitignore` — prevents local and sensitive files from being uploaded
- `README.md` — explains the project and how to use it

## Requirements

The project requires Python 3.

It only uses Python’s built-in `csv` module, so no external packages need to be installed.

## How to Run the Project

1. Clone the repository:

```bash
git clone YOUR-REPOSITORY-URL
```

2. Enter the project folder:

```bash
cd basketball_mvp-repo
```

3. Make sure `match_stats.csv` is in the same folder as `csv_test.py`.

4. Run the program on Windows:

```bash
python csv_test.py
```

On macOS or Linux, you may need to use:

```bash
python3 csv_test.py
```

## Example Output

```text
All MVP Scores:
[44.8, 37.7, 34.2, 27.4]

Average MVP Score: 36.0

========== MATCH MVP ==========
MVP Name: Example Player
MVP Abbreviation: EP
MVP Team: TEAM-A
MVP Score: 44.8
```

The actual result depends on the player statistics inside `match_stats.csv`.

## What I Learned

While completing this project, I learned how to use Git to track changes with meaningful commits. I also learned how to work with branches, open and merge a pull request, intentionally create and resolve a merge conflict, and use `.gitignore` to protect local and sensitive files.

On the Python side, I learned how to read CSV data, organize code into functions, work with lists, calculate player statistics, and handle possible errors.