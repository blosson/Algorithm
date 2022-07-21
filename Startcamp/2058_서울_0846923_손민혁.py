k = int(input())       

# k가 4자리수이고 각 자리값이 0이 아니라는 가정 하에
a = k // 1000 # k의 천의 자리 숫자 6
b = k % 1000 # k의 천의 자리 숫자를 제외한 3자리 수 789
c = (k % 1000) // 100 # k의 백의 자리 숫자 7
d = (k % 1000) % 100 # k의 천, 백의 자리 숫자를 제외한 2자리 수 89
e = ((k % 1000) % 100) // 10 # k의 십의 자리 숫자 8
f = ((k % 1000) % 100) % 10 # k의 일의 자리 숫자 0
# 결국 (a + c + e + f) 값을 구해주면 됨

if a >= 1:
    if c >= 1:
        if e >= 1:
            print(a + c + e +f)
        else: 
            print(a + c + e +f)
    else:
        if e >= 1:
            print(a + c + e +f)
        else: 
            print(a + c + e +f)
else:
    if c >= 1:
        if e >= 1:
            print(a + c + e +f)
        else: 
            print(a + c + e +f)
    else:
        if e >= 1:
            print(a + c + e +f)
        else: 
            print(a + c + e +f)  
