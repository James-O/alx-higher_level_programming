-- list all score with there num of occureance in desc order

SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC
