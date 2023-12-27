# 05. R 리스트

# 1. 객체, 객체의 타입, 객체의 속성

- 객체(Objects) : 메모리에 저장하거나 메모리에서 읽어 올 수 있는 모든 데이터 단위
- 객체의 타입 : 원자적 벡터, 일반적 벡터
- 원자적 벡터(Atomic Vector) : 숫자 벡터, 논리 벡터, 문자 벡터처럼 하나의 데이터 형식으로 저장되는 데이터 타입
- `typeof()`
    
    ```r
    a <- c(T, F, F, T)
    typeof(a)
    # "logical"
    
    b <- 1:4
    typeof(b)
    # "integer"
    
    d <- c(1.5, 2.7, 3.3, 4.7)
    typeof(d)
    # "double"
    
    e <- c("car", "bus", "train", "plane")
    typeof(e)
    # "character"
    ```
    
- 데이터 자동 형변환
    
    ```r
    f <- c(a, b)
    typeof(f)
    # 1 0 0 1 1 2 3 4
    # "integer"
    
    g <- c(b, d)
    typeof(g)
    # 1.0 2.0 3.0 4.0 1.5 2.7 3.3 4.7
    # "double"
    
    h <- c(d, e)
    typeof(h)
    # "1.5" "2.7" "3.3" "4.7" "car" "bus" "train" "plane"
    # "character"
    
    g*2
    # 2.0 4.0 6.0 8.0 3.0 5.4 6.6 9.4
    
    h*2
    # Error in h * 2: 이항연산자에 수치가 아닌 인수입니다
    ```
    
- 내재적 속성
    
    ```r
    length(a)
    # 4
    
    length(a)
    # 4
    ```
    
- 행렬의 타입
    
    ```r
    aa <- matrix(a, nrow=2)
    typeof(aa)
    length(aa
    # "logical"
    # 4
    
    bb <- matrix(b, nrow=2)
    typeof(bb)
    length(bb)
    # "integer"
    # 4
    
    dd <- matrix(d, nrow=2)
    typeof(dd)
    length(dd)
    # "double"
    # 4
    
    ee <- matrix(e, nrow=2)
    typeof(ee)
    length(ee)
    # "character"
    # 4
    
    b
    # 1 2 3 4
    
    bb
    #      [,1] [,2]
    # [1,]    1    3
    # [2,]    2    4
    
    class(b)
    # "integer"
    
    class(bb)
    # "matrix" "array"
    ```
    
- 클래스 `class()` : 객체가 R함수에 의해 처리될 때 어떤 방식으로 처리되어야 하는지 알려줌
- `attributes()`
    
    ```r
    attributes(b)
    # NULL
    
    attributes(bb)
    # $dim
    # 2 2
    ```
    
- `attr()`
    
    ```r
    z <- 1:9
    # 1 2 3 4 5 6 7 8 9
    
    class(z)
    # "integer"
    
    attr(z, "dim")
    # NULL
    
    attr(z, "dim") <- c(3,3)
    attributes(z)
    # $dim
    # 3 3
    
    z
    #      [,1] [,2] [,3]
    # [1,]    1    4    7
    # [2,]    2    5    8
    # [3,]    3    6    9
    
    attr(z, "dimnames") <- list(c("A", "B", "C"), 1:3)
    attributes(z)
    # $dim
    # 3 3
    # $dimnames
    # $dimnames[[1]]
    # "A" "B" "C"
    # $dimnames[[2]]
    # "1" "2" "3"
    
    z
    #   1 2 3
    # A 1 4 7
    # B 2 5 8
    # C 3 6 9
    ```
    
- 객체 속성 함수 : 해당 속성을 위한 함수를 잘못 지정 → 오류 발생
- 모드와 타입의 차이
    - 모드 : R의 전신인 S언어에서 데이터의 기본 형식을 지정하기 위해 사용
    - 타입 : R에서 이용되는 개념
    
    ```r
    typeof(a)
    mode(a)
    # "logical"
    # "logical"
    
    typeof(b)
    mode(b)
    # "integer"
    # "numeric"
    
    typeof(d)
    mode(d)
    # "double"
    # "numeric"
    
    typeof(e)
    mode(e)
    # "character"
    # "character"
    
    storage.mode(b)
    # "integer"
    
    storage.mode(d)
    # "double"
    ```
    

# 2. 리스트의 생성 및 필터링

- `list()`
    
    ```r
    list(요소1, 요소2, ...)
    list(이름1=요소1, 이름2=요소2, ...)
    ```
    
    ```r
    a <- list(name="Fred", age=43, wife="Mary", no.children=3, child.ages=c(4, 7, 9), is.house.owner=T)
    # $name
    # "Fred"
    # $age
    # 43
    # $wife
    # "Mary"
    # $no.children
    # 3
    # $child.ages
    # 4 7 9
    # $is.house.owner
    # TRUE
    ```
    
- 리스트 객체의 타입, 길이, 속성 및 `names()`
    
    ```r
     typeof(a)
    # "list"
    
    length(a)
    # 6
    
    attributes(a)
    # $names
    # [1] "name" "age" "wife" "no.children"   
    # [5] "child.ages" "is.house.owner"
    
    names(a)
    # [1] "name" "age" "wife" "no.children"   
    # [5] "child.ages" "is.house.owner"
    
    a2 <- list(1:5, letters[1:8], LETTERS[1:3])
    # [[1]]
    # [1] 1 2 3 4 5
    # [[2]]
    # [1] "a" "b" "c" "d" "e" "f" "g" "h"
    # [[3]]
    # [1] "A" "B" "C"
    ```
    
- 리스트 요소의 이름 자동으로 부여되지 않음
    
    ```r
    var1 <- 1:3
    var2 <- 4:6
    cbind(var1, var2)
    #      var1 var2
    # [1,]    1    4
    # [2,]    2    5
    # [3,]    3    6
    
    data.frame(var1, var2)
    #   var1 var2
    # 1    1    4
    # 2    2    5
    # 3    3    6
    
    list(var1, var2)
    # [[1]]
    # [1] 1 2 3
    # [[2]]
    # [1] 4 5 6
    
    list(var1=var1, var2=var2)
    # $var1
    # [1] 1 2 3
    # $var2
    # [1] 4 5 6
    ```
    
- 리스트 요소 지정
    
    ```r
    a[[3]]
    # "Mary"
    
    a$wife
    # "Mary"
    
    a[["wife"]]
    # "Mary"
    ```
    
- 단계적으로 요소 지정
    
    ```r
    a[[5]]
    # 4 7 9
    
    a[[5]][2:3]
    # 7 9
    
    a$child.ages[2:3]
    # 7 9
    ```
    
- 요소 이름의 단축
    
    ```r
    a$no
    # 3
    
    a$child
    # 4 7 9
    ```
    
- 부분 리스트로 필터링
    
    ```r
    a[1:3]
    # $name
    # "Fred"
    # $age
    # 43
    # $wife
    # "Mary"
    
    a[c(2, 5)]
    # $age
    # 43
    # $child.ages
    # 4 7 9
    
    a[-(4:5)]
    # $name
    # "Fred"
    # $age
    # 43
    # $wife
    # "Mary"
    # $is.house.owner
    # TRUE
    
    a[c("wife", "child.ages")]
    # $wife
    # "Mary"
    # $child.ages
    # 4 7 9
    
    a[c(T, F, F)]
    # $name
    # "Fred"
    # $no.children
    # 3
    ```
    
- 리스트 요소 지정 vs 부분 리스트 필터링
    
    ```r
    a[[5]]
    # 4 7 9
    
    a[5]
    # $child.ages
    # 4 7 9
    
    a[[5]][2:3]
    # 7 9
    
    a[[5]]*7
    # 28 49 63
    
    a[5][2:3]
    # $<NA>
    # NULL
    # $<NA>
    # NULL
    
    a[5]*7
    # Error in a[5] * 7: 이항연산자에 수치가 아닌 인수입니다
    ```
