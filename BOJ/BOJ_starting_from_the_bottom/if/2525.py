hour, minute = map(int, input().split())
oven_time = int(input())
plus_minute = minute + oven_time

if plus_minute >= 60:
    plus_hour = plus_minute // 60
    hour += plus_hour
    plus_minute -= 60 * plus_hour

if hour >= 24:
    renew_hour = hour % 24    
else:
    renew_hour = hour

print(renew_hour, plus_minute, sep=' ')
