-- https://school.programmers.co.kr/learn/courses/30/lessons/131113
-- CASE 구문 (CASE-WHEN-THEN-ELSE-END)
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
    CASE WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
    WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
    ELSE '출고미정'
    END AS 출고여부
FROM FOOD_ORDER 
ORDER BY ORDER_ID