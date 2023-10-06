-- https://school.programmers.co.kr/learn/courses/30/lessons/131112
-- LIKE 활용
SELECT factory_id, factory_name, address FROM food_factory WHERE address LIKE '강원도%' ORDER BY factory_id