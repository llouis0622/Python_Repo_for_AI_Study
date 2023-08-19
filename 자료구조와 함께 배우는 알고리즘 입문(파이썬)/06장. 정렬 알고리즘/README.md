# 06장. 정렬 알고리즘

# 1. 정렬 알고리즘

## 1. 정렬(Sorting)이란?

- 키를 항목값의 대소 관계에 따라 데이터 집합을 일정한 순서로 바꾸어 늘어놓는 작업
- 오름차순(Ascending Order) 정렬 : 값이 작은 데이터를 앞쪽에 늘어놓는 것
- 내림차순(Descending Order) 정렬 : 값이 큰 데이터를 앞쪽에 늘어놓는 것

### 1. 정렬 알고리즘의 안정성

- 안정적인 알고리즘 : 값이 같은 원소의 순서가 정렬한 후에도 유지되는 것
- 안정적이지 않은 알고리즘 : 정렬한 후에도 원래의 순서가 유지된다는 보장을 할 수 없음

### 2. 내부 정렬(Internal Sorting)과 외부 정렬(External Sorting)

- 내부 정렬 : 정렬할 모든 데이터를 하나의 배열에 저장할 수 있는 경우에 사용
- 외부 정렬 : 정렬할 데이터가 많아서 하나의 배열에 저장할 수 없는 경우에 사용

# 2. 버블 정렬(Bubble Sort)

- 이웃한 두 원소의 대소 관계를 비교하여 필요에 따라 교환을 반복하는 알고리즘
- 단순 교환 정렬

## 1. 버블 정렬 알아보기

- 패스(Pass) : 일련의 비교, 교환하는 과정

### 1. 버블 정렬 프로그램

```python
# [Do it! 실습 6-1] 버블 정렬 알고리즘 구현하기

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬"""
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort(x)  # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

### 2. 교환 과정 출력

```python
# [Do it! 실습 6-2] 버블 정렬 알고리즘 구현(정렬 과정을 출력)

from typing import MutableSequence

def bubble_sort_verbose(a: MutableSequence) -> None:
    """버블 정렬(정렬 과정을 출력)"""
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    n = len(a)
    for i in range(n - 1):
        print(f'패스 {i + 1}')
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'), 
                                    end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort_verbose(x)  # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

### 3. 알고리즘 개선 1

```python
# [Do it! 실습 6-3]버블 정렬 알고리즘 구현하기(알고리즘의 개선 1)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬(교환 횟수에 따른 중단)"""
    n = len(a)
    for i in range(n - 1):
        exchng = 0  # 패스에서 교환 횟수
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0:
            break

if __name__ == '__main__':
    print('버블 정렬을 합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)      # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

```python
# [Do it! 실습 6-3] 버블 정렬 알고리즘 구현하기(알고리즘의 개선 1) - 정렬 과정을 출력

from typing import MutableSequence

def bubble_sort2_verbose(a: MutableSequence) -> None:
    """버블 정렬(교환 횟수에 따른 중단)"""
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    n = len(a)
    for i in range(n - 1):
        print(f"패스 {i + 1}")
        exchng = 0  # 패스에서의 교환 횟수
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(
                    f"{a[m]:2}"
                    + ("  " if m != j - 1 else " +" if a[j - 1] > a[j] else " -"),
                    end="",
                )
            print(f"{a[n - 1]:2}")
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        for m in range(0, n - 1):
            print(f"{a[m]:2}", end="  ")
        print(f"{a[n - 1]:2}")
        if exchng == 0:  # 교환이 수행되지 않았으면 작업을 중단
            break
    print(f"비교를 {ccnt}번 했습니다.")
    print(f"교환을 {scnt}번 했습니다.")

if __name__ == "__main__":
    print("버블 정렬을 수행합니다")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num        # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    bubble_sort2_verbose(x)  # 배열 x를 버블 정렬

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
```

### 4. 알고리즘 개선 2

```python
# [Do it! 실습 6-4] 버블 정렬 알고리즘 구현하기(알고리즘의 개선 2)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬(스캔 범위를 제한)"""
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last

if __name__ == '__main__':
    print('버블 정렬을 합니다.')
    num = int(input('원솟수를 입력하세요.: '))
    x = [None] * num    # 원솟수 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort(x)      # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

```python
# [Do it! 실습 6-4] 버블 정렬 알고리즘 구현하기(알고리즘의 개선 2) - 정렬 과정을 출력

from typing import MutableSequence

def bubble_sort3_verbose(a: MutableSequence) -> None:
    """버블 정렬(스캔 범위를 제한)"""
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    n = len(a)
    k = 0
    i = 0
    while k < n - 1:
        print(f'패스 {i + 1}')
        i += 1
        last = n - 1
        for j in range(n - 1, k, -1):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__':
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort3_verbose(x)  # 배열 x를 버블

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

## 2. 셰이커 정렬(Shaker Sort) 알아보기

- 홀수 패스에서는 가장 작은 원소를 맨 앞으로 이동시키고, 짝수 패스에서는 가장 큰 원소를 맨 뒤로 이동시켜 패스의 스캔 방향을 번갈아 바꾸어 보는 것
- 양방향 버블 정렬(Bidirectional Bubble Sort), 칵테일 정렬(Cooktail Sort), 칵테일 셰이커 정렬(Cooktail Shaker Sort)

```python
# [Do it! 실습 6-5] 셰이커 정렬 알고리즘 구현하기

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last

if __name__ == '__main__':
    print('셰이커 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    shaker_sort(x)      # 배열 x를 단순 교환 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

```python
# [Do it! 실습 6-5] 셰이커 정렬 알고리즘 구현하기(정렬 과정을 출력)

from typing import MutableSequence

def shaker_sort_verbose(a: MutableSequence) -> None:
    """"셰이커 정렬(정렬 과정을 출력)"""
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    left = 0
    n = len(a)
    right = len(a) - 1
    last = right
    i = 0
    while left < right:
        print(f'패스{i + 1}')
        i += 1
        for j in range(right, left, -1):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')

        if (left == right):
             break
        print(f'패스 {i + 1}')
        i += 1
        for j in range(left, right):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j else
                                    ' +' if a[j] > a[j + 1] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j] > a[j + 1]:
                scnt += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__':
    print('셰이커 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    shaker_sort_verbose(x)  # 배열 x를 단순 교환 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

# 3. 단순 선택 정렬(Straight Selection Sort)

- 가장 작은 원소부터 선택해 알맞은 위치로 옮기는 작업을 반복하며 정렬하는 알고리즘

## 1. 단순 선택 정렬 알아보기

1. 아직 정렬하지 않은 부분에서 값이 가장 작은 원소 `a[min]` 을 선택
2. `a[min]` 과 아직 정렬하지 않은 부분에서 맨 앞에 있는 원소를 교환

```python
# [Do it! 실습 6-6] 단순 선택 정렬 알고리즘 구현

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    """단순 선택 정렬"""
    n = len(a)
    for i in range(n - 1):
        min = i  # 정렬 할 부분에서 가장 작은 원소의 인덱스
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]  # 정렬 할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환 

if __name__ == '__main__':
    print('단순 선택 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    selection_sort(x)  # 배열 x를 단순 선택 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

# 4. 단순 삽입 정렬(Straight Insertion Sort)

- 주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입하며 정렬하는 알고리즘

## 1. 단순 삽입 정렬 알아보기

- 아직 정렬되지 않은 부분의 맨 앞 원소를 정렬된 부분의 알맞은 위치에 삽입
- 종료 조건 1 : 정렬된 배열의 왼쪽 끝에 도달한 경우
- 종료 조건 2 : `tmp` 보다 작거나 키값이 같은 원소 `a[j - 1]` 을 발견할 경우
- 계속 조건 1 : `j` 가 0보다 큰 경우
- 계속 조건 2 : `a[j - 1]` 의 값이 `tmp` 보다 큰 경우

```python
# [Do it! 실습 6-7] 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('단순 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)  # 배열 x를 단순 삽입 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

## 2. 이진 삽입 정렬(Binary Insertion Sort)

- 이진 검색법을 사용하여 삽입 정렬을 하는 것

```python
# [Do it! 실습 6C-1] 이진 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0      # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1  # 검색 범위의 맨 끝 원소 인덱스

        while True:
            pc = (pl + pr) // 2  # 검색 범위의 중앙 원소 인덱스
            if a[pc] == key:     # 검색 성공
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
    
        pd = pc + 1 if pl <= pr else pr + 1  # 삽입할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

if __name__ == "__main__":
    print("이진 삽입 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num          # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    binary_insertion_sort(x)  # 배열 x를 이진 삽입 정렬

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
```

# 5. 셸 정렬(Shell Sort)

- 단순 삽입 정렬의 장점은 살리고 단점은 보완하여 더 빠르게 정렬하는 알고리즘

## 1. 단순 삽입 정렬의 문제

- 장점 : 이미 정렬을 마쳤거나 정렬이 거의 끝나가는 상태에서는 속도가 아주 빠름
- 단점 : 삽입할 위치가 멀리 떨어져 있으면 이동 횟수가 증가

## 2. 셸 정렬 알아보기

- 정렬할 배열의 원소를 그룹으로 나눠 각 그룹별로 정렬 수행
- 정렬된 그룹을 합치는 작업을 반복하여 원소의 이동 횟수를 줄임

```python
# [Do it! 실습 6-8] 셸 정렬 알고리즘 구현하기

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    """셸 정렬"""
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2

if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)  # 배열 x를 셸 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

```python
# [Do it! 실습 6-9] 셸 정렬 알고리즘 구현하기(h * 3 + 1의 수열 사용)

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    """셸 정렬(h * 3 + 1의 수열 사용)"""
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3

if __name__ == '__main__':
    print('셸 정렬을 수행합니다(h * 3 + 1의 수열 사용).')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)  # 배열 x를 셸 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```
