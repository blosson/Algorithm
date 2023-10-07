-- https://school.programmers.co.kr/learn/courses/30/lessons/157342
-- HAVING보다 SELECT가 우선이다! SELECT에서 설정한 AS로 HAVING과 ORDER BY 등에서 사용할 수 있음
SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC




