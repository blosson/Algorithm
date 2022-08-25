#1 - front, rear

front = -1
rear = -1
Q = [0] * 3

for _ in range(3):
    rear += 1
    Q[rear] = int(input())


while front != rear:            # 공백 상태가 아니면
    front += 1
    print(Q[front], end = ' ')

#2 - append, pop

Q = []
for _ in range(3):
    Q.append(int(input()))

for _ in range(3):
    print(Q.pop(0), end = ' ')