-- https://school.programmers.co.kr/learn/courses/30/lessons/131535
-- BETWEEN도 사용 가능 SELECT AGE BETWEEN 20 AND 29 (이상, 이하)
SELECT COUNT(*) AS USERS FROM USER_INFO 
WHERE JOINED LIKE '2021%' AND  AGE >= 20 AND AGE <= 29