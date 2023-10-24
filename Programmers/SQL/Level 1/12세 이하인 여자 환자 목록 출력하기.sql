-- https://school.programmers.co.kr/learn/courses/30/lessons/132201
-- IFNULL (null 조건 시)
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO FROM PATIENT
WHERE GEND_CD = 'W' AND AGE <= 12 
ORDER BY AGE DESC, PT_NAME ASC
