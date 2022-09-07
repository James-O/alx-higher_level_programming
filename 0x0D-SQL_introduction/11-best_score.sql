-- select record in db table and sort it in desc order
-- only records greater than 10 should be displayed

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC
