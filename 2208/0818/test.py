def enQueue(itme):
    global rear
    if isFull(Q):
        print('Queue_Full') # 디버깅용
    else:
        rear += 1
        Q[rear] = itme

rear = -1    # 초기값
Q = [0] * 10 # 그냥 대충 설정한 거

def deQueue():
    global front
    if isEmpty(Q):
        print('Queue_Empty') # 디버깅용
    else:
        fornt += 1
        return Q[front]

front = -1 # 초기값
Q = [0] * 10 # 그냥 대충 설정한 거

def isEmtpy():
    return front == rear

def Full():
    return rear == len(Q) - 1