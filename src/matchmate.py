import csv
import datetime
import os

from dotenv import load_dotenv
import mysql.connector
from tabulate import tabulate

load_dotenv()


# ----------------------------
# Database Connection
# ----------------------------
def get_connection():
    """Create a MySQL connection using environment variables."""
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE", "sportsdb"),
    )


# ----------------------------
# CSV Backup Setup
# ----------------------------
def ensure_csv(filename, headers):
    """Create a CSV file with headers if it does not already exist."""
    if not os.path.exists(filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)


ensure_csv("teams.csv", ["team_id", "team_name", "coach_name"])
ensure_csv("players.csv", ["player_name", "age", "sport", "team_id"])
ensure_csv(
    "matches.csv",
    ["match_id", "team1_id", "team2_id", "match_date", "winner_id"],
)


# ----------------------------
# Team Management
# ----------------------------
def add_team():
    team_id = int(input("Enter team ID: "))
    name = input("Enter team name: ")
    coach = input("Enter coach name: ")

    # Save to Database
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """
        INSERT INTO teams (team_id, team_name, coach_name)
        VALUES (%s, %s, %s)
        """,
        (team_id, name, coach),
    )
    con.commit()
    con.close()

    # Save to CSV
    with open("teams.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([team_id, name, coach])

    print("Team added successfully!")


def add_player():
    name = input("Enter player name: ")
    age = int(input("Enter player age: "))
    sport = input("Enter sport: ")
    team_id = int(input("Enter team ID: "))

    # Save to Database
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """
        INSERT INTO players (player_name, age, sport, team_id)
        VALUES (%s, %s, %s, %s)
        """,
        (name, age, sport, team_id),
    )
    con.commit()
    con.close()

    # Save to CSV
    with open("players.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, age, sport, team_id])

    print("Player added successfully!")


# ----------------------------
# Match Management
# ----------------------------
def schedule_match():
    match_id = int(input("Enter match ID: "))
    team_1_id = int(input("Enter Team 1 ID: "))
    team_2_id = int(input("Enter Team 2 ID: "))
    date_str = input("Enter match date (YYYY-MM-DD): ")
    match_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    # Save to Database
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """
        INSERT INTO matches (match_id, team1_id, team2_id, match_date)
        VALUES (%s, %s, %s, %s)
        """,
        (match_id, team_1_id, team_2_id, match_date),
    )
    con.commit()
    con.close()

    # Save to CSV
    with open("matches.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([match_id, team_1_id, team_2_id, date_str, ""])

    print("Match scheduled successfully!")


def record_result():
    match_id = int(input("Enter match ID: "))
    winner_id = int(input("Enter winner team ID: "))

    # Update in Database
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """
        UPDATE matches
        SET winner_id = %s
        WHERE match_id = %s
        """,
        (winner_id, match_id),
    )
    con.commit()
    con.close()

    # Update in CSV
    with open("matches.csv", "r", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    for i in range(1, len(rows)):
        if rows[i][0] == str(match_id):
            rows[i][4] = str(winner_id)

    with open("matches.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Result recorded!")


def view_matches():
    print("\nMATCH DETAILS (from Database):")

    con = get_connection()
    cur = con.cursor()
    cur.execute(
        """
        SELECT
            m.match_id,
            t1.team_name AS Team1,
            t2.team_name AS Team2,
            m.match_date AS Date,
            w.team_name AS Winner
        FROM matches m
        JOIN teams t1 ON m.team1_id = t1.team_id
        JOIN teams t2 ON m.team2_id = t2.team_id
        LEFT JOIN teams w ON m.winner_id = w.team_id;
        """
    )

    db_data = cur.fetchall()
    con.close()

    headers = ["Match ID", "Team 1", "Team 2", "Match Date", "Winner"]
    print(tabulate(db_data, headers=headers, tablefmt="fancy_grid"))

    print("\nMATCH DETAILS (from CSV backup):")
    with open("matches.csv", "r", newline="", encoding="utf-8") as f:
        csv_data = list(csv.reader(f))

    print(tabulate(csv_data, tablefmt="fancy_grid"))


# ----------------------------
# Main Menu
# ----------------------------
def main_menu():
    while True:
        print("\nMatchMate")
        print("1. Add Team")
        print("2. Add Player")
        print("3. Schedule Match")
        print("4. Record Match Result")
        print("5. View Matches")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_team()
        elif choice == "2":
            add_player()
        elif choice == "3":
            schedule_match()
        elif choice == "4":
            record_result()
        elif choice == "5":
            view_matches()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main_menu()
