-- https://school.programmers.co.kr/learn/courses/30/lessons/59042
-- RIGHT JOIN, WHERE IS NULL 조건 주기
SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_INS INS
RIGHT JOIN ANIMAL_OUTS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY OUTS.ANIMAL_ID