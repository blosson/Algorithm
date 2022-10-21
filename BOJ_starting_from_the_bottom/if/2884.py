hour, minute = map(int, input().split())

new_minute = minute - 45

if new_minute < 0:
    hour -= 1
    new_minute += 60
    if hour == -1:
        hour = 23

print(hour, new_minute)


