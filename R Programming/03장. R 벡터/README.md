# 03. R 벡터

# 1. 숫자 벡터

## 1. `c()` 함수를 이용한 숫자 벡터 만들기

- 숫자 연결하여 벡터 만들기
    
    ```r
    y <- c(2, 4, 6, 8, 10)
    
    x <- c(1.2, 3.5, 5.6, 7.3, 9.9)
    ```
    
- 길이가 2 이상인 벡터 연결하여 새 백터 만들기
    
    ```r
    z <- c(x, y)
    # 1.2 3.5 5.6 7.3 9.9 2.0 4.0 6.0 8.0 10.0
    ```
    
- 여러 줄에 걸친 벡터 출력
    
    ```r
    w <- c(x, y, z)
    #  [1] 1.2 3.5 5.6 7.3 9.9 2.0 4.0 6.0 8.0 10.0
    # [11] 1.2 3.5 5.6 7.3 9.9 2.0 4.0 6.0 8.0 10.0
    ```
    

## 2. 패턴을 이용한 숫자 벡터 만들기

- `n:m`
    
    ```r
    1:10
    # 1 2 3 4 5 6 7 8 9 10
    
    2.3:-5
    # 2.3 1.3 0.3 -0.7 -1.7 -2.7 -3.7 -4.7
    ```
    
- `seq()`
    
    ```r
    seq(n, m)
    
    seq(n, m, by=k)
    
    seq(length=j, from=n, by=k)
    ```
    
    ```r
    seq(5, 15)
    # 5 6 7 8 9 10 11 12 13 14 15
    
    seq(5, 15, by=2)
    # 5 7 9 11 13 15
    
    seq(length=10, from=-3, by=0.5)
    # -3.0 -2.5 -2.0 -1.5 -1.0 -0.5 0.0 0.5 1.0 1.5
    ```
    
- `along()`
    
    ```r
    seq(along=y)
    # 1 2 3 4 5
    ```
    
- `rep()`
    
    ```r
    y <- c(1:5, 0:-5)
    rep(y, times=2)
    # 1 2 3 4 5 0 -1 -2 -3 -4 -5 1 2 3 4 5 0 -1 -2 -3 -4 -5
    
    rep(1, times = 10)
    # 1 1 1 1 1 1 1 1 1 1
    
    rep(y, each = 2)
    # 1 1 2 2 3 3 4 4 5 5 0 0 -1 -1 -2 -2 -3 -3 -4 -4 -5 -5
    ```
    

## 3. 숫자 벡터의 연산

- 요소 단위 연산(Elementwise Operation)
    
    ```r
    x <- seq(length=5, from=0, by=10)
    # 0 10 20 30 40
    
    y <- 1:5
    # 1 2 3 4 5
    
    x + y
    # 1 12 23 34 45
    
    x - y
    # -1 8 17 26 35
    
    x * y
    # 0 20 60 120 200
    
    x / y
    # 0.000000 5.000000 6.666667 7.500000 8.000000
    ```
    
- 벡터 재사용(Recycling)
    
    ```r
    z <- rep(x, times=2)
    # 0 10 20 30 40 0 10 20 30 40 
    
    z + y
    # 1 12 23 34 45 1 12 23 34 45
    
    w <- c(z, 50)
    # 0 10 20 30 40 0 10 20 30 40 50
    
    w + y
    # Warning in w + y: 두 객체의 길이가 서로 배수관계에 있지 않습니다
    # 1 12 23 34 45  1 12 23 34 45 51
    ```
    
- 숫자 벡터를 인수로 하는 함수
    - `length(x)` : 길이
    - `sum(x)` : 모든 요소 합
    - `mean(x)` : 평균
    - `var(x)` : 분산
    - `sd(x)` : 표준편차
    - `range(x)` : 최소값, 최대값
    - `min(x) / max(x)` : 최소값 / 최대값
    - `median(x)` : 중위수
    - `rank(x)` : 작은 것부터 큰 것까지의 순위
    - `sort(x)` : 정렬
    - `order(x)` : 가장 작은 값부터 가장 큰 값까지의 위치
    - `which.max(x)` : 최대값 위치
    - `which.min(x)` : 최소값 위치
    - `which(x)` : 조건 만족 요소 위치

# 2. 논리 벡터

- `c()` 로 논리 벡터 만들기
    
    ```r
    a <- c(T, F, T)
    # TRUE FALSE  TRUE
    ```
    
- 비교 연산으로 논리 벡터 만들기
    
    ```r
    y <- 1:5
    y > 3
    # FALSE FALSE FALSE TRUE TRUE
    ```
    
- 논리 연산으로 논리 벡터 만들기
    
    ```r
    b <- !a
    # FALSE TRUE FALSE
    
    a & b
    # FALSE FALSE FALSE
    ```
    
- 논리 벡터 함수 : `any(), all()`
    
    ```r
    any(c(F, F, F))
    # FALSE
    
    all(c(T, F, T))
    # FALSE
    ```
    
- 논리 벡터 함수 : `ifelse()`
    
    ```r
    x <- c(T, F, F, T, F)
    a <- 1:5
    b <- -1:-5
    y <- ifelse(x, a, b)
    # 1 -2 -3  4 -5
    ```
    

# 3. 문자 벡터

- 문자 벡터 만들기
    
    ```r
    students <- c("길동", "철수", "Tom")
    # "길동" "철수" "Tom"
    
    n <- 1:3
    num <- as.character(n)
    # "1" "2" "3"
    ```
    
- `paste()` 로 문자 벡터 연결하기
    
    ```r
    paste(students, num)
    # "길동 1" "철수 2" "Tom 3"
    
    paste(students, num, sep="")
    # "길동1" "철수2" "Tom3"
    
    paste(students, num, sep="-")
    # "길동-1" "철수-2" "Tom-3"
    
    paste(students, 1:2)
    # "길동 1" "철수 2" "Tom 1"
    ```
    
- `strsplit()` 로 문자 벡터 분리하기
    
    ```r
    x <- c("2015-3-15 10:12:12", "2016-10-11 11:12:13", "2014-7-8 02:03:04")
    strsplit(x, split=" ")
    # [[1]] "2015-3-15" "10:12:12" 
    # [[2]] "2016-10-11" "11:12:13"  
    # [[3]] "2014-7-8" "02:03:04"
    
    strsplit(x, split="-")
    # [[1]] "2015" "3" "15 10:12:12"
    # [[2]] "2016" "10" "11 11:12:13"
    # [[3]] "2014" "7" "8 02:03:04"
    
    strsplit(x, split=c("-", ":", " "))
    # [[1]] "2015" "3" "15 10:12:12"
    # [[2]] "2016-10-11 11" "12" "13"
    # [[3]] "2014-7-8" "02:03:04"
    ```
    
- `nchar()` 로 문자수 세기
    
    ```r
    nchar("날짜")
    # 2
    a <- c("날짜", "day", "date", "날짜와 시간")
    # 2 3 4 6
    ```
    
- `substr(x, start, stop)` : start번째 문자부터 stop번째 문자까지 부분 문자열 출력
- `grep(pattern, x, ignore.case=F, fixed=F)` : pattern 문자열 요소가 있는지 검색
- `sub(pattern, replacement, x, ignore.case=F, fixed=F)` : pattern을 찾아 replacement로 대체
- `toupper(x)` : 대문자 변환
- `tolower(x)` : 소문자 변환

# 4. 결측치(Missing Values)

- `NA` : 데이터 결측치
- `is.na()` : 결측치의 포함 여부, 위치 확인
    
    ```r
    z <- c(11:13, NA)
    # 11 12 13 NA
    
    is.na(z)
    FALSE FALSE FALSE TRUE
    ```
    
- `na.omit()` : 결측치를 제외한 벡터 생성
    
    ```r
    na.omit(z)
    # 11 12 13
    ```
    
- `na.rm` 인수
    
    ```r
    sum(z)
    # NA
    
    sum(z, na.rm=TRUE)
    # 36
    ```
    
- `NaN` : 데이터의 값을 결정할 수 없는 경우
    
    ```r
    0/0
    # NaN
    
    Inf-Inf
    # NaN
    ```
    
- `is.nan()`
    
    ```r
    z <- -1:1 / 0
    # -Inf NaN Inf
    
    is.na(z)
    # FALSE TRUE FALSE
    
    r <- c(z, NA)
    is.na(r)
    # FALSE TRUE FALSE TRUE
    
    is.nan(r)
    # FALSE TRUE FALSE FALSE
    ```
    

# 5. 인덱스 벡터와 필터링

## 1. 자연수 인덱스 벡터

```r
x <- 11:20
x[6]
# 16

x[c(6, 10)]
# 16 20

x[seq(3, 9, by=2)]
# 13 15 17 19

x[rep(c(2,4), times=3)]
# 12 14 12 14 12 14

x <- c(7, 9, 4, 6, 13, 4, 1, 11)
x[which.min(x)]  # You can use min() instead.
# 1

x[which.max(x)] # You can use max() instead.
# 13

x[order(x)] # You can use sort() instead.
# 1 4 4 6 7 9 11 13
```

## 2. 음의 정수 인덱스 벡터

```r
x <- 11:20
# 11 12 13 14 15 16 17 18 19 20

x[-2]
# 11 13 14 15 16 17 18 19 20

x[c(-2, -4)]
# 11 13 15 16 17 18 19 20

x[-(3:6)]
# 11 12 17 18 19 20
```

## 3. 논리 인덱스 벡터

```r
x <- 1:5
y <- c(T, F, T, T, F)
x[y]
# 1 3 4

x>3 & x<5
# FALSE FALSE FALSE TRUE FALSE
x[x>3 & x<5]
# 4

y <- c(TRUE, FALSE)
x[y]
# 1 3 5
```

## 4. 이름 인덱스 벡터

```r
animals <- c(5, 7, 3, 2)
names(animals) <- c("cats", "dogs", "camels", "donkeys")
animals
# cats dogs camels donkeys 
#    5    7      3       2

animals["camels"]
# camels 
#      3
```

## 5. 인덱스 벡터를 이용해 벡터 요소에 값 할당하기
