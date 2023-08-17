# 05장. 재귀 알고리즘

# 1. 재귀 알고리즘의 기본

## 1. 재귀(Recursion) 알아보기

- 어떠한 이벤트에서 자기 자신을 포함하고 다시 자기 자신을 사용하여 정의되는 경우

## 2. 팩토리얼(Factorial) 알아보기

- 양의 정수를 순서대로 곱한다는 의미, 순차 곱셈

```python
# [Do it! 실습 5-1] 양의 정수인 팩토리얼 구하기

def factorial(n: int) -> int:
    """양의 정수 n의 팩토리얼을 구하는 과정"""
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
```

- `math.factorial()` 함수 제공

```python
# [보충수업 5-1] 양의 정수인 팩토리얼 구하기(n이 음수면 ValueError 예외 처리 발생)

def factorial(n : int) -> int:
    """양의 정수 n의 팩토리얼값을 재귀적으로 구함(n이 음수면 ValueError 예외 처리 발생)"""
    if n > 0:
        return n * factorial(n - 1)
    elif n == 0:
        return 1
    else:
        raise ValueError

if __name__ == '__main__':
    n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
    try:
        print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
    except ValueError:
        print(f'{n}의 팩토리얼은 구할 수 없습니다.')
```

- 재귀 호출(Recursive Call) : 자기 자신과 똑같은 함수를 호출하는 것
- 직접 재귀(Direct Recursive) : 자신과 똑같은 함수를 호출하는 방식
- 간접 재귀(Indirect Recursive) : 다른 함수를 통해 자신과 똑같은 함수를 호출하는 방식

## 3. 유클리드 호제법(Euclidean Algorithm) 알아보기

- GCD(Greatest Common Divisor) : 최대공약수

```python
# [Do it! 실습 5-2] 유클리드 호제법으로 최대 공약수 구하기

def gcd(x: int, y: int) -> int:
    """정숫값 x와 y의 최대 공약수를 반환"""
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('두 정숫값의 최대 공약수를 구합니다.')
    x = int(input('첫 번째 정숫값을 입력하세요.: '))
    y = int(input('두 번째 정숫값을 입력하세요.: '))

    print(f'두 정숫값의 최대 공약수는 {gcd(x, y)}입니다.')
```

- `math.gcd()` 함수 제공

# 2. 재귀 알고리즘 분석

## 1. 재귀 알고리즘의 2가지 분석 방법

- 순수한 재귀(Genuinely Recursive) : 재귀 호출을 여러 번 실행하는 함수

```python
# [Do it! 실습 5-3] 순수한 재귀 함수 구현하기

def recur(n: int) -> int:
    """순수한 재귀 함수 recur의 구현"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('정숫값을 입력하세요.: '))

recur(x)
```

### 1. 하향식 분석(Top-Down Analysis)

- 가장 위쪽에 위치한 상자의 함수 호출부터 시작하여 계단식으로 자세히 조사해 나가는 분석 방법

### 2. 상향식 분석(Bottom-Up Analysis)

- 아래쪽부터 쌓아 올리며 분석하는 방법

## 2. 재귀 알고리즘의 비재귀적 표현

### 1. 꼬리 재귀를 제거하기

- 꼬리 재귀(Tail Recursion) : 맨 끝에서 실행된 재귀 호출

```python
# [Do it! 실습 5-4] 재귀 함수의 구현(꼬리 재귀를 제거)

def recur(n: int) -> int:
    """꼬리 재귀를 제거한 함수 recur"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2
x = int(input('정수값을 입력하세요.: '))

recur(x)
```

### 2. 재귀를 제거하기

- 스택을 사용하여 비재귀적으로 구현

```python
# [Do it! 실습 5-5] 스택으로 재귀 함수 구현하기(재귀를 제거)

from stack import Stack  # stack.py의 Stack 클래스를 임포트

def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)         # n 값을 푸시
            n = n - 1
            continue
        if not s.is_empty():  # 스택이 비어 있지 않으면
            n = s.pop()       # 저장하고 있는 값을 n에 팝
            print(n)
            n = n - 2
            continue
        break

x = int(input('정수값을 입력하세요.: '))

recur(x)
```

# 3. 하노이의 탑

## 1. 하노이의 탑(Towers of Hanoi) 알아보기

- 작은 원반이 위에, 큰 원반이 아래에 위치하는 규칙을 지키면서 기둥 3개를 이용해서 원반을 옮기는 문제

```python
# [Do it! 실습 5-6] 하노이의 탑 구현하기

def move(no: int, x: int, y: int) -> None:
    """원반을 no개를 x 기둥에서 y 기둥으로 옮김"""
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

    if no > 1:
        move(no - 1, 6 - x - y, y)

print('하노이의 탑을 구현하는 프로그램입니다.')
n = int(input('원반의 개수를 입력하세요.: '))

move(n, 1, 3)
```

# 4. 8퀸 문제

## 1. 8퀸 문제(8-Queen Problem) 알아보기

- 8개의 퀸이 서로 공격하여 잡을 수 없도록 8 × 8 체스판에 배치하는 것

## 2. 퀸 배치하기

- 8개를 배치하는 조합 : 64 × 63 × 62 × 61 × 60 × 59 × 58 × 57 = 178,462,987,637,760
- 각 열에 퀸을 1개만 배치 : 8 × 8 × 8 × 8 × 8 × 8 × 8 × 8 = 16,777,216
- 각 행에 퀸을 1개만 배치

## 3. 분기(Branching) 작업으로 문제 해결하기

- 분기 작업 : 차례대로 가지가 뻗어 나가듯이 배치 조합을 열거하는 방법
- 분할 정복법(Divide and Conquer) : 큰 문제를 작은 문제로 분할하고, 작은 문제 풀이법을 결합하여 전체 풀이법을 얻는 방법

```python
# [Do it! 실습 5-7] 각 열에 1개 퀸을 배치한 조합을 재귀적으로 나열하기

pos = [0] * 8  # 각 열에서 퀸의 위치를 출력

def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i 열에 퀸을 배치"""
    for j in range(8):
        pos[i] = j   # 퀸을 j행에 배치
        if i == 7 :  # 모든 열에 배치를 종료
            put()
        else:
            set(i + 1)  # 다음 열에 퀸을 배치

set(0)  # 0 열에 퀸을 배치
```

## 4. 한정(Bounding) 작업과 분기 한정법(Branching and Bounding Method)

- 한정 작업 : 필요하지 않은 분기를 없애서 불필요한 조합을 열거하지 않는 방법
- 분기 한정법 : 분기 작업과 한정 작업을 조합하여 문제를 풀이하는 방법

```python
# [Do it! 실습 5-8] 행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos = [0] * 8       # 각 열에서 퀸의 위치
flag = [False] * 8  # 각 행에 퀸을 배치했는지 체크

def put() -> None:
    """각 열에 놓은 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if not flag[j]:  # j 행에 퀸을 배치하지 않았으면
            pos[i] = j   # 퀸을 j 행에 배치
            if i == 7:   # 모든 열에 퀸을 배치를 완료
                put()
            else:
                flag[j] = True
                set(i + 1)  # 다음 열에 퀸을 배치
                flag[j] = False

set(0)  # 0열에 퀸을 배치
```

## 5. 8퀸 문제 해결 프로그램 만들기

```python
# [Do it! 실습 5-9] 8퀸 문제 알고리즘 구현하기

pos = [0] * 8          # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15  # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * 15  # 대각선 방향( ↘↖)으로 퀸을 배치했는지 체크

def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if(     not flag_a[j]            # j행에 퀸이 배치 되지 않았다면
            and not flag_b[i + j]        # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
            and not flag_c[i - j + 7]):  # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
            pos[i] = j  # 퀸을 j행에 배치
            if i == 7:  # 모든 열에 퀸을 배치하는 것을 완료
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)  # 다음 열에 퀸을 배치
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)  # 0열에 퀸을 배치
```

```python
# [Do it! 실습 5-9] 8퀸 문제 알고리즘 구현하기(퀸을 놓는 상황을 네모로 표시)

pos = [0] * 8          # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15  # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * 15  # 대각선 방향( ↘↖)으로 퀸을 배치했는지 체크

def put() -> None:
    """퀸을 놓는 상황을 □와 ■로 출력"""
    for j in range(8):
        for i in range(8):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()

def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 놓기"""
    for j in range(8):
        if(     not flag_a[j]           # j 행에 아직 퀸을 놓지 않았으면
            and not flag_b[i + j]       # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
            and not flag_c[i - j + 7]): # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
            pos[i] = j          # 퀸을 j 행에 놓기
            if i == 7:          # 모든 열에 퀸을 배치하는 것을 완료
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)      # 다음 열에 퀸을 놓기
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)          # 0 열에 퀸을 놓기
```
