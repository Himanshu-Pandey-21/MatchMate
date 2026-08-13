-- MatchMate database schema
-- Create the database
CREATE DATABASE IF NOT EXISTS sportsdb;
USE sportsdb;

-- Teams
CREATE TABLE IF NOT EXISTS teams (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    coach_name VARCHAR(100)
);

-- Players
CREATE TABLE IF NOT EXISTS players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    age INT,
    sport VARCHAR(50),
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Matches
CREATE TABLE IF NOT EXISTS matches (
    match_id INT PRIMARY KEY,
    team1_id INT,
    team2_id INT,
    match_date DATE,
    winner_id INT,
    FOREIGN KEY (team1_id) REFERENCES teams(team_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (team2_id) REFERENCES teams(team_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (winner_id) REFERENCES teams(team_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
