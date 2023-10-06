-- https://school.programmers.co.kr/learn/courses/30/lessons/59041
-- HAVING 조건
SELECT NAME, COUNT(*) AS COUNT FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(*) > 1
-- HAVING COUNT >= 2 AND NAME IS NOT NULL -> 이렇게 하면 굳이 COUNT(*) 안 써도 됨
ORDER BY NAME