-- https://school.programmers.co.kr/learn/courses/30/lessons/131528
-- AS를 사용하면 해당 컬럼으로 출력됨
SELECT COUNT(*) AS USERS FROM USER_INFO WHERE AGE IS NULL

-- 다른 풀이
SELECT SUM(AGE IS NULL) AS USERS FROM USER_INFO