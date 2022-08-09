import sys

sys.stdin = open('sample.txt', 'r') # readyonly

a = int(input())
print(a)

a = [1, 3, 4, 2, 6, 8]
print(a[1:])
print(a[3:])
print(max(a[3:]))