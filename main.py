from pathlib import Path
import pandas as pd

# Find cfb.csv in the same folder as this script, no matter where it's run from.
csv_path = Path(__file__).parent / "cfb.csv"

# Read the football data (utf-8-sig removes the hidden BOM before "Season").
football_data = pd.read_csv(csv_path, encoding="utf-8-sig")

# Ask which season to analyze.
season = int(input("Enter a season to analyze: "))

# Select the rows for that season.
season_data = football_data[football_data["Season"] == season]

if season_data.empty:
    print(f"No results found for the {season} season.")

else:
    # Create an empty list for each win category.
    categories = {
        "10 or more wins": [],
        "8–9 wins": [],
        "6–7 wins": [],
        "Fewer than 6 wins": []
    }

    # Place each team into its win category.
    for index, row in season_data.iterrows():
        team = row["Team"]
        wins = row["Win"]

        if wins >= 10:
            categories["10 or more wins"].append(team)
        elif wins >= 8:
            categories["8–9 wins"].append(team)
        elif wins >= 6:
            categories["6–7 wins"].append(team)
        else:
            categories["Fewer than 6 wins"].append(team)

    # Display the categories and their teams.
    print(f"\nCollege Football Results for {season}")

    for category, teams in categories.items():
        print(f"\n{category}:")

        for team in teams:
            print(f"  {team}")
