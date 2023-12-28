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
    

# 3. 리스트의 변경 및 연결

- 리스트 요소의 추가
    
    ```r
    length(a)
    # 6
    
    a[[7]] <- 1:5
    a[["address"]] <- "Cheonan"
    a$years.since.marrage <- 15
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
    # [[7]]
    # 1 2 3 4 5
    # $address
    # "Cheonan"
    # $years.since.marrage
    # 15
    ```
    
- 리스트 요소의 변경
    
    ```r
    a[[7]] <- 10:18
    a$address <- "Daejeon"
    a[[9]] <- 16
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
    # [[7]]
    # 10 11 12 13 14 15 16 17 18
    # $address
    # "Daejeon"
    # $years.since.marrage
    # 16
    ```
    
- 자연수 인덱스를 이용한 리스트 요소의 추가와 빈 요소의 생성
    
    ```r
    a2
    # [[1]]
    # [1] 1 2 3 4 5
    # [[2]]
    # [1] "a" "b" "c" "d" "e" "f" "g" "h"
    # [[3]]
    # [1] "A" "B" "C"
    
    a2[[5]] <- "New items"
    # [[1]]
    # [1] 1 2 3 4 5
    # [[2]]
    # [1] "a" "b" "c" "d" "e" "f" "g" "h"
    # [[3]]
    # [1] "A" "B" "C"
    # [[4]]
    # NULL
    # [[5]]
    # [1] "New items
    ```
    
- 리스트 요소의 삭제
    
    ```r
    a2[[5]] <- NULL
    # [[1]]
    # [1] 1 2 3 4 5
    # [[2]]
    # [1] "a" "b" "c" "d" "e" "f" "g" "h"
    # [[3]]
    # [1] "A" "B" "C"
    # [[4]]
    # NULL
    
    a2[[4]] <- NULL
    # [[1]]
    # [1] 1 2 3 4 5
    # [[2]]
    # [1] "a" "b" "c" "d" "e" "f" "g" "h"
    # [[3]]
    # [1] "A" "B" "C"
    
    names(a2) <- c("num", "lower.case", "upper.case")
    # $num
    # 1 2 3 4 5
    # $lower.case
    # "a" "b" "c" "d" "e" "f" "g" "h"
    # $upper.case
    # "A" "B" "C"
    
    a2$num <- NULL
    # $lower.case
    # "a" "b" "c" "d" "e" "f" "g" "h"
    # $upper.case
    # "A" "B" "C"
    ```
    
- 부분 리스트를 이용한 리스트 변경
    
    ```r
    a2[3:4] <- list(1:5, month.name)
    # $lower.case
    # "a" "b" "c" "d" "e" "f" "g" "h"
    # $upper.case
    # "A" "B" "C"
    # [[3]]
    # [1] 1 2 3 4 5
    # [[4]]
    # [1] "January" "February" "March" "April" "May" "June"     
    # [7] "July" "August" "September" "October" "November" "December"
    ```
    
- 리스트의 Recycling
    
    ```r
    a2[3:6] <- list(11:15, month.abb)
    # $lower.case
    # "a" "b" "c" "d" "e" "f" "g" "h"
    # $upper.case
    # "A" "B" "C"
    # [[3]]
    # [1] 11 12 13 14 15
    # [[4]]
    # [1] "Jan" "Feb" "Mar" "Apr" "May" "Jun" "Jul" "Aug" "Sep" "Oct" "Nov" "Dec"
    # [[5]]
    # [1] 11 12 13 14 15
    # [[6]]
    # [1] "Jan" "Feb" "Mar" "Apr" "May" "Jun" "Jul" "Aug" "Sep" "Oct" "Nov" "Dec"
    ```
    
- 벡터 리스트로의 형변환
    
    ```r
    a2[3:6] <- c("X", "Y", "Z", "W")
    # $lower.case
    # "a" "b" "c" "d" "e" "f" "g" "h"
    # $upper.case
    # "A" "B" "C"
    # [[3]]
    # [1] "X"
    # [[4]]
    # [1] "Y"
    # [[5]]
    # [1] "Z"
    # [[6]]
    # [1] "W"
    
    c("X", "Y", "Z", "W")
    # "X" "Y" "Z" "W"
    
    as.list(c("X", "Y", "Z", "W"))
    # [[1]]
    # [1] "X"
    # [[2]]
    # [1] "Y"
    # [[3]]
    # [1] "Z"
    # [[4]]
    # [1] "W"
    
    a2[3:6] <- NULL
    # $lower.case
    # "a" "b" "c" "d" "e" "f" "g" "h"
    # $upper.case
    # "A" "B" "C"
    ```
    
- `c()` 를 이용한 리스트 연결하기
    
    ```r
    a3 <- list(first=1:3, second=4:6)
    # $first
    # 1 2 3
    # $second
    # 4 5 6
    
    a4 <- c(a2, a3)
    # $lower.case
    # "a" "b" "c" "d" "e" "f" "g" "h"
    # $upper.case
    # "A" "B" "C"
    # $first
    # 1 2 3
    # $second
    # 4 5 6
    
    length(a4)
    # 4
    ```
    
- 계층적인 리스트 만들기
    
    ```r
    a5 <- list(a2, a3)
    # [[1]]
    # [[1]]$lower.case
    # [1] "a" "b" "c" "d" "e" "f" "g" "h"
    # [[1]]$upper.case
    # [1] "A" "B" "C"
    # [[2]]
    # [[2]]$first
    # [1] 1 2 3
    # [[2]]$second
    # [1] 4 5 6
    
    length(a5)
    # 2
    
    a4[[2]]
    # "A" "B" "C"
    
    a5[[2]]
    # $first
    # 1 2 3
    # $second
    # 4 5 6
    
    a5[[1]][[2]]
    # "A" "B" "C"
    
    a5[[2]]$second
    # 4 5 6
    
    a4$second
    # 4 5 6
    
    c(a4, a5)
    # $lower.case
    # "a" "b" "c" "d" "e" "f" "g" "h"
    # $upper.case
    # "A" "B" "C"
    # $first
    # [1] 1 2 3
    # $second
    # [1] 4 5 6
    # [[5]]
    # [[5]]$lower.case
    # [1] "a" "b" "c" "d" "e" "f" "g" "h"
    # [[5]]$upper.case
    # [1] "A" "B" "C"
    # [[6]]
    # [[6]]$first
    # [1] 1 2 3
    # [[6]]$second
    # [1] 4 5 6
    
    c(a4, a5, recursive = TRUE)
    # lower.case1 lower.case2 lower.case3 lower.case4 lower.case5 lower.case6 
    #         "a"         "b"         "c"         "d"         "e"         "f" 
    # lower.case7 lower.case8 upper.case1 upper.case2 upper.case3      first1 
    #         "g"         "h"         "A"         "B"         "C"         "1" 
    #      first2      first3     second1     second2     second3 lower.case1 
    #         "2"         "3"         "4"         "5"         "6"         "a" 
    # lower.case2 lower.case3 lower.case4 lower.case5 lower.case6 lower.case7 
    #         "b"         "c"         "d"         "e"         "f"         "g" 
    # lower.case8 upper.case1 upper.case2 upper.case3      first1      first2 
    #         "h"         "A"         "B"         "C"         "1"         "2" 
    #      first3     second1     second2     second3 
    #         "3"         "4"         "5"         "6"
    ```
    
- `unlist()` 로 리스트를 벡터로 형 변환하기
    
    ```r
    unlist(a3)
    # first1  first2  first3 second1 second2 second3 
    #      1       2       3       4       5       6
    
    unlist(a4)
    # lower.case1 lower.case2 lower.case3 lower.case4 lower.case5 lower.case6 
    #         "a"         "b"         "c"         "d"         "e"         "f" 
    # lower.case7 lower.case8 upper.case1 upper.case2 upper.case3      first1 
    #         "g"         "h"         "A"         "B"         "C"         "1" 
    #      first2      first3     second1     second2     second3 
    #         "2"         "3"         "4"         "5"         "6"
    
    a <- c("R은 통계분석을 위해 특화된 프로그램 언어입니다.", "다양한 데이터 분석 함수가 내장되어 있습니다.")
    b <- strsplit(a, split = " ")
    # [[1]]
    # [1] "R은" "통계분석을" "위해" "특화된" "프로그램"   
    # [6] "언어입니다."
    # [[2]]
    # [1] "다양한" "데이터" "분석" "함수가" "내장되어" "있습니다."
    
    unlist(b)
    # [1] "R은" "통계분석을" "위해" "특화된" "프로그램"   
    # [6] "언어입니다." "다양한" "데이터" "분석" "함수가"     
    # [11] "내장되어" "있습니다."
    ```
    

# 4. 리스트에 함수 적용하기

## 1. `lapply()` 함수

- `lapply()` : 각 요소 함수 적용 → 리스트 객체로 결과 제공
    
    ```r
    lapply(리스트, 함수)
    ```
    
    ```r
    b <- list(1:5, 21:29, seq(2, 20, by=2))
    # [[1]]
    # [1] 1 2 3 4 5
    # [[2]]
    # [1] 21 22 23 24 25 26 27 28 29
    # [[3]]
    # [1] 2 4 6 8 10 12 14 16 18 20
    
    mean(b[[1]])
    # 3
    
    mean(b[[2]])
    # 25
    
    mean(b[[3]])
    # 11
    
    lapply(b, mean)
    # [[1]]
    # [1] 3
    # [[2]]
    # [1] 25
    # [[3]]
    # [1] 11
    ```
    
- `lapply()` 결과 리스트의 요소 이름
    
    ```r
    lapply(b, max)
    # [[1]]
    # [1] 5
    # [[2]]
    # [1] 29
    # [[3]]
    # [1] 20
    
    names(b) <- c("A", "B", "C")
    lapply(b, range)
    # $A
    # 1 5
    # $B
    # 21 29
    # $C
    # 2 20
    ```
    

## 2. `sapply()` 함수

- `sapply()` : 최종 결과 벡터나 행렬로 제공
    
    ```r
    sapply(b, length)
    # A B C 
    # 5 9 10
    
    sapply(b, range)
    #      A  B  C
    # [1,] 1 21  2
    # [2,] 5 29 20
    
    lb <- lapply(b, length)
    typeof(lb)
    # "list"
    
    sb <- sapply(b, length)
    typeof(sb)
    # "integer"
    ```
    
- 사용자 정의 함수의 적용
    
    ```r
    sapply(b, function(x){
      sum(x > 10)
    })
    # A B C 
    # 0 9 5
    ```
    

## 3. `mapply()` 함수

- 다수의 리스트에 대해 같은 위치의 요소들에 함수 적용
- 벡터나 행렬 등의 단순한 형태 제공 가능 → 단순한 형태로 결과 제공
    
    ```r
    mapply(FUN, list_1(vector_1), ..., list_n(vector_n), MoreArgs=NULL)
    ```
    
    ```r
    a <- list(1:5, 10:5, letters[1:4])
    b <- list(6:4, 4:7, LETTERS[5:1])
    
    mapply(c, a, b)
    # [[1]]
    # [1] 1 2 3 4 5 6 5 4
    # [[2]]
    # [1] 10 9 8 7 6 5 4 5 6 7
    # [[3]]
    # [1] "a" "b" "c" "d" "E" "D" "C" "B" "A"
    
    mapply(rep, times=2:4, x=list(1:2, 11:12, 21:22))
    # [[1]]
    # [1] 1 2 1 2
    # [[2]]
    # [1] 11 12 11 12 11 12
    # [[3]]
    # [1] 21 22 21 22 21 22 21 22
    ```
    

# 5. 리스트 활용 분야

- 리스트로 결과를 반환하는 함수의 예
    
    ```r
    x <- lm(dist~speed, data=cars)
    # Call:
    # lm(formula = dist ~ speed, data = cars)
    # Coefficients:
    # (Intercept)        speed  
    #     -17.579        3.932
    
    typeof(x)
    # "list"
    
    class(x)
    # "lm"
    
    names(x)
    # [1] "coefficients" "residuals" "effects" "rank"
    # [5] "fitted.values" "assign" "qr" "df.residual"
    # [9] "xlevels" "call" "terms" "model"
    
    x$residuals
    #          1          2          3          4          5          6          7 
    #   3.849460  11.849460  -5.947766  12.052234   2.119825  -7.812584  -3.744993 
    #          8          9         10         11         12         13         14 
    #   4.255007  12.255007  -8.677401   2.322599 -15.609810  -9.609810  -5.609810 
    #         15         16         17         18         19         20         21 
    #  -1.609810  -7.542219   0.457781   0.457781  12.457781 -11.474628  -1.474628 
    #         22         23         24         25         26         27         28 
    #  22.525372  42.525372 -21.407036 -15.407036  12.592964 -13.339445  -5.339445 
    #         29         30         31         32         33         34         35 
    # -17.271854  -9.271854   0.728146 -11.204263   2.795737  22.795737  30.795737 
    #         36         37         38         39         40         41         42 
    # -21.136672 -11.136672  10.863328 -29.069080 -13.069080  -9.069080  -5.069080 
    #         43         44         45         46         47         48         49 
    #   2.930920  -2.933898 -18.866307  -6.798715  15.201285  16.201285  43.201285 
    #         50 
    #   4.268876
    
    x$terms
    # dist ~ speed
    # attr(,"variables")
    # list(dist, speed)
    # attr(,"factors")
    #       speed
    # dist      0
    # speed     1
    # attr(,"term.labels")
    # "speed"
    # attr(,"order")
    # 1
    # attr(,"intercept")
    # 1
    # attr(,"response")
    # 1
    # attr(,".Environment")
    # <environment: R_GlobalEnv>
    # attr(,"predvars")
    # list(dist, speed)
    # attr(,"dataClasses")
    #      dist     speed 
    # "numeric" "numeric"
    ```
    
- `unclass()` : 객체에 부여된 클래스 속성 제거 → 단순 리스트 객체 변환
- 데이터 프레임
    
    ```r
    head(cars)
    #   speed dist
    # 1     4    2
    # 2     4   10
    # 3     7    4
    # 4     7   22
    # 5     8   16
    # 6     9   10
    
    typeof(cars)
    # "list"
    
    class(cars)
    # "data.frame"
    
    unclass(cars)
    # $speed
    # [1] 4 4 7 7 8 9 10 10 10 11 11 12 12 12 12 13 13 13 13 14 14 14 14 15 15
    # [26] 15 16 16 17 17 17 18 18 18 18 19 19 19 20 20 20 20 20 22 23 24 24 24 24 25
    # $dist
    # [1] 2 10 4 22 16 10 18 26 34 17 28 14 20 24 28 26 34 34 46
    # [20] 26 36 60 80 20 26 54 32 40 32 40 50 42 56 76 84 36 46 68
    # [39] 32 48 52 56 64 66 54 70 92 93 120 85
    # attr(,"row.names")
    # [1] 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
    # [26] 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
    
    y <- list(a=11:15, b=letters[11:15])
    # $a
    # 11 12 13 14 15
    # $b
    # "k" "l" "m" "n" "o"
    
    typeof(y)
    class(y)
    # "list"
    # "list"
    
    z <- as.data.frame(y)
    #    a b
    # 1 11 k
    # 2 12 l
    # 3 13 m
    # 4 14 n
    # 5 15 o
    
    typeof(z)
    class(z)
    # "list"
    # "data.frame"
    ```
