# 02장. 기본 자료구조와 배열

# 1. 자료구조와 배열

## 1. 배열 개념 알아보기

```python
#[Do it! 실습 2-1] 학생 5명의 점수를 입력받아 합계와 평균을 출력하기

print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1 = int(input('1번 학생의 점수를 입력하세요.: '))
score2 = int(input('2번 학생의 점수를 입력하세요.: '))
score3 = int(input('3번 학생의 점수를 입력하세요.: '))
score4 = int(input('4번 학생의 점수를 입력하세요.: '))
score5 = int(input('5번 학생의 점수를 입력하세요.: '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계는 {total}점입니다.')
print(f'평균은 {total / 5}점입니다.')
```

- 배열(Array) : 묶음 단위로 값을 저장
- 원소(Element) : 배열에 저장된 객체

## 2. 리스트와 튜플 알아보기

- 리스트(List)
    - 뮤터블(Mutable) list형 객체 : 값을 변경할 수 있는 특ㅈ
- 튜플(Tuple)
    - 이뮤터블(Immutable) 자료형 : 값을 변경할 수 없는 특성
- 언팩(Unpack) : 리스트나 튜플의 원소값들을 풀어 여러 변수에 대입하는 것

## 3. 인덱스로 원소에 접근하기

- 인덱스(Index)

## 4. 슬라이스식으로 원소에 접근하기

- 슬라이스(Slice) : 리스트나 튜플의 원소 일부를 연속해서 또는 일정한 간격으로 꺼내 새로운 리스트 또는 튜플을 만드는 것
- `s[i:j]` : `s[i]` 부터 `s[j-1]` 까지 나열
- `s[i:j:k]` : `s[i]` 부터 `s[j-1]` 까지 `k` 씩 건너뛰며 나열
- `s[:]` : 리스트의 원소 모두 출력
- `s[:n]` : 리스트 원소 중 맨 앞부터 `n` 개까지 출력
- `s[i:]` : 리스트 원소 중 `s[i]` 부터 맨 끝까지 출력
- `s[-n:]` : 리스트 원소 중 `-n` 부터 맨 끝까지 출력
- `s[::k]` : 리스트 원소 중 맨 앞부터 `k` 개씩 건너뛰며 출력
- `s[::-1]` : 리스트 원소 중 맨 끝부터 전부 출력

## 5. 자료구조의 개념 알아보기

- 자료구조(Data Structure) : 데이터 단위와 데이터 자체 사이의 물리적 또는 논리적인 관계
- 등가성(Equality) : `==` 사용, 좌변과 우변의 값이 같은지 비교
- 동일성(Identity) : `is` 사용, 값은 물론 객체의 식별 번호까지 같은지 비교

# 2. 배열이란?

## 1. 배열 원소의 최댓값 구하기

- 스캔(Scan) : 배열 원소를 하나씩 차례로 주목하여 살펴보는 방식

```python
# [Do it! 실습 2-2] 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형 a 요소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
         if a[i] > maximum: 
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num    # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]를 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')
```

## 2. 주석과 자료형 힌트

- `Any` : 제약이 없는 임의의 자료형
- `Sequence` : 시퀀스형(리스트형, 바이트 배열형, 문자열형, 튜플형, 바이트열형)
- 함수 어노테이션(Annotation) : 주석 달기

## 3. 재사용할 수 있는 묘듈 작성하기

- 모듈(Module) : 하나의 스크립트 프로그램

## 4. 모듈 테스트하기

### 1. 입력받을 때 원소 수를 결정하기

```python
# [Do it! 실습 2-3] 배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)

from max import max_of

print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []                  # 빈 리스트

while True:
    s = input(f'x[{number}]를 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))    # 배열의 끝에 추가
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')
```

### 2. 배열의 원소값을 난수로 결정하기

```python
# [Do it! 실습 2-4] 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

import random
from max import max_of

print('난수의 최댓값을 구합니다.')
num = int(input('난수의 개수를 입력하세요.: '))
lo = int(input('난수의 최솟값을 입력하세요.: '))
hi = int(input('난수의 최댓값을 입력하세요.: '))
x = [None] * num        # 원소 수 num인 리스트를 생성

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')
```

### 3. 튜플, 문자열, 문자열 리스트의 최댓값 구하기

```python
# [Do it! 실습 2-5] 배열 요소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.')
print(f'{a}의 최댓값은 {max_of(a)}입니다.')
```

### 4. 리스트 스캔

```python
# [Do it! 실습 2C-1] 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)

x = ['John', 'George', 'Paul', 'Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
```

```python
# [Do it! 실습 2C-2] 리스트의 모든 원소를 enumerate 함수로 스캔하기

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
```

```python
# [Do it! 실습 2C-3] 리스트의 모든 요소를 enumerate 함수로 스캔(1부터 카운트)

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')
```

```python
# [Do it! 실습 2C-4] 리스트의 모든 원소를 스캔하기(인덱스 값을 사용하지 않음)

x = ['John', 'George', 'Paul', 'Ringo']

for i in x:
    print(i)
```

### 5. 튜플 스캔

- `x = []` → `x = ()` 로 수정
- 이터러블(Iterable) : 반복 가능

## 5. 배열 원소를 역순으로 정렬하기

```python
# [Do it! 실습 2-6] 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스형 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n // 2):
         a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx   # 원소 수가 nx인 리스트를 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}] : '))

    reverse_array(x)  # x를 역순으로 정렬

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
```

## 6. 기수 변환하기(n진수 구하기)

```python
# Do it! 실습 2-7 [A] 10진수 정수값을 입력받아 2~36진수로 변환하여 출력하기

def card_conv(x: int, r: int) -> str:
    """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d = ''  # 변환 뒤 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar [x % r]  # 해당하는 문자를 꺼내 결합
        x //= r

    return d[::-1]          # 역순으로 반환

# Do it! 실습 2-7 [B]

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True :  # 음이 아닌 정수를 입력받음
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0:
                break

        while True :  # 2~36진수의 정수값을 입력받음
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <=  cd <=  36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input( "한 번 더 변환할까요?(Y ... 예/N ... 아니오): ")
        if retry in {'N', 'n'}:
           break
```

```python
# 10진수 정수값을 입력받아 2~36진수로 변환하여 출력하기(실습 2-7 수정)

def card_conv(x: int, r: int) -> str:
    """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d =  ''  # 변환 뒤 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))  # 변환하기 전의 자릿수

    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print('   +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}d} … {x % r}')
        else:
            print(f'     {x // r:{n}d} … {x % r}')
        d += dchar [x % r]  # 해당하는 문자를 꺼내 결합
        x //= r

    return d[::-1]  # 역순으로 반환

# 이하 Do it! 실습 2-7 [B]와 동일

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True :  # 음이 아닌 정수를 입력받음
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0:
                break

        while True :  # 2~36진수의 정수값을 입력받음
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <=  cd <=  36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input( "한 번 더 변환할까요?(Y … 예/N … 아니오) : ")
        if retry in {'N', 'n'}:
           break
```

## 7. 소수 나열하기

```python
# [Do it! 실습 2-8] 1,000 이하의 소수를 나열하기

counter = 0  # 나눗셈 횟수

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0 :     # 나누어 떨어지면 소수가 아님
            break           # 반복은 더 이상 불필요하여 중단
    else:                   # 끝까지 나누어 떨어지지 않으면 다음을 수행
        print(n)
print(f'나눗셈을 실행한 횟수: {counter}')
```

```python
# [Do it! 실습 2-9] 1,000 이하의 소수를 나열하기(알고리즘 개선 1)

counter = 0           # 나눗셈 횟수
ptr = 0               # 이미 찾은 소수의 개수
prime = [None] * 500  # 소수를 저장하는 배열

prime[ptr] = 2        # 2는 소수이므로 초깃값으로 지정
ptr += 1

for n in range(3, 1001, 2):  # 홀수만을 대상으로 설정
    for i in range(1, ptr):  # 이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0:  # 나누어 떨어지면 소수가 아님
            break              # 반복 중단
    else:                      # 끝까지 나누어 떨어지지 않았다면
        prime[ptr] = n         # 소수로 배열에 등록
        ptr += 1

for i in range(ptr):  # ptr의 소수를 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')
```

```python
# [Do it! 실습 2-10] 1,000 이하의 소수를 나열하기(알고리즘 개선 2)

counter = 0           # 곱셈과 나눗셈을 합한 횟수
ptr = 0               # 이미 찾은 소수의 개수
prime = [None] * 500  # 소수를 저장하는 배열

prime[ptr] = 2  # 2는 소수
ptr += 1

prime[ptr] = 3  # 3은 소수
ptr += 1

for n in range(5, 1001, 2):    # 홀수만을 대상으로 설정
    i = 1
    while prime[i] * prime[i] <=  n:
        counter += 2
        if n % prime[i] == 0:  # 나누어 떨어지므로 소수가 아님
            break              # 반복 중단
        i += 1
    else:                      # 끝까지 나누어 떨어지지 않았다면
        prime[ptr] = n         # 소수로 배열에 등록
        ptr += 1
        counter += 1

for i in range(ptr):  # ptr개의 소수를 출력
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')
```

## 8. 리스트 원소와 복사

```python
# [Do it! 실습 2C-7] 자료형을 정하지 않은 리스트 원소 확인하기

x = [15, 64, 7, 3.14, [32, 55], 'ABC']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
```

- 얕은 복사(Shallow Copy) : 리스트 안의 모든 원소가 참조하는 곳까지 복사
- 깊은 복사(Deep Copy) : 구성 원소 수준으로 복사
