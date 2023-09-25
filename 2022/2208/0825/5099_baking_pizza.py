N, M = map(int, input().split())
c_list = list(map(int, input().split()))

oven = [0] * N
pizza_check = [0] * M

for i in range(N):
    oven[i] = c_list.pop(0)

while True:
    

print(oven)
print(pizza_check)
print(c_list)