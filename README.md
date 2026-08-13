# MatchMate — Sports Management System

MatchMate is a Class 12 Python project designed as a database-driven system for managing sports activities. It provides a menu-driven command-line interface for managing teams, registering players, scheduling matches, recording results, and viewing match details.

The project combines **Python, MySQL, and CSV files**. MySQL provides structured storage, while CSV files are maintained as backups for portability and easy data access.

> **Note:** This repository is a cleaned public version reconstructed from the project documentation. The original document contained a hard-coded MySQL password; that credential has been removed and replaced with environment-variable configuration.

## Features

- Add teams with team ID, team name, and coach
- Register players with name, age, sport, and team ID
- Schedule matches between teams
- Record match winners
- View scheduled matches, dates, participating teams, and winners
- Store structured data in MySQL
- Maintain CSV backups for teams, players, and matches
- Simple menu-driven command-line interface

## Tech Stack

- Python
- MySQL
- `mysql-connector-python`
- CSV
- `tabulate`

## Repository Structure

```text
MatchMate/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── src/
│   └── matchmate.py
├── database/
│   └── schema.sql
├── data/
│   └── README.md
└── docs/
    └── project-notes.md
```

## Database Design

The MySQL database is named `sportsdb` and contains three main tables:

- `teams` — team ID, team name, and coach
- `players` — player details and associated team
- `matches` — teams involved, match date, and winner

The schema and relationships are defined in [`database/schema.sql`](database/schema.sql).

## CSV Backup

The application also maintains:

- `teams.csv`
- `players.csv`
- `matches.csv`

These files are generated locally when the application runs. They are ignored by Git so personal/local data is not accidentally committed.

## Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd MatchMate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the MySQL database

Open MySQL and run:

```sql
SOURCE database/schema.sql;
```

Or paste the contents of `database/schema.sql` into your MySQL client.

### 4. Configure database credentials

Copy `.env.example` to `.env` and fill in your local MySQL credentials. The application loads these variables from `.env` using `python-dotenv`.

Example `.env`:

```bash
export MYSQL_HOST=localhost
export MYSQL_USER=root
export MYSQL_PASSWORD=your_mysql_password
export MYSQL_DATABASE=sportsdb
```

If you prefer, you can also set the same variables directly in your shell.

### 5. Run MatchMate

```bash
python src/matchmate.py
```

## Main Menu

```text
MatchMate
1. Add Team
2. Add Player
3. Schedule Match
4. Record Match Result
5. View Matches
6. Exit
```

## How the system works

```text
User
  │
  ▼
Python Command-Line Interface
  │
  ├──────────────► MySQL (sportsdb)
  │                    │
  │                    ├── teams
  │                    ├── players
  │                    └── matches
  │
  └──────────────► CSV backup files
```

## Security Note

**Never commit real database passwords, API keys, tokens, or other secrets to GitHub.**

This public version intentionally removes the password that appeared in the original project document and uses environment variables instead.

If a real password from the original project was ever used for an account, rotate/change it before publishing this repository.

## Project Background

MatchMate was created as a Class 12 project with the goal of reducing manual work involved in organizing sports activities and keeping sports records. The project documentation describes its intended use for schools, colleges, and small sports organizations.

## Learning Outcomes

The project provided practical experience with:

- Python programming
- SQL and relational databases
- Connecting Python to MySQL
- CRUD-style database operations
- CSV file handling
- Basic data relationships using foreign keys
- Command-line interface design
- Thinking about data backup and portability

## Future Improvements

Possible future improvements include:

- A graphical or web-based interface
- Better input validation and error handling
- User authentication and role-based access
- Automated fixture generation
- Score tracking
- Points tables and standings
- Stronger synchronization between MySQL and CSV data
- Automated tests

## Source

This repository is based on the original MatchMate Class 12 project documentation and cleaned for public portfolio use.
