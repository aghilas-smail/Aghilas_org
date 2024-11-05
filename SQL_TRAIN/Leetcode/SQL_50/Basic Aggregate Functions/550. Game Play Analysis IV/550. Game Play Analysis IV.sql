-- link : https://leetcode.com/problems/game-play-analysis-iv/description/?envType=study-plan-v2&envId=top-sql-50

SELECT
  -- Dans cette partie on va calculer la fraction des joueurs qui sont connectés a nouveau le jour suivant 
  ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM
  Activity
WHERE 
   -- Ici on regarde la pemier date au le joueur a connecter et si il s'est reconnecter encore une fois le jour suivant
  (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
  IN (
    
    SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id )