# 07장. 문자열 검색

# 1. 브루트 포스법

## 1. 문자열 검색(String Searching)이란?

- 어떤 문자열 안에 다른 문자열이 포함되어 있는지 검사, 포함 시 어디에 위치하는지 찾아내는 것
- 텍스트(Text) : 검색되는 쪽의 문자열
- 패턴(Pattern) : 찾아내는 문자열

## 2. 브루트 포스법(Brute Force Method) 알아보기

- 선형 검색을 단순하게 확장한 알고리즘, 단순법

```python
# [Do it! 실습 7-1] 브루트 포스법으로 문자열 검색하기

def bf_match(txt: str, pat: str) -> int:
    """브루트 포스법으로 문자열 검색"""
    pt = 0  # txt(텍스트)를 따라가는 커서
    pp = 0  # pat(패턴)를 따라가는 커서

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')  # 텍스트용 문자열
    s2 = input('패턴을 입력하세요.: ')    # 패턴용 문자열

    idx = bf_match(s1, s2)  # 문자열 s1~s2를 브루트 포스법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치합니다.')
```

## 3. 멤버십 연산자와 표준 라이브러리를 사용한 문자열 검색

### 1. 멤버십 연산자(Membership Operator)로 구현하기

- `ptn in txt` : `ptn` 은 `txt` 에 포함되었는가
- `ptn not in txt` : `ptn` 은 `txt` 에 포함되지 않았는가

### 2. `find, index` 계열 함수로 구현하기

- `str.find(sub[, start[, end]])` : `str` 의 `[start:end]` 에 `sub` 가 포함되면 그 가운데 가장 작은 인덱스를 반환하고, 그렇지 않으면 -1 반환
- `str.rfind(sub[, start[, end]])` : `str` 의 `[start:end]` 에 `sub` 가 포함되면 그 가운데 가장 큰 인덱스를 반환하고, 그렇지 않으면 -1 반환
- `str.index(sub[, start[, end]])` : `str` 의 `[start:end]` 에 `sub` 가 포함되면 그 가운데 가장 작은 인덱스를 반환하고, 그렇지 않으면 -1 반환. `sub` 가 발견되지 않으면 `ValueError` 예외 처리
- `str.rindex(sub[, start[, end]])` : `str` 의 `[start:end]` 에 `sub` 가 포함되면 그 가운데 큰 인덱스를 반환하고, 그렇지 않으면 -1 반환. `sub` 가 발견되지 않으면 `ValueError` 예외 처리

```python
# 문자열에 포함되어 있는 문자열을 검색(find 계열 함수）

txt = input('문자열 txt: ')  # 문자열 나열
ptn = input('문자열 ptn: ')  # 검색할 문자

c = txt.count(ptn)

if c == 0:                                                  # 포함된 문자가 없음
    print('ptn은 txt에 포함되어 있지 않습니다.')
elif c == 1:                                                # 포함된 문자가 １개만 있는 경우
    print('ptn이 txt에 포함되어 있는 인덱스: ', txt.find(ptn))
else:                                                       # 포함된 문자가 2개 이상 있는 경우
    print('ptn이 txt에 포함되어 있는 맨 앞 인덱스: ', txt.find(ptn))
    print('ptn이 txt에 포함되어 있는 맨 끝 인덱스: ', txt.rfind(ptn))
```

```python
# 문자열에 포함되어 있는 문자열을 검색(index 계열 함수)

txt = input('문자열 txt: ')
ptn = input('문자열 ptn: ')

c = txt.count(ptn)

if c == 0:                                                  # 포함된 문자가 없음
    print('ptn은 txt에 포함되어 있지 않습니다.')
elif c == 1:                                                # 포함된 문자가 １개만 있는 경우
    print('ptn이 txt에 포함되어 있는 인덱스: ', txt.index(ptn))
else:                                                       # 포함된 문자가 2개 이상 있는 경우
    print('ptn이 txt에 포함되어 있는 맨 앞 인덱스: ', txt.index(ptn))
    print('ptn이 txt에 포함되어 있는 맨 끝 인덱스: ', txt.rindex(ptn))
```

### 3. `with` 계열 함수로 구현하기

- `str.startswith(prefix[, start[, end]])` : 문자열이 `prefix` 로 시작하면 True를, 그렇지 않으면 False를 반환
- `str.endswith(prefix[, start[, end]])` : 문자열이 `suffix` 로 끝나면 True를, 그렇지 않으면 False를 반환

# 2. KMP법(Knuth-Morris-Pratt)

## 1. KMP법 알아보기

- 텍스트와 패턴 안에서 겹치는 문자열을 찾아내 검사를 다시 시작할 위치를 구하여 패턴의 이동을 되도록이면 크게 하는 알고리즘
- 검사했던 결과를 버리지 않고 효율적으로 활용하는 알고리즘
- 건너뛰기 표(Skip Table) 작성

```python
# [Do it! 실습 7-2] KMP법으로 문자열 검색하기

def kmp_match(txt: str, pat: str) -> int:
    """KMP법에 의한 문자열 검색"""
    pt = 1  # txt를 따라가는 커서
    pp = 0  # pat를 따라가는 커서
    skip = [0] * (len(pat) + 1)  # 건너뛰기 표

    # 건너뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')  # 텍스트용 문자열
    s2 = input('패턴을 입력하세요.: ')    # 패턴용 문자열

    idx = kmp_match(s1, s2)  # 문자열 s1~s2를 KMP법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치합니다.')
```

# 3. 보이어 • 무어법

## 1. 보이어 • 무어법(Boyer-Moor Method) 알아보기

- 패턴의 끝 문자에서 시작하여 앞쪽을 향해 검사를 수행. 이 과정에서 일치하지 않는 문자를 발견하면 미리 준비한 표를 바탕으로 패턴이 이동하는 값 결정

```python
# [Do it! 실습 7-3] 보이어 무어법으로 문자열 검색하기(0~255 문자)

def bm_match(txt: str, pat: str) -> int:
    """보이어 무어법에 의한 문자열 검색"""
    skip = [None] * 256  # 건너뛰기 표

    # 건너뛰기 표 만들기
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # 검색하기
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
              else len(pat) - pp

    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')  # 텍스트 문자열
    s2 = input('패턴을 입력하세요.: ')    # 패턴 문자열

    idx = bm_match(s1, s2)  # 문자열 s1~s2를 KMP법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치합니다.')
```
