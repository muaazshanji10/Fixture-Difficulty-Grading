import requests, json, time, os, duckdb

con = duckdb.connect("data/grader.duckdb")

con.sql("""
    CREATE OR REPLACE TABLE matches_clean AS
    SELECT
        m.season.id AS season_id,
        m.matchday AS match_day,
        m.id AS match_id,
        m.utcDate AS date,
        m.homeTeam.name AS home_team,
        m.awayTeam.name AS away_team,
        m.score.winner AS winner,
        m.status AS status
    FROM (
        SELECT unnest(matches) AS m
        FROM read_json_auto('data/raw/matches_*.json')
    )

""")

con.sql("SELECT * FROM matches_clean").show()

import duckdb

con.sql("""
    CREATE OR REPLACE TABLE standings_clean AS
    SELECT
        t.team.name AS team,
        t.position AS position,
        t.points AS points,
        t.goalDifference AS goal_difference,
        t.playedGames as games_played
    FROM (
        SELECT unnest(standings[1].table) AS t
        FROM read_json_auto('data/raw/standings.json')
    )
""")

con.sql("SELECT * FROM standings_clean").show()