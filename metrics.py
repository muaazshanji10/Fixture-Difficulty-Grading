import requests, json, time, os, duckdb

con.sql("""
    CREATE OR REPLACE TABLE form_last_five_games AS
    WITH x as (
    Select
        match_id,
        date,
        home_team as team,
        away_team as opponent,
        case when winner = 'HOME_TEAM' then 'win'
            when winner = 'DRAW' then 'draw'
            else 'loss'
        end as result,
        case when winner = 'HOME_TEAM' then 3
            when winner = 'DRAW' then 1
            else 0
        end as points
    From matches_clean
    Where date <= CURRENT_DATE

    Union all

    Select
        match_id,
        date,
        away_team as team,
        home_team as opponent,
        case when winner = 'AWAY_TEAM' then 'win'
            when winner = 'DRAW' then 'draw'
            else 'loss'
        end as result,
        case when winner = 'AWAY_TEAM' then 3
            when winner = 'DRAW' then 1
            else 0
        end as points
    From matches_clean
    Where date <= CURRENT_DATE
    ),

    ranked as (
        select *,
            row_number() over (partition by team order by date desc) as rn
        from x
    )

    select team, sum(points) as form
    from ranked
    where rn <= 5
    group by team
""")

con.sql("SELECT * FROM form_last_five_games").show()

con.sql("""
    CREATE OR REPLACE TABLE h2h_form AS
    WITH y as (
    Select
        match_id,
        date,
        home_team as team,
        away_team as opponent,
        case when winner = 'HOME_TEAM' then 'win'
            when winner = 'DRAW' then 'draw'
            else 'loss'
        end as result,
        case when winner = 'HOME_TEAM' then 3
            when winner = 'DRAW' then 1
            else 0
        end as points
    From matches_clean
    Where date <= CURRENT_DATE

    Union all

    Select
        match_id,
        date,
        away_team as team,
        home_team as opponent,
        case when winner = 'AWAY_TEAM' then 'win'
            when winner = 'DRAW' then 'draw'
            else 'loss'
        end as result,
        case when winner = 'AWAY_TEAM' then 3
            when winner = 'DRAW' then 1
            else 0
        end as points
    From matches_clean
    Where date <= CURRENT_DATE
    ),

    ranked as (
        select *,
            row_number() over (partition by team, opponent order by date desc) as rn
        from y
    )

    select team, opponent, avg(points) as h2h_form_pl, count(*) as meetings
    from ranked
    where rn <= 6
    group by team, opponent
""")

con.sql("SELECT * FROM h2h_form").show()

con.sql("""
CREATE OR REPLACE TABLE fixture_grader AS
WITH fixtures AS (
    SELECT match_id, date, home_team AS team, away_team AS opponent, TRUE AS is_home
    FROM matches_clean
    WHERE status IN ('SCHEDULED', 'TIMED')

    UNION ALL

    SELECT match_id, date, away_team AS team, home_team AS opponent, FALSE AS is_home
    FROM matches_clean
    WHERE status IN ('SCHEDULED', 'TIMED')
),

next_fixture AS (
    SELECT *
    FROM (
        SELECT *,
            row_number() OVER (PARTITION BY team ORDER BY date, match_id) AS rn
        FROM fixtures
    )
    WHERE rn = 1
),

standings_scored AS (
    SELECT
        team,
        points,
        goal_difference,
        points / (3.0 * games_played) AS league_score,
        (count(*) OVER () - rank() OVER (ORDER BY goal_difference DESC))
        / (count(*) OVER () - 1.0) AS gd_score
    FROM standings_clean
),

scaled AS (
    SELECT
        n.team,
        n.opponent,
        n.is_home,
        s.points AS opp_points,
        s.goal_difference AS opp_goal_difference,
        f.form AS opp_form,
        h.h2h_form_pl AS h2h_ppg,
        f.form / 15.0 AS form_score,
        s.league_score,
        s.gd_score,
        1 - COALESCE(h.h2h_form_pl / 3.0, 0.5) AS h2h_score,
        CASE WHEN n.is_home THEN 0.36 ELSE 0.64 END AS venue_score
    FROM next_fixture n
    LEFT JOIN standings_scored s ON n.opponent = s.team
    LEFT JOIN form_last_five_games f ON n.opponent = f.team
    LEFT JOIN h2h_form h ON n.team = h.team AND n.opponent = h.opponent
)

SELECT *,
    ROUND(100 * (0.30 * form_score
               + 0.30 * league_score
               + 0.10 * gd_score
               + 0.20 * h2h_score
               + 0.10 * venue_score), 1) AS difficulty
FROM scaled
""")

con.sql("SELECT * FROM fixture_grader ORDER BY difficulty DESC").show()