# 04장. 스택과 큐

# 1. 스택이란?

## 1. 스택(Stack) 알아보기

- 데이터를 임시 저장할 때 사용하는 자료구조
- 후입선출(Last In First Out) 방식
- 푸시(Push) : 스택에 데이터를 넣는 작업
- 팝(Pop) : 스택에서 데이터를 꺼내는 작업
- 꼭대기(Top) : 푸시하고 팝하는 윗부분
- 바닥(Bottom) : 아랫부분

## 2. 스택 구현하기

- `stk` : 푸시한 데이터를 저장하는 스택 본체인 list형 배열
- `capacity` : 스택의 최대 크기를 나타내는 int형 정수
- `ptr` : 스택 포인터(Stack Pointer), 스택에 쌓여 있는 데이터의 개수
- `Empty` : 스택이 비어있으면 내보내는 예외 처리
- `Full` : 스택이 가득 차 있으면 내보내는 예외 처리
- `__init__()` 함수 : 스택 배열을 생성하는 등의 준비 작업 실행
- `__len__()` 함수 : 스택에 쌓여 있는 데이터 개수 반환, `len(stk)` 가능
- `is_empty()` 함수 : 스택이 비어 있는지 판단
- `is_full()` 함수 : 스택이 가득 차 있는지 판단

```python
# 고정 길이 스택 클래스 FixedStack 구현하기
# Do it! 실습 4-1 [A]
from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""

    class Empty(Exception):
        """비어 있는 FixedStack에 pop 또는 peek를 호출할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedStack에 push를 호출할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """초기화"""
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity      # 스택의 크기
        self.ptr = 0                  # 스택 포인터

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수를 반환"""
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어 있는가?"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택은 가득 찼는가?"""
        return self.ptr >= self.capacity
```

- `push()` 함수 : 스택에 데이터를 추가
- `pop()` 함수 : 스택의 꼭대기에서 데이터를 꺼내서 그 값을 반환
- `peek()` 함수 : 스택의 꼭대기 데이터를 들여다봄
- `clear()` 함수 : 스택에 쌓여 있는 데이터를 모두 삭제하여 빈 스택을 만듦

```python
# Do it! 실습 4-1 [B]
    def push(self, value: Any) -> None:
        """스택에 value를 푸시"""
        if self.is_full():              # 스택이 가득 참
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)"""
        if self.is_empty():             # 스택이 비어 있음
             raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """스택에서 데이터를 피크(꼭대기 데이터를 들여다 봄)"""
        if self.is_empty():             # 스택이 비어 있음
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """스택을 비움(모든 데이터를 삭제)"""
        self.ptr = 0
```

- `find()` 함수 : 찾는 값이 같은 데이터가 포함되어 있는지 확인, 배열의 어디에 들어있는지 검색
- `count()` 함수 : 스택에 쌓여 있는 데이터의 개수를 구하여 반환
- `__contains__()` 함수 : 스택에 데이터가 있는지 판단, `x in stk` 가능
- `dump()` 함수 : 스택에 쌓여 있는 모든 데이터를 바닥부터 꼭대기까지 순서대로 출력

```python
# Do it! 실습 4-1 [C]
    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 첨자(없으면 -1)를 반환"""
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기 쪽부터 선형 검색
            if self.stk[i] == value:
                return i  # 검색 성공
        return -1         # 검색 실패

    def count(self, value: Any) -> bool:
        """스택에 포함되어있는 value의 개수를 반환"""
        c = 0
        for i in range(self.ptr):  # 바닥 쪽부터 선형 검색
            if self.stk[i] == value:
                c += 1             # 들어 있음
        return c

    def __contains__(self, value: Any) -> bool:
        """스택에 value가 있는가?"""
        return self.count(value)

    def dump(self) -> None:
        """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
        if self.is_empty():  # 스택이 비어 있음
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])
```

## 3. 스택 알고리즘 코드

```python
# [Do it! 실습 4-2] 고정 길이 스택 FixedStack의 사용하기

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)  # 최대 64개를 푸시할 수 있는 스택

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()  # 메뉴 선택
    
    if menu == Menu.푸시:  # 푸시
        x = int(input('데이터를 입력하세요.: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')

    elif menu == Menu.팝:  # 팝
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.피크:  # 피크
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.검색:  # 검색
        x = int(input('검색할 값을 입력하세요.: '))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        s.dump()

    else:
        break
```

## 4. `collections.deque` 로 스택 구현하기

- `collections` 모듈 : `namedtuple()` , `deque()` , `ChainMap` , `Counter` , `OrderedDict` , `defaultdict` , `UserDict` , `UserList` , `UserString` 등
- `collection.deque` : 맨 앞과 맨 끝 앙쪽에서 원소를 추가, 삭제하는 자료구조, 덱(Deque) 구현
    - `maxlen` 속성 : `deque` 의 최대 크기를 나타내는 속성, 읽기 전용
    - `append(x)` 함수 : 맨 끝에 `x` 추가
    - `appendleft(x)` 함수 : 맨 앞에 `x` 추가
    - `clear()` 함수 : 모든 원소 삭제
    - `copy()` 함수 : 얕은 복사
    - `count(x)` 함수 : 안에 있는 `x` 와 같은 원소의 개수 계산
    - `extend(iterable)` 함수 : 순차 반복 인수에서 가져온 원소를 맨 끝에 추가하여 확장
    - `extendleft(iterable)` 함수 : 순차 반복 인수에서 가져온 원소를 맨 앞에 추가하여 확장
    - `index(x[, start[, stop]])` 함수 : 안에 있는 `x` 가운데 가장 앞쪽에 있는 원소의 위치 반환
    - `insert(i, x)` 함수 : `x` 를 `i` 위치에 삽입
    - `pop()` 함수 : 맨 끝에 있는 원소를 1개 삭제, 그 원소 반환
    - `popleft()` 함수 : 맨 앞에 있는 원소를 1개 삭제, 그 원소 반환
    - `remove(value)` 함수 : `value` 의 첫 번째 항목 삭제
    - `reverse()` 함수 : 원소를 역순으로 재정렬하고 `None` 반환
    - `rotate(n = 1)` 함수 : 모든 원소를 n값만큼 오른쪽으로 밀어냄

```python
# [Do it! 4C-1] 고정 길이 스택 클래스 구현하기(collections.deque를 사용)

from typing import Any
from collections import deque

class Stack:
    """고정 길이 스택 클래스(collections.deque를 사용)"""

    def __init__(self, maxlen: int = 256) -> None:
        """초기화 선언"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수를 반환"""
        return len(self.__stk)

    def is_empty(self) -> bool:
        """스택이 비어 있는지 판단"""
        return not self.__stk

    def is_full(self) -> bool:
        """스택이 가득 찼는지 판단"""
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        """스택에 value를 푸시"""
        self.__stk.append(value)

    def pop(self) -> Any:
        """스택에서 데이터를 팝"""
        return self.__stk.pop()

    def peek(self) -> Any:
        """스택에서 데이터를 피크"""
        return self.__stk[-1]

    def clear(self) -> None:
        """스택을 비웁니다"""
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 인덱스(없으면 -1)를 반환"""
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        """스택에 포함된 value의 개수를 반환"""
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        """스택에 value가 포함되어 있는지 판단"""
        return self.count(value)

    def dump(self) -> int:
        """스택 안에 있는 모든 데이터를 나열"""
        print(list(self.__stk))
```

## 5. 덱을 활용한 스택 알고리즘 코드

```python
# [Do it! 4C-1] 고정 길이 스택 클래스(collections.deque)를 사용하기

from enum import Enum
from stack import Stack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = Stack(64)  # 최대 64 개를 푸시할 수 있는 스택

while True:
    print(f'현재 데이터 개수：{len(s)} / {s.capacity}')
    menu = select_menu()  # 메뉴 선택

    if menu == Menu.푸시:  # 푸시
        x = int(input('데이터：'))
        try:
            s.push(x)
        except IndexError:
            print('스택이 가득 찼습니다.')

    elif menu == Menu.팝:  # 팝
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except IndexError:
           print('스택이 비어 있습니다.')

    elif menu == Menu.피크:  # 피크
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except IndexError:
           print('스택이 비어 있습니다.')

    elif menu == Menu.검색:  # 검색
        x = int(input('검색 값을 입력하세요：'))
        if x in s:
            print(f'{s.count(x)} 개를 포함하고, 맨 앞쪽의 위치는 {s.find(x)}입니다.')
        else:
            print('검색 값은 포함되어 있지 않습니다.')
            
    elif menu == Menu.덤프:  # 덤프
        s.dump()

    else:
        break
```
