-- https://school.programmers.co.kr/learn/courses/30/lessons/59039
-- MySQL에서는 NAME = NULL이 아니고 IS NULL / IS NOT NULL 이런식으로 검색한다! (기본문법)
 select animal_id from animal_ins where name is null order by animal_id