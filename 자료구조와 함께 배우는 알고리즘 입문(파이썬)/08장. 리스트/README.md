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

# 3. 커서를 이용한 연결 리스트

## 1. 커서로 연결 리스트 만들기

- 커서(Cursor) : 인덱스로 나타낸 포인터

```python
# [Do it! 실습 8-3] 커서로 선형 리스트 만들기

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    """선형 리스트용 노드 클래스(배열 커서 버전)"""

    def __init__(self, data = Null, next = Null, dnext = Null):
        """초기화"""
        self.data  = data   # 데이터
        self.next  = next   # 리스트의 뒤쪽 포인터
        self.dnext = dnext  # 프리 리스트의 뒤쪽 포인터

class ArrayLinkedList:
    """선형 리스트 클래스(배열 커서 버전)"""

    def __init__(self, capacity: int):
        """초기화"""
        self.head = Null                   # 머리 노드
        self.current = Null                # 주목 노드
        self.max = Null                    # 사용 중인 맨끝 레코드
        self.deleted = Null                # 프리 리스트의 머리 노드
        self.capacity = capacity           # 리스트의 크기
        self.n = [Node()] * self.capacity  # 리스트 본체
        self.no = 0

    def __len__(self) -> int:
        """선형 리스트의 노드 수를 반환"""
        return self.no

    def get_insert_index(self):
        """다음에 삽입할 레코드의 첨자를 구합니다"""
        if self.deleted == Null:  # 삭제 레코드는 존재하지 않습니다
            if self.max+1 < self.capacity:
                self.max += 1
                return self.max   # 새 레코드를 사용
            else:
                return Null       # 크기 초과
        else:
            rec = self.deleted                # 프리 리스트에서
            self.deleted = self.n[rec].dnext  # 맨 앞 rec를 꺼내기
            return rec

    def delete_index(self, idx: int) -> None:
        """레코드 idx를 프리 리스트에 등록"""
        if self.deleted == Null:      # 삭제 레코드는 존재하지 않습니다
            self.deleted = idx        # idx를 프리 리스트의
            self.n[idx].dnext = Null  # 맨 앞에 등록
        else:
            rec = self.deleted        # idx를 프리 리스트의
            self.deleted = idx        # 맨 앞에 삽입
            self.n[idx].dnext = rec

    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head             # 현재 스캔 중인 노드
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt          # 검색 성공
            cnt += 1
            ptr = self.n[ptr].next  # 뒤쪽 노드에 주목
        return Null                 # 검색 실패

    def __contains__(self, data: Any) -> bool:
        """선형 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0

    def add_first(self, data: Any):
        """머리 노드에 삽입"""
        ptr = self.head                     # 삽입하기 전의 머리 노드
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec  # rec번째 레코드에 삽입
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        """꼬리 노드에 삽입"""
        if self.head == Null:     # 리스트가 비어 있으면
            self.add_first(data)  # 맨 앞에 노드 삽입
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()

            if rec != Null:       # rec번째 레코드에 삽입
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head != Null:  # 리스트가 비어 있으면
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        """꼬리 노드를 삭제"""
        if self.head != Null:
            if self.n[self.head].next == Null:  # 노드가 1개 뿐이면
                self.remove_first()             # 머리 노드를 삭제
            else:
                ptr = self.head                 # 스캔 중인 노드
                pre = self.head                 # 스캔 중인 노드의 앞쪽 노드

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null  # pre는 삭제한 뒤의 꼬리 노드
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def remove(self, p: int) -> None:
        """레코드 p를 삭제"""
        if self.head != Null:
            if p == self.head:       # p가 머리 노드면
                self.remove_first()  # 머리 노드를 삭제
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return  # p는 리스트에 존재하지 않음
                #self.n[ptr].next = Null
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """모든 노드를 삭제"""
        while self.head != Null:  # 리스트 전체가 빌 때까지
            self.remove_first()   # 머리 노드를 삭제
        self.current = Null

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 진행"""
        if self.current == Null or self.n[self.current].next == Null:
            return False  # 진행할 수 없음
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current == Null:
            print('주목 노드가 없습니다.')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        """배열을 덤프"""
        for i in self.n:
            print(f'[{i}]  {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        """이터레이터를 반환"""
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    """클래스 ArrayLinkedList의 이터레이터용 클래스"""

    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
```

## 2. 배열 안에 비어 있는 원소 처리하기

- 삽입된 노드 저장 장소 : 배열 안에서 가장 끝 쪽에 있는 인덱스의 위치

## 3. 프리 리스트(Free List)

- 삭제된 레코드 그룹을 관리할 때 사용하는 자료구조
- `dnext` : 프리 리스트의 뒤쪽 포인터
- `deleted` : 프리 리스트의 머리 노드를 참조하는 커서
- `max` : 배열에서 맨 끝 쪽에 저장되는 노드의 레코드 번호

## 4. 커서를 이용한 연결 리스트 알고리즘 코드

```python
# [Do it! 실습 8-3] 커서를 이용한 선형 리스트 클래스 ArrayLinkedList 사용하기

from enum import Enum
from array_list import ArrayLinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
                     '꼬리노드삭제', '주목노드출력', '주목노드이동',
                     '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
                     '모든노드출력', '스캔', '종료'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = ArrayLinkedList(100)  # 선형 리스트를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.머리에노드삽입:               # 맨 앞에 노드 삽입
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))
                                    
    elif menu == Menu.꼬리에노드삽입:             # 맨 끝에 노드 삽입
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.머리노드삭제:             # 맨 앞 노드를 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:             # 맨 끝 노드를 삭제
        lst.remove_last()

    elif menu == Menu.주목노드출력:             # 주목 노드를 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:             # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드삭제:             # 주목 노드를 삭제
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:             # 모두 삭제
        lst.clear()

    elif menu == Menu.검색:                     # 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'이 키를 갖는 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:               # 멤버십을 판단
        print('그 값의 데이터는 포함되어'
              +('있습니다.' if int(input('판단할 값을 입력하세요.')) in lst else ' 있지 않습니다.'))

    elif menu == Menu.모든노드출력:             # 모든 노드를 출력
        lst.print()

    elif menu == Menu.스캔:                     # 모든 노드 스캔
        for e in lst:
             print(e)

    else:                                       # 종료
        break
```

# 4. 원형 이중 연결 리스트

## 1. 원형 리스트(Circular List) 알아보기

- 연결 리스트의 꼬리 노드가 다시 머리 노드를 가리키는 모양

## 2. 이중 연결 리스트(Doubly Linked List)

- 각 노드에는 뒤쪽 노드에 대한 포인터뿐만 아니라 앞쪽 노드에 대한 포인터가 주어짐
- `data` : 데이터에 대한 참조
- `prev` : 앞쪽 노드에 대한 참조
- `next` : 뒤쪽 노드에 대한 참조

## 3. 원형 이중 연결 리스트(Circular Doubly Linked List)

- 원형 리스트 + 이중 연결 리스트

## 4. 원형 이중 연결 리스트 만들기

- 노드 클래스 `Node`
    - `prev` 가 참이면 `self.prev` 에 `prev` 대입
    - `prev` 가 거짓이면 `self.prev` 에 `self` 대입
- 원형 이중 연결 리스트 클래스 `DoubleLinkedList`
    - `no` : 노드 개수
    - `head` : 머리 노드에 대한 참조
    - `current` : 주목 노드에 대한 참조
- `__init__()` 함수 : 비어 있는 원형 이중 연결 리스트 생성
- `__len__()` 함수 : 데이터 개수 반환
- `is_empty()` 함수 : 리스트가 비어 있는지 검사

```python
# 원형 이중 연결 리스트 구현하기
# Do it! 실습 8-5 [A] 
from __future__ import annotations
from typing import Any, Type

class Node:
    """원형 이중 연결 리스트용 노드 클래스"""

    def __init__(self, data: Any = None, prev: Node = None,
                       next: Node = None) -> None:
        """초기화"""
        self.data = data          # 데이터
        self.prev = prev or self  # 앞쪽 포인터
        self.next = next or self  # 뒤쪽 포인터

class DoubleLinkedList:
    """원형 이중 연결 리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.head = self.current = Node()  # 더미 노드를 생성
        self.no = 0

    def __len__(self) -> int:
        """선형 리스트의 노드 수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        """리스트가 비어 있는가?"""
        return self.head.next is self.head
```

- `search()` 함수 : 인수로 주어진 데이터 `data` 와 값이 같은 노드를 선형 검색
- `__contains__()` 함수 : 데이터와 값이 같은 노드가 존재하는지 판단

```python
# Do it! 실습 8-5 [B]
    def search(self, data: Any) -> Any:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head.next  # 현재 스캔 중인 노드
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt  # 검색 성공
            cnt += 1
            ptr = ptr.next  # 뒤쪽 노드에 주목
        return -1           # 검색 실패

    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는가?"""
        return self.search(data) >= 0
```

- `print_current_nod()` 함수 : 주목 노드의 데이터 `current.data` 출력
- `print()` 함수 : 리스트에 있는 모든 노드를 맨 앞에서 맨 끝까지 순서대로 출력
- `print_reverse()` 함수 : 리스트에 있는 모든 노드를 맨 끝부터 역순으로 출력
- `next()` 함수 : 주목 노드를 한 칸 뒤로 이동
- `prev()` 함수 : 주목 노드를 한 칸 앞으로 이동

```python
# Do it! 실습 8-5 [C]
    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.is_empty():
            print('주목 노드는 없습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head.next  # 더미 노드의 뒤쪽 노드
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        """모든 노드를 역순으로 출력"""
        ptr = self.head.prev  # 더미 노드의 앞쪽 노드
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.is_empty() or self.current.next is self.head:
            return False  # 이동할 수 없음
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        """주목 노드를 한 칸 앞으로 이동"""
        if self.is_empty() or self.current.prev is self.head:
            return False  # 이동할 수 없음
        self.current = self.current.prev
        return True
```

- `add()` 함수 : 주목 노드 바로 뒤에 노드 삽입
- `add_first()` 함수 : 리스트의 맨 앞에 노드 삽입
- `add_last()` 함수 : 리스트의 맨 끝에 노드 삽입

```python
# Do it! 실습 8-5[D]
    def add(self, data: Any) -> None:
        """주목 노드의 바로 뒤에 노드를 삽입"""
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        self.current = self.head  # 더미 노드 head의 바로 뒤에 삽입
        self.add(data)

    def add_last(self, data: Any) -> None:
        """맨 뒤에 노드를 삽입"""
        self.current = self.head.prev  # 꼬리 노드 head.prev의 바로 뒤에 삽입
        self.add(data)
```

- `remove_current_node()` 함수 : 주목 노드 삭제
- `remove()` 함수 : 참조하는 노드 삭제
- `remove_first()` 함수 : 머리 노드 삭제
- `remove_last()` 함수 : 꼬리 노드 삭제
- `clear()` 함수 : 더미 노드 이외의 모든 노드 삭제

```python
# Do it! 실습 8-5[E]
    def remove_current_node(self) -> None:
        """주목 노드 삭제"""
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self, p: Node) -> None:
        """노드 p를 삭제"""
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:  # p를 발견
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next

    def remove_first(self) -> None:
        """머리 노드 삭제"""
        self.current = self.head.next  # 머리 노드 head.next를 삭제
        self.remove_current_node()

    def remove_last(self) -> None:
        """꼬리 노드 삭제"""
        self.current = self.head.prev  # 꼬리 노드 head.prev를 삭제
        self.remove_current_node()

    def clear(self) -> None:
        """모든 노드를 삭제"""
        while not self.is_empty():  # 리스트 전체가 빌 때까지
            self.remove_first()  # 머리 노드를 삭제
        self.no = 0
```

```python
# Do it! 실습 8-5[F]
    def __iter__(self) -> DoubleLinkedListIterator:
        """반복자를 반환"""
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        """내림차순 반복자를 반환"""
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    """DoubleLinkedList의 반복자용 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    """DoubleLinkedList의 내림차순 반복자용 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data
```

## 5. 원형 이중 연결 리스트 알고리즘 코드

```python
# [Do it! 실습 8-6] 원형 이중 연결 리스트 클래스 DoubleLinkedList 구현하기

from enum import Enum
from double_list import DoubleLinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '주목노드바로뒤삽입',
                     '머리노드삭제', '꼬리노드삭제', '주목노드출력',
                     '주목노드이동', '주목노드역순이동', '주목노드삭제',
                     '모든노드삭제', '검색', '멤버십판단', '모든노드출력',
                     '모든노드역순출력', '모든노드스캔', '모든노드역순스캔', '종료'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = DoubleLinkedList()  # 원형・이중 연결 리스트 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.머리에노드삽입:  # 맨 앞에 노드 삽입
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.꼬리에노드삽입:  # 맨 끝에 노드 삽입
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.주목노드바로뒤삽입:  # 주목 노드 바로 뒤에 삽입
        lst.add(int(input('주목 노드 바로 뒤에 넣을 값을 입력하세요 : ')))

    elif menu == Menu.머리노드삭제:  # 맨 앞 노드 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:  # 맨 끝 노드 삭제
        lst.remove_last()

    elif menu == Menu.주목노드출력:  # 주목 노드 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:  # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드역순이동:  # 주목 노드를 한 칸 앞으로 이동
        lst.prev()

    elif menu == Menu.주목노드삭제:  # 주목 노드 삭제
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:  # 모두 삭제
        lst.clear()

    elif menu == Menu.검색:  # 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:  # 멤버십 판단
        print('그 값의 데이터는 포함되어'
              +(' 있습니다.' if int(input('판단할 값을 입력하세요.: ')) in lst else ' 있지 않습니다.'))

    elif menu == Menu.모든노드출력:  # 모든 노드를 출력
        lst.print()

    elif menu == Menu.모든노드역순출력:  # 모든 노드 역순 출력
        lst.print_reverse()

    elif menu == Menu.모든노드스캔:  # 모든 노드 스캔
        for e in lst:
             print(e)

    elif menu == Menu.모든노드역순스캔:  # 모든 노드 역순 스캔
        for e in reversed(lst):
             print(e)

    else:  # 종료
        break
```
