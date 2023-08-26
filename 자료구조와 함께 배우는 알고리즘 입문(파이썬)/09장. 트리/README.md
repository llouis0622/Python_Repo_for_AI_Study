# 09장. 트리

# 1. 트리 구조

## 1. 트리(Tree)의 구조와 관련 용어

- 노드(Node) + 가지(Edge)
- 루트(Root) : 트리의 가장 위쪽에 있는 노드
- 리프(Leaf) : 가장 아래쪽에 있는 노드, 단말 노드(Terminal Node), 외부 노드(External Node)
- 비단말 노드(Non-Terminal Node) : 리프를 제외한 노드, 내부 노드(Internal Node)
- 자식(Child) : 어떤 노드와 가지가 연결되었을 때 아래쪽 노드
- 부모(Parent) : 어떤 노드와 가지가 연결되었을 때 가장 위쪽에 있는 노드
- 형제(Sibling) : 부모가 같은 노드
- 조상(Ancestor) : 어떤 노드에서 위쪽으로 가지를 따라가면 만나는 모든 노드
- 자손(Descendant) : 어떤 노드에서 아래쪽으로 가지를 따라가면 만나는 모든 노드
- 레벨(Level) : 루트에서 얼마나 멀리 떨어져 있는지를 나타내는 것
- 차수(Degree) : 각 노드가 갖는 자식의 수
- 높이(Height) : 루트에서 가장 멀리 있는 리프까지의 거리, 리프 레벨의 최댓값
- 서브트리(Subtree) : 어떠 노드를 루트로 하고 그 자손으로 구성된 트리
- 빈 트리(None Tree) : 노드와 가지가 전혀 없는 트리, 널 트리(Null Tree)

## 2. 순서 트리와 무순서 트리

- 순서 트리(Ordered Tree) : 형제 노드의 순서 관계가 있는 트리
- 무순서 트리(Unordered Tree) : 형제 노드의 순서를 구별하지 않는 트리

## 3. 순서 트리의 검색

### 1. 너비 우선 검색(Breadth-First Search, BFS)

- 낮은 레벨부터 왼쪽에서 오른쪽으로 검색하고, 한 레벨에서 검색을 마치면 다음 레벨로 내려가는 방법
- 폭 우선 검색, 가로 검색, 수평 검색

### 2. 깊이 우선 검색(Depth-First Search, DFS)

- 리프에 도달할 때까지 아래쪽으로 내려가면서 검색하는 것을 우선으로 하는 방법
- 세로 검색, 수직 검색

### 3. 전위 순회(Preorder)

- 노드 방문 → 왼쪽 자식 → 오른쪽 자식

### 4. 중위 순회(Inorder)

- 왼쪽 자식 → 노드 방문 → 오른쪽 자식

### 5. 후위 순회(Postorder)

- 왼쪽 자식 → 오른쪽 자식 → 노드 방문

# 2. 이진 트리와 이진 검색 트리

## 1. 이진 트리(Binary Tree) 알아보기

- 노드가 왼쪽 자식과 오른쪽 자식만을 갖는 트리
- 왼쪽 서브트리(Left Subtree) : 왼쪽 자식을 루트로 하는 서브트리
- 오른쪽 서브트리(Right Subtree) : 오른쪽 자식을 루트로 하는 서브트리

## 2. 완전 이진 트리(Complete Binary Tree) 알아보기

- 루트부터 아래쪽 레벨로 노드가 가득 차 있고, 같은 레벨 안에서 왼쪽부터 오른쪽으로 노드가 채워져 있는 이진 트리
- 마지막 레벨을 제외하고 모든 레벨에 노드가 가득 차 있음
- 마지막 레벨에 한해서 왼쪽부터 오른쪽으로 노드를 채우되 반드시 끝까지 채우지 않아도 됨

## 3. 균형 검색 트리(Self-Balancing Search Tree)

- 직선 모양의 트리
- 높이를 O(log n)으로 제한
- 이진 균형 검색 트리
    - AVL 트리(AVL Tree)
    - 레드 • 블랙 트리(Red-Black Tree)
- 일반 균형 검색 트리
    - B 트리(B Tree)
    - 2-3 트리(2-3 Tree)

## 4. 이진 검색 트리(Binary Search Tree) 알아보기

- 왼쪽 서브트리 노드의 키 값은 자신의 노드 키 값보다 작아야 함
- 오른쪽 서브트리 노드의 키 값은 자신의 노드 키 값보다 커야 함

## 5. 이진 검색 트리 만들기

- 노드 클래스 `Node`
    - `key` : 키
    - `value` : 값
    - `left` : 왼쪽 자식 노드에 대한 참조
    - `right` : 오른쪽 자식 노드에 대한 참조
- 이진 검색 트리 클래스 `BinarySearchTree`

```python
# [Do it! 실습 9-1] 이진 검색 트리의 구현

from __future__ import annotations
from typing import Any, Type

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key: Any, value: Any, left: Node = None,
                 right: Node = None):
        """생성자"""
        self.key = key      # 키
        self.value = value  # 값
        self.left = left    # 왼쪽 포인터(왼쪽 자식 참조)
        self.right = right  # 오른쪽 포인터(오른쪽 자식 참조)

class BinarySearchTree:
    """이진 검색 트리"""

    def __init__(self):
        """초기화"""
        self.root = None  # 루트
```

- `search()` 함수 : 키 값으로 노드 검색

```python
# Do it! 실습 9-1[B]
    def search(self, key: Any) -> Any:
        """키 key를 갖는 노드를 검색"""
        p = self.root           # 루트에 주목
        while True:
            if p is None:       # 더 이상 진행할 수 없으면
                return None     # 검색 실패
            if key == p.key:    # key와 노드 p의 키가 같으면
                return p.value  # 검색 성공
            elif key < p.key:   # key 쪽이 작으면
                p = p.left      # 왼쪽 서브 트리에서 검색
            else:               # key 쪽이 크면
                p = p.right     # 오른쪽 서브 트리에서 검색
```

- `add()` 함수 : 노드 삽입

```python
# Do it! 실습 9-1[C]
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고, 값이 value인 노드를 삽입"""

        def add_node(node: Node, key: Any, value: Any) -> None:
            """node를 루트로 하는 서브 트리에 키가 key이고, 값이 value인 노드를 삽입"""
            if key == node.key:
                return False  # key가 이진검색트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
```

- `remove()` 함수 : 노드 삭제
    - 자식 노드가 없는 노드 삭제
        - 삭제할 노드가 부모 노드의 왼쪽 자식인 경우 : 부모의 왼쪽 포인터를 `None`
        - 삭제할 노드가 부모 노드의 오른쪽 자식인 경우 : 부모의 오른쪽 포인터를 `None`
    - 자식 노드가 1개인 노드 삭제
        - 삭제할 노드가 부모 노드의 왼쪽 자식인 경우 : 부모의 왼쪽 포인터가 삭제할 노드의 자식을 가리키도록 업데이트
        - 삭제할 노드가 부모 노드의 오른쪽 자식인 경우 : 부모의 오른쪽 포인터가 삭제할 노드의 자식을 가리키도록 업데이트
    - 자식 노드가 2개인 노드 삭제
        - 삭제할 노드의 왼쪽 서브트리에서 키 값이 가장 큰 노드 검색
        - 검색한 노드를 삭제 위치로 옮김. 검색한 노드의 데이터를 삭제할 노드 위치에 복사
        - 옮긴 노드 삭제. 자식 노드의 개수에 따라 삭제

```python
# Do it! 실습 9-1[D]
    def remove(self, key: Any) -> bool:
        """키가 key인 노드를 삭제"""
        p = self.root           # 스캔 중인 노드
        parent = None           # 스캔 중인 노드의 부모 노드
        is_left_child = True    # p는 parent의 왼쪽 자식 노드인지 확인

        while True:
            if p is None:       # 더 이상 진행할 수 없으면
                return False    # 그 키는 존재하지 않음

            if key == p.key:    # key와 노드 p의 키가 같으면
                break           # 검색 성공
            else:
                parent = p                  # 가지를 내려가기 전에 부모를 설정
                if key < p.key:             # key 쪽이 작으면
                    is_left_child = True    # 여기서 내려가는 것은 왼쪽 자식
                    p = p.left              # 왼쪽 서브 트리에서 검색
                else:                       # key 쪽이 크면
                    is_left_child = False   # 여기서 내려가는 것은 오른쪽 자식
                    p = p.right             # 오른쪽 서브 트리에서 검색

        if p.left is None:                  # p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right       # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right      # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None:               # p에 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left        # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left       # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
        else:
            parent = p
            left = p.left                   # 서브 트리 안에서 가장 큰 노드
            is_left_child = True
            while left.right is not None:   # 가장 큰 노드 left를 검색
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key                # left의 키를 p로 이동
            p.value = left.value            # left의 데이터를 p로 이동
            if is_left_child:
                parent.left = left.left     # left를 삭제
            else:
                parent.right = left.left    # left를 삭제
        return True
```

- `dump()` 함수 : 모든 노드를 키의 오름차순으로 출력, 중위 순회의 깊이 우선 검색

```python
# Do it! 실습 9-1[E]
    def dump(self) -> None:
        """덤프(모든 노드를 키의 오름차순으로 출력)"""

        def print_subtree(node: Node):
            """node를 루트로 하는 서브 트리의 노드를 키의 오름차순으로 출력"""
            if node is not None:
                print_subtree(node.left)            # 왼쪽 서브 트리를 오름차순으로 출력
                print(f'{node.key}  {node.value}')  # node를 출력
                print_subtree(node.right)           # 오른쪽 서브 트리를 오름차순으로 출력

        print_subtree(self.root)
```

- `min_key()` 함수 : 가장 작은 키를 찾아 반환
- `max_key()` 함수 : 가장 큰 키를 찾아 반환

```python
# Do it! 실습 9-1[F]
    def min_key(self) -> Any:
        """가장 작은 키"""
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        """가장 큰 키"""
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
```

## 6. 이진 검색 트리 알고리즘 코드

```python
# [Do it! 실습 9-2] 이진 검색 트리 클래스 BinarySearchTree 사용하기

from enum import Enum
from bst import BinarySearchTree

Menu = Enum('Menu', ['삽입', '삭제', '검색', '덤프', '키의범위', '종료'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()  # 이진 검색 트리를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.삽입:  # 삽입
        key = int(input('삽입할 키를 입력하세요.: '))
        val = input('삽입할 값을 입력하세요.: ')
        if not tree.add(key, val):
            print('삽입에 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        tree.remove(key)

    elif menu == Menu.검색:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키를 갖는 값은 {t}입니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.덤프:  # 덤프(모두 출력)
        tree.dump()

    elif menu == Menu.키의범위 :  # 키의 범위(최솟값과 최댓값)
        print(f'키의 최솟값은 {tree.min_key()}입니다.')
        print(f'키의 최댓값은 {tree.max_key()}입니다.')

    else:  # 종료
        break
```
