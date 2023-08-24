# 08장. 리스트

# 1. 연결 리스트

- 리스트(List) : 데이터에 순서를 매겨 늘어놓은 자료구조

## 1. 연결 리스트(Linked List) 알아보기

- 순서가 있는 데이터를 늘어놓은 자료구조, 선형 리스트(Linear List)
- 노드(Node) : 각각의 원소(Element)
- 포인터(Pointer) : 뒤쪽 노드를 가리키는 것
- 머리 노드(Head Node) : 맨 앞에 있는 노드
- 꼬리 노드(Tail Node) : 맨 끝에 있는 노드
- 앞쪽 노드(Predecessor Node) : 각 노드에서 바로 앞에 있는 노드
- 뒤쪽 노드(Successor Node) : 각 노드에서 바로 뒤에 있는 노드

## 2. 배열로 연결 리스트 만들기

- 뒤쪽 노드 꺼내기 : 인덱스 값이 1만큼 큰 원소에 접근하여 획득
- 노드의 삽입과 삭제 : 배열 안의 일부 원소를 모두 이동

# 2. 포인터를 이용한 연결 리스트

## 1. 포인터로 연결 리스트 만들기

- 자기 참조형(Self-Referential) : 자신과 같은 형의 인스턴스를 참조하는 필드가 있는 구조

```python
# [Do it! 실습 8-1] 포인터로 연결 리스트 만들기

from __future__ import annotations
from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""

    def __init__(self, data: Any = None, next: Node = None):
        """초기화"""
        self.data = data  # 데이터
        self.next = next  # 뒤쪽 포인터
```

- 노드 클래스 `Node` : 필드, `__init__()` 함수
- 필드
    - `data` : 데이터(데이터에 대한 참조)
    - `next` : 뒤쪽 포인터(뒤쪽 노드에 대한 참조)

```python
# Do it! 실습 8-1 [B]
class LinkedList:
    """연결 리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.no = 0          # 노드의 개수
        self.head = None     # 머리 노드
        self.current = None  # 주목 노드

    def __len__(self) -> int:
        """연결 리스트의 노드 개수를 반환"""
        return self.no
```

- 연결 리스트 클래스 `LinkedList`
    - `no` : 리스트에 등록되어 있는 노드의 개수
    - `head` : 머리 노드에 대한 참조
    - `current` : 현재 주목하고 있는 노드에 대한 참조
- `__init__()` 함수 : 노드가 하나도 없는 빈 연결 리스트 생성
- `__len__()` 함수 : 연결 리스트의 노드 개수 반환
- `search()` 함수 : 인수로 주어진 데이터 `data` 와 값이 같은 노드 검색
- 종료 조건 1 : 검색 조건을 만족하는 노드를 발견하지 못하고 꼬리 노드까지 왔을 경우
- 종료 조건 2 : 검색 조건을 만족하는 노드를 발견한 경우

```python
# Do it! 실습 8-1 [C]
    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는가?"""
        return self.search(data) >= 0
```

- `__contains__()` 함수 : 리스트에 `data` 와 값이 같은 노드가 포함되어 있는지를 판단
- `add_first()` 함수 : 리스트의 맨 앞에 노드를 삽입

```python
# Do it! 실습 8-1 [D]
    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        ptr = self.head  # 삽입 전의 머리 노드
        self.head = self.current = Node(data, ptr)
        self.no += 1
```

- `add_last()` 함수 : 리스트의 맨 끝에 노드를 삽입
    - 리스트가 비어 있을 때 : `add_first()` 함수 호출
    - 리스트가 비어 있지 않을 때 : 리스트의 맨 끝에 노드 삽입

```python
# Do it! 실습 8-1 [E]
    def add_last(self, data: Any):
        """맨 끝에 노드를 삽입"""
        if self.head is None :    # 리스트가 비어 있으면
            self.add_first(data)  # 맨앞에 노드 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next  # while문을 종료할 때 ptr은 꼬리 노드를 참조
            ptr.next = self.current = Node(data, None)
            self.no += 1
```

- `remove_first()` 함수 : 머리 노드 삭제

```python
# Do it! 실습 8-1 [F]
    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None:  # 리스트가 비어 있으면
            self.head = self.current = self.head.next
        self.no -= 1
```

- `remove_last()` 함수 : 꼬리 노드 삭제
    - 리스트에 노드가 하나만 존재할 때 : `remove_first()` 함수 호출
    - 리스트에 노드가 2개 이상 존재할 때 : 리스트의 맨 끝에서 노드 삭제

```python
# Do it! 실습 8-1 [G]
    def remove_last(self):
        """꼬리 노드 삭제"""
        if self.head is not None:
            if self.head.next is None :  # 노드가 1개 뿐이라면
                self.remove_first()      # 머리 노드를 삭제
            else:
                ptr = self.head  # 스캔 중인 노드
                pre = self.head  # 스캔 중인 노드의 앞쪽 노드

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next # while문 종료시 ptr은 꼬리 노드를 참조하고 pre는 맨끝에서 두 번째 노드를 참조
                pre.next = None  # pre는 삭제 뒤 꼬리 노드
                self.current = pre
                self.no -= 1
```

- `remove()` 함수 : 임의의 노드를 삭제
    - 주어진 노드가 머리 노드일 때 : `remove_first()` 함수 호출
    - 주어진 노드가 머리 노드가 아닐 때 : 리스트에서 주어진 노드가 참조하는 노드 삭제
- `remove_current_node()` 함수 : 현재 주목하고 있는 노드 삭제
- `clear()` 함수 : 모든 노드 삭제
- `next()` 함수 : 주목 노드를 한 칸 뒤쪽으로 이동

```python
# Do it! 실습 8-1 [H]
    def remove(self, p: Node) -> None:
        """노드 p를 삭제"""
        if self.head is not None:
            if p is self.head:       # p가 머리 노드이면
                self.remove_first()  # 머리 노드를 삭제
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return  # ptr은 리스트에 존재하지 않음
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """전체 노드를 삭제"""
        while self.head is not None:  # 전체가 비어 있게 될 때까지
            self.remove_first()       # 머리 노드를 삭제
        self.current = None
        self.no = 0

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 진행"""
        if self.current is None or self.current.next is None:
            return False  # 진행할 수 없음
        self.current = self.current.next
        return True
```

- `print_current_node()` 함수 : 주목 노드 출력
- `print()` 함수 : 리스트 순서대로 모든 노드의 데이터 출력

```python
# Do it! 실습 8-1 [I]
    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
```

```python
# Do it! 실습 8-1 [J]
    def __iter__(self) -> LinkedListIterator:
        """이터레이터(반복자)를 반환"""
        return LinkedListIterator(self.head)

class LinkedListIterator:
    """클래스 LinkedList의 이터레이터(반복자)용 클래스"""

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
```

## 2. 포인터를 이용한 연결 리스트 알고리즘 코드

```python
# [Do it! 실습 8-2] 포인터로 이용한 연결 리스트 클래스 LinkedList 사용하기

from enum import Enum
from linked_list import LinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
                     '꼬리노드삭제', '주목노드출력', '주목노드이동',
                     '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
                     '모든노드출력', '스캔', '종료',])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = LinkedList()  # 연결 리스트를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.머리에노드삽입:  # 맨 앞에 노드 삽입
        lst.add_first(int(input('머리에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.꼬리에노드삽입:  # 맨 끝에 노드 삽입
        lst.add_last(int(input('꼬리에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.머리노드삭제:  # 맨 앞 노드 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:  # 맨 끝 노드 삭제
        lst.remove_last()

    elif menu == Menu.주목노드출력:  # 주목 노드 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:  # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드삭제:  # 주목 노드 삭제
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:  # 모든 노드를 삭제
        lst.clear()

    elif menu == Menu.검색:  # 노드를 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:  # 멤버십 판단
        print('그 값의 데이터는 포함되어' + (' 있습니다.' if int(input('멤버십 판단할 값을 입력하세요.: ')) in lst else ' 있지 않습니다.'))

    elif menu == Menu.모든노드출력:  # 모든 노드 출력
        lst.print()

    elif menu == Menu.스캔:  # 모든 노드 스캔
        for e in lst:
            print(e)

    else:  # 종료
        break
```
