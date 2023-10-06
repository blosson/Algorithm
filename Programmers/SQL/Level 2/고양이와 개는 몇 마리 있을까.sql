-- https://school.programmers.co.kr/learn/courses/30/lessons/59040
-- IN 조건 
SELECT ANIMAL_TYPE, COUNT(*) AS count FROM ANIMAL_INS
-- WHERE ANIMAL_TYPE IN ('Cat', 'Dog') 
WHERE ANIMAL_TYPE = 'Cat' OR ANIMAL_TYPE = 'Dog'
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC