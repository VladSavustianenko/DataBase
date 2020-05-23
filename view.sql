CREATE VIEW match_view AS
    SELECT 
        match.team_home_name
        , match.team_away_name
        , match.match_results
        , match.season_period
    FROM match
    INNER JOIN season ON match.season_period = season.season_period
    INNER JOIN team ON match.team_home_name = team.team_name
    INNER JOIN team ON match.team_away_name = team.team_name
    WHERE 
        (match.match_results = 'H'
        AND match.team_home_name = 'Manchester City') OR
        (match.match_results = 'A'
        AND match.team_away_name = 'Manchester City')