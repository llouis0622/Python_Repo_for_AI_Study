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
