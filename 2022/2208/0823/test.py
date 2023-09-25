str1 = '2+3*4/5'

stack = []
result = ''

# 후위표기법으로 계산하기

def calculator(word, stack):
    '''
    1. word : 연산할 계산식 (후위표기법)
    2. stack : 결과
    : return : stack
    '''
    for char in word:
        if char not in '*/+-':
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            if char == '-':
                stack.append(y - x)
            if char == '*':
                stack.append(y * x)
            if char == '/':
                stack.append(y / x)

# 후위표기법 만들기 (뭔가 문제가 있는듯 다시 보자)

for char in str1:
    # 연산자
    if char in '*/+-()':
        if not stack:
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char in '*/':
            while stack and stack[-1] in '*/':
                result += stack.pop()
            stack.append(char)
        elif char in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)
        elif char in ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

    # 피연산자   
    else:
        result += char
        print(f'result : {result}')

while stack:
    result += stack.pop()

res = calculator(result, [])
print(res)
    


