# link : https://leetcode.com/problems/average-time-of-process-per-machine/?envType=study-plan-v2&envId=top-sql-50
# Write your MySQL query statement below
select machine_id,
round(avg(end_timestamp - start_timestamp),3) AS processing_time
from (
    select a.machine_id, a.process_id, a.timestamp AS start_timestamp,
    b.timestamp as end_timestamp
    From Activity a
    inner join Activity b ON a.machine_id = b.machine_id AND a.process_id = b.process_id
    where a.activity_type = 'start' and b.activity_type = 'end'

) As process_data
group by machine_id
order by machine_id;