-- Link : https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50
-- author : Aghilas SMAIL

select S.user_id,

        round( -- Handles cases where the user has no confirmation messages by setting the rate to 0.
            coalesce(count(case when C.action = 'confirmed' then 1 end) / nullif(count(C.user_id), 0), 0),
            2 -- the round for getting value in decimal
        ) as confirmation_rate
from
    Signups S
left join 
    Confirmations C
on 
    S.user_id = C.user_id
Group BY
    S.user_id;
