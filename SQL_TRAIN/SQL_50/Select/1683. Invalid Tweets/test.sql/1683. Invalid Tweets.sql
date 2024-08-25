 -- Link : https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50
-- Author : Aghilas SMAIL


select tweet_id
from Tweets
where length(content) > 15