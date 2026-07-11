# Write your MySQL query statement below
select round(count(t.player_id)/(
    select count(distinct player_id)
from Activity
),2) as fraction
from Activity a
JOIN (select player_id,MIN(event_date) as first_day
from Activity
group by player_id)  as t on t.player_id=a.player_id
where a.event_date=t.first_day+INTERVAL 1 DAY