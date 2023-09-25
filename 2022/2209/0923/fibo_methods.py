#1 재귀 피보나치
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

#2 메모이제이션 재귀 피보나치
def fibo_memoization(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo_memoization(n-1) + fibo_memoization(n-2))
    return memo[n]

memo = [0, 1]

#3 DP 반복 피보나치 - append 활용 (재귀를 활용한 메모이제이션보다 반복이 더 효율적)
def fibo_dp(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    return f[n]


#4 DP 반복 피보나치 = table 활용 (DP-append보다 더 빠름)
def fibo_dp_table(n):
    table[0] = 0
    table[1] = 1
    
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return

N = int(input())
table = [0] * N