# 03장. 검색 알고리즘

# 1. 검색 알고리즘이란?

## 1. 검색과 키

- 키(Key) : 주목하는 항목, 데이터의 일부

## 2. 검색의 종류

- 배열 검색
    - 선형 검색
    - 이진 검색
    - 해시법
        - 체인법
        - 오픈 주소법
- 연결 리스트 검색
- 이진 검색 트리 검색

# 2. 선형 검색(Linear Search)

## 1. 선형 검색, 순차 검색

- 직선 모양으로 늘어선 배열에서 검색하는 경우에 원하는 키값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즈
- 선형 검색의 종료 조건
    - 검색 실패 : 검색할 값을 찾지 못하고 배열의 맨 끝을 지나간 경우
    - 검색 성공 : 검색할 값과 같은 원소를 찾는 경우

```python
# [Do it! 실습 3-1] while 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key값이 같은 원소를 선형 검색(while 문)"""
    i = 0

    while True:
        if i == len(a):
            return -1  # 검색에 실패하여 -1을 반환
        if a[i] == key:
            return i   # 검색에 성공하여 현재 조사한 배열의 인덱스를 반환
        i += 1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))  # num 값을 입력
    x = [None] * num                           # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력받기

    idx = seq_search(x, ky)                     # ky와 같은 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
```

```python
# [Do it! 실습 3-2] for 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key값이 같은 요소를 선형 검색(for 문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i  # 검색 성공(인덱스를 반환)
    return -1         # 검색 실패(-1을 반환)

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))  # num 값을 입력
    x = [None] * num                           # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력받음

    idx = seq_search(x, ky)                     # ky와 값이 같은 요소를 x에서 검색

    if idx == -1:
        print('검색 값을 갖는 요소가 존재하지 않습니다.')
    else:
        print(f'검색 값은 x[{idx}]에 있습니다.')
```

```python
# [Do it! 실습 3C-1] seq_search() 함수를 사용하여 실수 검색하기
from ssearch_while import seq_search

print('실수를 검색합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []  # 빈 리스트 x를 생성

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))  # 배열 마지막에 원소를 추가
    number += 1

ky = float(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력

idx = seq_search(x, ky)  # ky와 같은 값의 원소를 x에서 검색
if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')
```

```python
# [Do it! 실습 3C-2] seq_search() 함수를 사용하여 특정 인덱스 검색하기

from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}에서 5.6의 인덱스는 {seq_search(t, 5.6)}입니다.')
print(f'{s}에서 "n"의 인덱스는 {seq_search(s, "n")}입니다.')
print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a, "DTS")}입니다.')
```

## 2. 보초법(Sentinel Method)

- 비용을 반으로 줄이는 방법
- 보초(Sentinel) : 검색하고자 하는 키값

```python
# [Do it! 실습 3-3] 선형 검색 알고리즘(실습 3-1)을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
    a = copy.deepcopy(seq)  # seq를 복사
    a.append(key)           # 보초 key를 추가
 
    i = 0
    while True:
        if a[i] == key: 
            break  # 검색에 성공하면 while 문을 종료
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))  # num 값을 입력
    x = [None] * num                           # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력받기

    idx = seq_search(x, ky)                     # ky값과 같은 원소를 x에서 검색

    if idx == -1:
         print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
```

## 3. 선형 검색 알고리즘 코드

```python
# 선형 검색 알고리즘(검색에 실패하면 ValueError를 보냄)

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 요소를 선형 검색(for 문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i        # 검색 성공(첨자를 반환)
    raise ValueError        # 검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))  # 키 ky를 입력받음

    try:
        idx = seq_search(x, ky)  # ky와 값이 같은 요소를 x에서 검색
    except ValueError:
        print('검색 값을 갖는 요소가 존재하지 않습니다.')
    else:
        print(f'검색 값은 x[{idx}]에 있습니다.')
```

# 3. 이진 검색(Binary Search)

## 1. 이진 검색

- 원소가 오름차순이나 내림차순으로 정렬된 배열에서 좀 더 효율적으로 검색할 수 있는 알고리즘
- 이진 검색의 종료 조건
    - `a[중앙 인덱스]` 와 `key` 가 일치하는 경우
    - 검색 범위가 더 이상 없는 경우

```python
# [Do it! 실습 3-3] 이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0           # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc    # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
        if pl > pr:
            break
    return -1            # 검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                 break

    ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 ky를 입력

    idx = bin_search(x, ky)                     # ky와 같은 값의 원소를 x에서 검색

    if idx < 0:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
```

## 2. 이진 검색 알고리즘 코드

```python
# 이진 검색 알고리즘(검색에 실패할 때 ValueError를 내보냄）

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 요소를 이진 검색"""
    pl = 0           # 검색 범위 맨 앞 요소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 요소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 요소의 인덱스
        if a[pc] == key:
            return pc  # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽 절반으로 좁힘
        if pl > pr:
            break
    raise ValueError  # 검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수 num인 배열을 생성

    print('오름차순으로 입력하세요.')

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i - 1]:
                 break

    ky = int(input('검색할 값을 입력하세요.: '))  # 키 ky를 입력받음

    try:
        idx = bin_search(x, ky)                 # ky와 같은 값의 요소를 x에서 검색
    except ValueError:
        print('검색값을 갖는 요소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
```

## 3. 복잡도(Complexity)

- 알고리즘의 성능을 객관적으로 평가하는 기준
- 시간 복잡도(Time Complexity) : 실행하는 데 필요한 시간을 평가
- 공간 복잡도(Space Complexity) : 메모리와 파일 공간이 얼마나 필요한지 평가

### 1. 선형 검색의 시간 복잡도 → `O(N)`

```python
def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    while i < n:
        if a[i] == key:
            return i  # 검색에 성공하여 인덱스를 반환
        i += 1

    return -1  # 검색에 실패하여 -1을 반환
```

### 2. 이진 검색의 시간 복잡도 → `O(log N)`

```python
def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0           # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc  # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽 절반으로 좁힘
        if pl > pr:
            break
    return -1  # 검색 실패
```

### 3. 이진 검색의 실행 과정 출력하기

```python
# [Do it! 실습 3C-3] 이진 검색 알고리즘의 실행 과정을 출력

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색(실행 과정을 출력)"""
    pl = 0           # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스

        print('   |', end='')
        if pl != pc:         # pl 원소 위에 <-를 출력
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
        else: 
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:         # pr 원소 위에 ->를 출력
            print(((pr - pc) * 4 - 2) * ' ' + '->')
        else:
            print('->')
        print(f'{pc:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='') 
        print('\n   |')

        if a[pc] == key:
            return pc    # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
        if pl > pr:  
            break
    return -1            # 검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                 break

    ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 ky를 입력

    idx = bin_search(x, ky)                     # ky와 같은 값의 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
```

# 4. 해시법(Hashing)

## 1. 해시법

- `데이터를 저장할 위치 = 인덱스` 를 간단한 연산으로 구하는 것
- 해시값(Hash Value) : 데이터에 접근할 때 기준이 되는 것
- 해시 테이블(Hash Table) : 해시값을 인덱스로 하여 원소를 새로 저장한 배열
- 해시 함수(Hash Function) : 키를 해시값으로 변환하는 과정
- 버킷(Bucket) : 해시 테이블에서 만들어진 원소

## 2. 해시 충돌

- 키와 해시값의 대응 관계 : 다 대 1
- 충돌(Collision) : 저장할 버킷이 중복되는 현상
    - 체인법 : 해시값이 같은 원소를 연결 리스트로 관리
    - 오픈 주소법 : 빈 버킷을 찾을 때까지 해시 반복

## 3. 체인법(Chaining)

- 해시값이 같은 데이터를 체인 모양의 연결 리스트로 연결하는 방법
- 오픈 해시법(Open Hashing)

### 1. 해시값이 같은 데이터 저장하기

- 인덱스를 해시값으로 하는 연결 리스트의 앞쪽 노드(Head Node) 참조

### 2. `Node` 클래스 만들기

- `key` : 키(임의의 자료형)
- `value` : 값(임의의 자료형)
- `next` : 뒤쪽 노드를 참조(Node형)

```python
# 체인법으로 해시 함수 구현하기
# Do it! 실습 3-5 [A]
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key   = key    # 키
        self.value = value  # 값
        self.next  = next   # 뒤쪽 노드를 참조
```

### 3. `ChainedHash` 해시 클래스 만들기

- `capacity` : 해시 테이블의 크기(배열 table의 원소 수)
- `table` : 해시 테이블을 저장하는 list형 배열

### 4. `__init__()` 함수로 초기화하기

- 빈 해시 테이블 생성

### 5. `hash_value()` 해시 함수 만들기

- 인수 `key` 에 대응하는 해시값 구함

```python
# Do it! 실습 3-5 [B]
class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity             # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
```

### 6. 키로 원소를 검색하는 `search()` 함수

1. 해시 함수를 사용하여 키를 해시값으로 변환
2. 해시값을 인덱스로 하는 버킷에 주목
3. 버킷이 참조하는 연결 리스트를 맨 앞부터 차례로 스캔. 키와 같은 값이 발견되면 검색 성공, 원소의 맨 끝까지 스캔해서 발견되지 않으면 검색 실패

### 7. 원소를 추가하는 `add()` 함수

1. 해시 함수를 사용하여 키를 해시값으로 변환
2. 해시값을 인덱스로 하는 버킷에 주목
3. 버킷이 참조하는 연결 리스트를 맨 앞부터 차례로 선형 검색. 키와 같은 값이 발견되면 키가 이미 등록된 경우이므로 추가 실패, 원소의 맨 끝까지 발견되지 않으면 해시값인 리스트의 맨 앞에 노드 추가

```python
# Do it! 실습 3-5[C]
    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]         # 노드를 노드

        while p is not None:
            if p.key == key:
                 return p.value  # 검색 성공
            p = p.next           # 뒤쪽 노드를 주목

        return None              # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 삽입"""
        hash = self.hash_value(key)  # 삽입하는 키의 해시값
        p = self.table[hash]         # 주목하는 노드

        while p is not None:
            if p.key == key:
                return False         # 삽입 실패
            p = p.next               # 뒤쪽 노드에 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp      # 노드를 삽입
        return True                  # 삽입 성공
```

### 8. 원소를 삭제하는 `remove()` 함수

1. 해시 함수를 사용하여 키를 해시값으로 변환
2. 해시값을 인덱스로 하는 버킷에 주목
3. 버킷이 참조하는 연결 리스트를 맨 앞부터 차례로 선형 검색. 키와 같은 값이 발견되면 그 노드를 리스트에서 삭제, 그렇지 않으면 삭제 실패

### 9. 원소를 출력하는 `dump()` 함수

- 해시 테이블의 내용을 한꺼번에 통째로 출력

## 4. 체인 해시법 알고리즘 코드

```python
# [Do it! 실습 3-6] 체인법을 구현하는 해시 클래스 ChainedHash의 사용

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])  # 메뉴를 선언

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <=  n <=  len(Menu):
            return Menu(n)

hash = ChainedHash(13)     # 크기가 13인 해시 테이블을 생성

while True:
    menu = select_menu()   # 메뉴 선택

    if menu == Menu.추가:  # 추가
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val):
            print('추가를 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        if not hash.remove(key):
            print('삭제를 실패했습니다!')

    elif menu == Menu.검색:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        hash.dump()

    else:  # 종료
        break
```

## 5. 오픈 주소법(Open Addressing)

- 충돌이 발생했을 때 재해시(Rehashing)를 수행하여 빈 버킷을 찾는 방법
- 닫힌 해시법(Closed Hashing)
- 선형 탐사법(Linear Probing)

### 1. 원소 추가하기

- 빈 버킷이 나올 때까지 재해시 반복

### 2. 원소 삭제하기

- 데이터가 저장되어 있음(숫자)
- 비어 있음(-)
- 삭제 완료

### 3. 원소 검색하기

- 원하는 값을 찾을 때까지 재해시 반복

### 4. 오픈 주소법 알고리즘 코드

```python
# Do it! 실습 3-7 오픈 주소법으로 해시함수 구현하기

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1     # 비어 있음
    DELETED = 2   # 삭제 완료

class Bucket:
    """해시를 구성하는 버킷"""

    def __init__(self, key: Any = None, value: Any = None,
                       stat: Status = Status.EMPTY) -> None:
        """초기화"""
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """모든 필드에 값을 설정"""
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성

    def set_status(self, stat: Status) -> None:
        """속성을 설정"""
        self.stat = stat

class OpenHash:
    """오픈 주소법을 구현하는 해시 클래스"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                 # 해시 테이블의 크기를 지정
        self.table = [Bucket()] * self.capacity  # 해시 테이블

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)

    def rehash_value(self, key: Any) -> int:
        """재해시값을 구함"""
        return(self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """키가 key인 버킷을 검색"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        """키가 key인 갖는 원소를 검색하여 값을 반환"""
        p = self.search_node(key)
        if p is not None:
            return p.value  # 검색 성공
        else:
            return None     # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 요소를 추가"""
        if self.search(key) is not None:
            return False             # 이미 등록된 키

        hash = self.hash_value(key)  # 추가하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return False                        # 해시 테이블이 가득 참

    def remove(self, key: Any) -> int:
        """키가 key인 갖는 요소를 삭제"""
        p = self.search_node(key)  # 버킷을 주목
        if p is None:
            return False           # 이 키는 등록되어 있지 않음
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i] .stat == Status.DELETED:
                print('-- 삭제 완료 --')
```

- 열거형 `Bucket` 클래스의 필드 `stat`
    - 저장 : OCCUPIED
    - 비어 있음 : EMPTY
    - 삭제 완료 : DELETED

## 6. 오픈 주소 해시법 알고리즘 코드

```python
# [Do it! 실습 3-8] 오픈 주소법을 구현하는 해시 클래스 OpenHash 사용

from enum import Enum
from open_hash import OpenHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <=  n <= len(Menu):
            return Menu(n)

hash = OpenHash(13)  # 크기가 13인 해시 테이블 생성

while True:
    menu = select_menu()  # 메뉴 선택

    if menu == Menu.추가:  # 추가
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val):
            print('추가를 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        if not hash.remove(key):
            print('삭제를 실패했습니다!')

    elif menu == Menu.검색:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        hash.dump()

    else:  # 종료
        break
```
