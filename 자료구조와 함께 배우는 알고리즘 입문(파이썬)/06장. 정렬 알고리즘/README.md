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

# 6. 퀵 정렬(Quick Sort)

- 일반적으로 사용되는 아주 빠른 정렬 알고리즘

## 1. 퀵 정렬 알아보기

- 피벗(Pivot) : 그룹을 나누는 기준, 중심축

## 2. 배열을 두 그룹으로 나누기

- `a[pl] >= x` 가 성립하는 원소를 찾을 때까지 `pl` 을 오른쪽 방향으로 스캔
- `a[pr] <= x` 가 성립하는 원소를 찾을 때까지 `pr` 을 왼쪽 방향으로 스캔
- 피벗 이하인 그룹 : `a[0], ..., a[pl - 1`
- 피벗 이상인 그룹 : `a[pr + 1], ..., a[pl - 1]`
- 피벗과 일치하는 그룹 : `a[pr + 1, ..., a[pl - 1]`

```python
# [Do it! 실습 6-10] 배열을 두 그룹으로 나누기

from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    """배열을 분할하여 출력"""
    n = len(a)
    pl = 0         # 왼쪽 커서
    pr = n - 1     # 오른쪽 커서
    x = a[n // 2]  # 피벗(가운데 원소)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'피벗은 {x}입니다.')

    print('피벗 이하인 그룹입니다.')
    print(*a[0 : pl])           # a[0] ~ a[pl - 1]

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr + 1 : pl])  # a[pr + 1] ~ a[pl - 1]

    print('피벗 이상인 그룹입니다.')
    print(*a[pr + 1 : n])       # a[pr + 1] ~ a[n - 1]

if __name__ == '__main__':
    print('배열을 나눕니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)         # 배열 x를 나누어서 출력
```

## 3. 퀵 정렬 만들기

- 중앙값을 기준으로 피벗 만들기

```python
# [Do it! 실습 6-10] 퀵 정렬 알고리즘 구현

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 요소)

    while pl <= pr:    # 실습 6-10과 같은 while 문
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num   # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)      # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

```python
# [Do it! 실습 6C-3] 퀵 정렬 알고리즘 구현(배열을 나누는 과정 출력)

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬(배열을 나누는 과정 출력)"""
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 원소)

    print(f'a[{left}] ~ a[{right}]: ', *a[left : right + 1])  # 새로 추가된 부분

    while pl <= pr:                     
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:                    
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)   
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬을 수행합니다(배열을 나누는 과정 출력).')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

## 4. 비재귀적인 퀵 정렬 만들기

- 데이터를 임시 저장하기 위해 스택 사용
- `range` : 나눌 범위에서 맨 앞 원소의 인덱스와 맨 끝 원소의 인덱스를 조합한 튜플 스택

```python
# [Do it! 실습 6-12] 퀵 정렬 알고리즘 구현(비재귀적인 퀵 정렬)

from stack import Stack  # 실습 4C-1의 파일 import
from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a [right]를 퀵 정렬(비재귀 버전)"""
    range = Stack(right - left + 1)  # 스택 생성

    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()  # 왼쪽, 오른쪽 커서를 꺼냄
        x = a[(left + right) // 2]          # 피벗(중앙 요소)

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:                        # 실습 6-10, 실습 6-11과 같음
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left, pr))    # 왼쪽 그룹의 커서를 저장
        if pl < right: range.push((pl, right))  # 오른쪽 그룹의 커서를 저장

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('비재귀적인 퀵 정렬')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

- 스택의 크기 : 정렬 대상인 배열의 원소 수와 같은 값
- 규칙 1 : 원소 수가 많은 쪽의 그룹을 먼저 푸시
- 규칙 2 : 원소 수가 적은 쪽의 그룹을 먼저 푸시

## 5. 피벗 선택하기

- 방법 1 : 나누어야 할 배열의 원소 수가 3 이상이면, 배열에서 임의의 원소 3개를 꺼내 중앙값인 원소를 피벗으로 선택
- 방법 2 : 나누어야 할 배열의 맨 앞 원소, 가운데 원소, 맨 끝 원소를 정렬한 뒤 가운데 원소와 맨 끝에서 두 번째 원소를 교환, 맨 끝에서 두 번째 원소값 `a[right - 1]` 이 피벗으로 선택, 그 동시에 나눌 대상을 `a[left + 1] ~ a[right - 2]` 로 좁힘
- 왼쪽 커서 `pl` 의 시작 위치 : `left -> left + 1`
- 오른쪽 커서 `pr` 의 시작 위치 : `right -> right - 2`

## 6. 퀵 정렬의 시간 복잡도

- `O(n log n)`
- 최악의 경우 시간 복잡도 : `O(n^2)`
- 원소 수가 9개 미만인 경우 단순 삽입 정렬로 전환
- 피벗 선택은 방법 2를 채택

```python
# [Do it! 실습 6-13] 퀵 정렬 알고리즘 구현하기(원소 수가 9개 미만인 경우 단순 삽입 정렬)

from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    """a[idx1], a[idx2], a[idx3]을 오름차순으로 정렬하고 가운데 값의 인덱스를 반환"""
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 단순 삽입 정렬"""
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    if right - left < 9:            # 원소 수가 9개 미만이면 단순 삽입 정렬을 호출
        insertion_sort(a, left, right)
    else:                           # 원소 수가 9개 이상이면 퀵 정렬을 수행
        pl = left                   # 왼쪽 커서
        pr = right                  # 오른쪽 커서
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m]

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: qsort(a, left, pr)
        if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬을 합니다(원소 수가 9개 미만이면 단순 삽입 정렬).')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

## 7. `sorted()` 함수로 정렬하기

- 전달받은 이터러블 객체의 원소를 정렬하여 list형으로 반환

```python
# [Do it! 실습 6C-4] sorted() 함수를 사용하여 정렬하기

print('sorted() 함수를 사용하여 정렬합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num    # 원소 수가 num인 배열을 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

# 배열 x를 오름차순으로 정렬
x = sorted(x)
print('오름차순으로 정렬했습니다.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')

# 배열 x를 내림차순으로 정렬
x = sorted(x, reverse = True)
print('내림차순으로 정렬했습니다.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')
```

- 튜플 정렬
    - 1단계 : `sorted()` 함수로 정렬한 원소의 나열에서 새로운 리스트 생성
    - 2단계 : 생성한 리스트를 튜플로 변환

# 7. 병합 정렬(Merge Sort)

- 배열을 앞 부분과 뒷 부분의 두 그룹으로 나누어 각각 정렬한 후 병합하는 작업을 반복하는 알고리즘

## 1. 정렬을 마친 배열의 병합

```python
# [Do it! 실습 6-14] 정렬을 마친 두 배열을 병합하기

from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0                 # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c)  # 각 배열의 원소수 

    while pa < na and pb < nb:  # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:              # a에 남은 원소를 복사
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:              # b에 남은 원소를 복사
        c[pc] = b[pb]
        pb += 1
        pc += 1

if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    print('정렬을 마친 두 배열의 병합을 수행합니다.')

    merge_sorted_list(a, b, c)  # 배열 a와 b를 병합하여 c에 저장

    print('배열 a와 b를 병합하여 배열 c에 저장하였습니다.')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'배열 c: {c}')
```

## 2. `sorted()` 함수로 병합 정렬하기

```python
# 정렬을 마친 두 배열의 병합 (heapq.merege 사용）

import heapq

a = [2, 1, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(heapq.merge(a, b))  # 배열 a와 b를 병합하여 c에 저장

print('배열 a와 b를 병합하여 배열 c에 저장하였습니다.')
print(f'배열 a: {a}')
print(f'배열 b: {b}')
print(f'배열 c: {c}')
```

## 3. 병합 정렬 만들기

- 배열의 앞 부분을 병합 정렬로 정렬
- 배열의 뒷 부분을 병합 정렬로 정렬
- 배열의 앞 부분과 뒷 부분을 병합

```python
# [Do it! 실습 6-15] 병합 정렬 알고리즘 구현하기

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합 정렬"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)            # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right)       # 배열 뒷부분을 병합 정렬

            p = j = 0
            i = k = left

            while i <= center:
                 buff[p] = a[i]
                 p += 1
                 i += 1

            while i <= right and j < p:
                 if buff[j] <= a[i]:
                     a[k] = buff[j]
                     j += 1
                 else:
                     a[k] = a[i]
                     i += 1
                 k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n           # 작업용 배열을 생성
    _merge_sort(a, 0, n - 1)    # 배열 전체를 병합 정렬
    del buff                    # 작업용 배열을 소멸

if __name__ == '__main__':
    print('병합 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)       # 배열 x를 병합 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

# 8. 힙 정렬(Heap Sort)

- 힙의 특성을 이용하여 정렬하는 알고리즘

## 1. 힙 정렬 알아보기

- 힙 : 부모의 값이 자식의 값보다 항상 크거나 작다는 조건을 만족하는 완전 이진 트리
- 부분 순서 트리(Partial Ordered Tree) : 형제의 대소 관계가 정해져 있지 않음
- 부모 : `a[(i - 1) // 2]`
- 왼쪽 자식 : `a[i * 2 + 1]`
- 오른쪽 자식 : `a[i * 2 + 2]`

## 2. 힙 정렬의 특징

- 힙에서 최댓값은 루트에 위치함
- 힙에서 최댓값인 루트를 꺼냄
- 루트 이외의 부분을 힙으로 만듦

## 3. 루트를 삭제한 힙의 재구성

1. 루트를 꺼냄
2. 마지막 원소를 루트로 이동
3. 루트에서 시작하여 자신보다 값이 큰 자식과 자리를 바꾸고 아래쪽으로 내려가는 작업을 반복, 자식의 값이 작거나 리프의 위치에 도달하면 종료

## 4. 힙 정렬 알고리즘 알아보기

1. `i` 값을 `n - 1` 로 초기화
2. `a[0]` 과 `a[i]` 를 교환
3. `a[0], a[1], ..., a[i - 1]` 을 힙으로 만듦
4. `i` 값을 1씩 감소시켜 0이 되면 종료, 그렇지 않으면 2로 돌아감

## 5. 배열을 힙으로 만들기

```python
# [Do it! 실습 6-16] 힙 정렬 알고리즘 구현하기

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """힙 정렬"""

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 힙으로 만들기"""
        temp = a[left]      # 루트

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl  # 큰 값을 선택합니다.
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):   # a[i] ~ a[n-1]을 힙으로 만들기
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]     # 최댓값인 a[0]과 마지막 원소 a[i]를 교환
        down_heap(a, 0, i - 1)      # a[0] ~ a[i-1]을 힙으로 만들기

if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

## 6. 힙 정렬의 시간 복잡도

- `O(n log n)

## 7. `heapq` 모듈을 사용하는 힙 정렬

```python
# [Do it! 실습 6C-5] 힙 정렬 알고리즘 구현하기(heapq.push와 heapq.pop를 사용）

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """힙 정렬(heapq.push와 heapq.pop를 사용)"""

    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)

if __name__ == '__main__':
    print('힙 정렬을 수행합니다(heapq.push와 heapq.pop를 사용).')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```

# 9. 도수 정렬(Counting Sort)

- 원소의 대소 관계를 판단하지 않고 빠르게 정렬하는 알고리즘, 분포수 세기 정렬(Distribution Counting)

## 1. 도수 정렬 알아보기

- 도수 분포표 만들기 → 누적 도수 분포표 만들기
- 작업용 배열 만들기
- 배열 복사하기

```python
# 도수 분포표로 정렬
for i in range(n - 1, -1, -1):
    f[a[i]] -= 1
    b[f[a[i]]] = a[i]

# 정렬 완료 후
for i in range(n):
    a[i] = b[i]
```

```python
# [Do it! 실습 6-17] 도수 정렬 알고리즘 구현하기

from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    """도수 정렬(배열 원솟값은 0 이상 max 이하)"""
    n = len(a)           # 정렬할 배열 a
    f = [0] * (max + 1)  # 누적 도수 분포표 배열 f
    b = [0] * n          # 작업용 배열 b

    for i in range(n):              f[a[i]] += 1                     # [1단계]
    for i in range(1, max + 1):     f[i] += f[i - 1]                 # [2단계]
    for i in range(n - 1, -1, -1):  f[a[i]] -= 1; b[f[a[i]]] = a[i]  # [3단계]
    for i in range(n):              a[i] = b[i]                      # [4단계]

def counting_sort(a: MutableSequence) -> None:
    """도수 정렬"""
    fsort(a, max(a))

if __name__ == '__main__':
    print('도수 정렬을 합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):  # 양수만 입력받음
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= 0: break

    counting_sort(x)  # 배열 x를 도수 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
```
