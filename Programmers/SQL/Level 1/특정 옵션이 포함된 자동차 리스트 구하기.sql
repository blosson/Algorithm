-- https://school.programmers.co.kr/learn/courses/30/lessons/157343
-- LIKE와 IN ('~~~')은 다름에 주의!!
SELECT * FROM CAR_RENTAL_COMPANY_CAR 
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC