-- https://school.programmers.co.kr/learn/courses/30/lessons/59409
-- CASE WHEN THEN ELSE END
SELECT ANIMAL_ID, NAME,
    CASE 
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
        WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
        -- 아래처럼도 가나ㅡㅇ
        -- WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
        ELSE 'X'
        
    END AS 중성화
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID