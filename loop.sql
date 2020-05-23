DECLARE
    new_values INT NOT NULL DEFAULT 1;
BEGIN
    FOR i IN 1..new_values LOOP
        INSERT INTO team(team_name)
        VALUES ('Barcelona');
        INSERT INTO match(team_home_name, team_away_name, match_home_goals, match_away_goals, match_results, season_period)
        VALUES ('Barcelona', 'Liverpool', '5', '0', 'H', '2010-2011');
        INSERT INTO match(team_home_name, team_away_name, match_home_goals, match_away_goals, match_results, season_period)
        VALUES ('Liverpool', 'Barcelona', '1', '3', 'A', '2017-2018');
        
    END LOOP;
END;
