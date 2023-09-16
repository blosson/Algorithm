numbers = [int(input()) for _ in range(10)]

remainder = []
for number in numbers:
    remainder.append(number % 42)
remainder = list(set(remainder))
print(len(remainder))
    
    