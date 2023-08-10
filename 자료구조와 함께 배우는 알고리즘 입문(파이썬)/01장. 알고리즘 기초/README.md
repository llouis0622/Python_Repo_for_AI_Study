# 01장. 알고리즘 기초

# 1. 알고리즘이란?

- 알고리즘(Algorithm) : 어떠한 문제를 해결하기 위해 정해 놓은 일련의 절차

### 1. 세 정수의 최댓값 구하기

```python
# [Do it! 실습 1-1] 세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최댓값은 {maximum}입니다.')
```

- 순차 구조(Sequential Structure) : 한 문장씩 순서대로 처리되는 구조
- 선택 구조(Select Structure) : 조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경

```python
# [Do it! 실습 1-2] # 세 정수의 최댓값을 구하기

def max3(a, b, c):
    """a, b, c의 최댓값을 구하여 반환"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum  # 최댓값 반환

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')   # [A] a > b > c
print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')   # [B] a > b = c
print(f'max3(3, 1, 2) = {max3(3, 1, 2)}')   # [C] a > c > b
print(f'max3(3, 2, 3) = {max3(3, 2, 3)}')   # [D] a = c > b
print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')   # [E] c > a > b
print(f'max3(3, 3, 2) = {max3(3, 3, 2)}')   # [F] a = b > c
print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')   # [G] a = b = c
print(f'max3(2, 2, 3) = {max3(2, 2, 3)}')   # [H] c > a = b
print(f'max3(2, 3, 1) = {max3(2, 3, 1)}')   # [I] b > a > c
print(f'max3(2, 3, 2) = {max3(2, 3, 2)}')   # [J] b > a = c
print(f'max3(1, 3, 2) = {max3(1, 3, 2)}')   # [K] b > c > a
print(f'max3(2, 3, 3) = {max3(2, 3, 3)}')   # [L] b = c > a
print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')   # [M] c > b > a
```

### 2. 문자열과 숫자 입력받기

```python
# [Do it! 실습 1C-1] 이름을 입력받아 인사하기

print('이름을 입력하세요.: ', end = '')
name = input()
print(f'안녕하세요? {name} 님.')
```

```python
# 이름을 입력 받아 인사합니다(실습 1C-1 수정).

name = input( '이름을 입력하세요.: ')
print(f'안녕하세요? {name} 님.')
```

- 양 갈래 선택 : 조건식에 따라 알고리즘 흐름이 두 갈래로 나뉘는 것
- 결정 트리(Decision Tree) : 관계 조합을 나열한 모습이 나무같이 생긴 것

### 3. 세 정수의 중앙값 구하기

```python
# [Do it! 실습 1C-2] 세 정숫값을 입력받아 중앙값을 구하기 1

def med3(a, b, c):
    """a, b, c의 중앙값을 구하여 반환"""
    if a >= b: 
        if b >= c: 
            return b
        elif a <= c: 
            return a
        else:
            return c
    elif a > c: 
        return a
    elif b > c: 
        return c
    else:
        return b

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a, b, c)}입니다.')
```

```python
# 세 정숫값을 입력받아 중앙값을 구하기 2

def med3(a, b, c):
    """a, b, c의 중앙값을 구하여 반환(다른 방법)"""
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a, b, c)}입니다.')
```

### 4. 조건문과 분기

```python
# [Do it! 실습 1-3] 입력받은 정숫값의 부호(양수, 음수, 0) 출력하기

n = int(input('정수를 입력하세요.: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')
```

```python
# [Do it! 실습 1-4] 3개로 분기하는 조건문

n = int(input('정수를 입력하세요.: '))

if n == 1:
    print('A')
elif n == 2:
    print('B')
else:
    print('C')
```

```python
# [Do it! 실습 1-5] 4개로 분기하는 조건문

n = int(input('정수를 입력하세요.: '))

if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')
```

```python
# [Do it! 실습 1-6] 실습 1-5의 원래 모습

n = int(input('정수를 입력하세요.: '))

if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')
else :
    pass
```

### 5. 순서도 기호 살펴보기

- 순서도(Flowchart) : 문제를 정의, 분석하고 해결하는 방법을 그림으로 표현한 것
- 데이터 : 데이터 자체
- 처리 : 여러 종류의 처리 기능
- 미리 정의한 처리 : 서브루틴, 모듈 등 이미 정의한 하나 이상의 연산, 명령
- 판단 : 정의한 조건을 평가하여 하나의 출구를 선택하는 판단 기능
- 루프 범위 : 변수명, 초기값, 증가값, 종료값으로 이루어짐
- 선 : 제어의 흐름
- 단말 : 외부 환경으로 나가거나 외부 환경에서 들어오는 것

# 2. 반복하는 알고리즘

### 1. 1부터 n까지 정수의 합 구하기

```python
# [Do it! 실습 1-7] 1부터 n까지 정수의 합 구하기 1(while 문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = 0
i = 1

while i <= n:  # i가 n보다 작거나 같은 동안 반복
    sum += i   # sum에 i를 더함
    i += 1     # i에 1을 더함

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
```

- 반복 구조(Repetition Structure) : 어떤 조건이 성립하는 동안 반복해서 처리하는 것
- 판단 반복 구조 : 실행하기 전에 반복을 계속할 것인지 판단
- 루프 본문 : 반복 대상이 되는 명령문
- 카운터용 변수 : 반복을 제어할 때 사용하는 변수

### 2. `for문` 반복 알아보기

```python
# [Do it! 실습 1-8] 1부터 n까지의 합 구하기 2(for 문)

print('1부터 n까지의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = 0
for i in range(1, n + 1):
    sum += i  # sum에 i를 더함

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
```

### 3. `range()` 함수로 이터러블 객체 생성하기

- 이터러블 객체 : 반복할 수 있는 객체, `list, str, tuple`

### 4. 연속하는 정수의 합을 구하기 위해 값 정렬하기

```python
# [Do it! 실습 1-9] a부터 b까지 정수의 합 구하기(for 문)

print('a부터 b까지의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a  # a와 b를 오름차순으로 정렬

sum = 0
for i in range(a, b + 1):
    sum += i  # sum에 i를 더함

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')
```

### 5. 반복 과정에서 조건 판단하기 1

```python
# [Do it! 실습 1-10] a부터 b까지 정수의 합 구하기 1

print('a부터 b까지의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):  # b - a번 반복
    if i < b:              # i가 b보다 작으면 합을 구하는 과정을 출력
        print(f'{i} + ', end='')
    else:                  # i가 b보다 크거나 같으면 최종값 출력을 위해 i =를 출력
        print(f'{i} = ', end='')
    sum += i               # sum에 i를 더함

print(sum)
```

```python
# [Do it! 실습 1-11] a부터 b까지 정수의 합 구하기 2

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b :
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i  # sum에 i를 더함

print(f'{b} = ', end ='')
sum += b      # sum에 b를 더함

print(sum)
```

### 6. 반복 과정에서 조건 판단하기 2

```python
# [Do it! 실습 1-12] +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):          # 반복 n번
    if i % 2:                 
        print('-', end='')  # 홀수인 경우 - 출력
    else:
        print('+', end='')  # 짝수인 경우 + 출력

print()
```

```python
# [Do it! 실습 1-12] +와 -를 번갈아 출력하기 1(for 문 수정)

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(1, n + 1):  
    if i % 2:              # 홀수
        print('+', end='')
    else:                  # 짝수
        print('-', end='')
        
print()
```

```python
# [Do it! 실습 1-13] +와 -를 번갈아 출력하기 2

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for _ in range(n // 2):
    print('+-', end='')  # n // 2개의 +-를 출력

if n % 2:
    print('+', end='')  # n이 홀수일 때만 +를 출력

print()
```

```python
# [Do it! 실습 1-13] +와 -를 번갈아 출력하기 2(range()함수 수정)

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for _ in range(1, n // 2 + 1):
    print('+-', end='')  # n // 2개의 +-를 출력
    
if n % 2:
    print('+', end='')  # n이 홀수일 때만 +를 출력
```

### 7. 반복 과정에서 조건 판단하기 3

```python
# [Do it! 실습 1-14] *를 n개 출력하되 w개마다 줄바꿈하기 1

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요? : '))
w = int(input('몇 개마다 줄바꿈할까요? : '))

for i in range(n):      # n번 반복
    print('*', end='')
    if i % w == w - 1:  # n번 판단
        print()         # 줄바꿈

if n % w:
    print()             # 줄바꿈
```

```python
# *를 n개 출력하되 w개마다 줄바꿈하기 2

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for _ in range(n // w):  # 반복 n // w번 반복
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)  # if 문 1번 판단
```

### 8. 양수만 입력받기

```python
# [Do it! 실습 1-16] 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

print('1부터 n까지 정수의 합을 구합니다.')

while True:
    n = int(input('n값을 입력하세요.: '))
    if n > 0:
        break  # n이 0보다 커질 때까지 반복

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i  # sum에 i를 더함
    i += 1    # i에 1을 더함

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
```

### 9. 직사각형 넓이로 변의 길이 구하기

```python
# [Do it! 실습 1-17] 가로 세로가 정수이고 넓이가 area인 직사각형에서 변의 길이를 나열하기

area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area + 1):  # 1부터 사각형의 넓이 계산
    if i * i > area: break
    if area % i: continue
    print(f'{i} × {area // i}')
```

```python
# [Do it! 실습 1-18] 10~99 사이의 난수 n개 생성하기(13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else :
    print('\n난수 생성을 종료합니다.')
```

### 10. 반복문 건너뛰기와 여러 범위 스캔하기

```python
# [Do it! 실습 1-19] 1~12까지 8을 건너뛰고 출력하기 1

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
    
print()
```

```python
# [Do it! 실습 1-20] 1부터 12까지 8을 건너 뛰고 출력하기 2

for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')
print()
```

### 11. 비교 연산자를 연속으로 사용하는 방법과 드모르간 법칙

```python
# [Do it! 실습 1C-3] 2자리 양수(10 ~ 99) 입력받기

print('2자리 양수를 입력하세요.')

while True:
    no = int(input('값을 입력하세요.: '))
    if no >= 10 and no <= 99:
        break

print(f'입력받은 양수는 {no}입니다.')
```

```python
# 2자리 양수(10 ~ 99) 입력받기 2

print('2자리 양수를 입력하세요.')

while True:
    no = int(input('값을 입력하세요.: '))
    if 10 <= no <= 99:
        break

print(f'입력받은 양수는 {no}입니다.')
```

```python
# 2자리 양수(10~99) 입력받기 3

print('2자리 양수를 입력하세요.')

while True:
    no = int(input('값을 입력하세요.: '))
    if not(no < 10 or no > 99):
        break

print(f'입력받은 양수는 {no}입니다.')
```

### 12. 다중 루프 알아보기

```python
# [Do it! 실습 1-21] 구구단 곱셈표 출력하기

print('-' * 27)
for i in range(1, 10):      # 행 루프
    for j in range(1, 10):  # 열 루프
        print(f'{i * j : 3}', end='')
    print()                 # 행 변경
print('-' * 27)
```

```python
# [Do it! 실습 1-22] 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요.: '))

for i in range(n):          # 행 루프
    for j in range(i + 1):  # 열 루프
        print('*', end='')
    print()
```

```python
# [Do it! 실습 1-23] 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변 길이를 입력하세요.: '))

for i in range(n):              # 행 루프
    for _ in range(n - i - 1):  # 열 루프(공백을 출력)
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')      # 열 루프(*을 출력)
    print()
```

- 파이썬의 변수는 값을 갖지 않음
