-- Lists all records of the table second_table.
-- Records are ordered by descending score.
-- where score >= 10
SELECT score, name
FROM second_table
WHERE score >= 21
ORDER BY score DESC;
