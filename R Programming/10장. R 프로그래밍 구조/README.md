# 10. R 프로그래밍 구조

# 1. R 조건문

## 1. `if` 조건문

- `if-else` 조건문
    
    ```r
    if (statement1) statement2 else statement3
    ```
    
    ```r
    x <- 4
    if( x >= 4 ) y <- 1 else y <- -1
    y
    # 1
    
    x <- sample(1:6, size=1)
    if( x >= 4 ) y <- 1 else y <- -1
    x
    # 1
    y
    # -1
    
    x <- sample(1:6, size=1)
    if (x >= 4) {
      y <- 1
      cat("손님이 이겼습니다.\n")
    } else {
      y <- -1
      cat("딜러가 이겼습니다.\n")
    }
    cat("주사위 눈금:", x, "\n")
    cat("손익:", y, "\n")
    # 손님이 이겼습니다.
    # 주사위 눈금: 6 
    # 손익: 1
    ```
    
- 단순 `if` 조건문
    
    ```r
    if (statement1) statement2
    ```
    
    ```r
    n <- 0
    x <- sample(1:6, size=1)
    if (x >= 4) n <- n + 1
    cat("x:", x, ", n:", n, "\n")
    # x: 5 , n: 1
    
    x <- sample(1:6, size=1)
    if (x >= 4) n <- n + 1
    cat("x:", x, ", n:", n, "\n")
    # x: 2 , n: 1
    
    x <- sample(1:6, size=1)
    if (x >= 4) n <- n + 1
    cat("x:", x, ", n:", n, "\n")
    # x: 4 , n: 2
    ```
    
- 복합 조건문
    
    ```r
    if (statement1) {
      statement2 
    } else if (statement3.1) {
      statement3.2
    } else {
      statement3.3
    }
    ```
    
    ```r
    x <- sample(1:6, size=1)
    if (x>=5) {
      cat("손님이 이겼습니다.\n")
      y <- 1
    } else if ( x >=3 ) {
      cat("무승부입니다.\n")
      y <- 0
    } else {
      cat("딜러가 이겼습니다.\n")
      y <- -1
    }
    cat("주사위 눈금:", x, "\n")
    cat("손익:", y, "\n")
    # 무승부입니다.
    # 주사위 눈금: 4 
    # 손익: 0
    ```
    
- 중첩 조건문
    
    ```r
    if (statement1) {
      ...
      if (statement2.1) {
        statement2.2
      } else {
        statement2.3
      }
      ...
    } else {
      ...
      if (statement3.1) {
        statement3.2
      } else {
        statement3.3
      }
      ...
    }
    ```
    
    ```r
    x <- sample(-10:10, size=1)
    if (x>0) {
      cat(x, "은(는) 양수이고 ")
      if (x %% 2 == 0) cat("짝수입니다.\n") else cat("홀수입니다.\n")
    } else {
      cat(x, "은(는) 0 또는 음수이고 ")
      if (x %% 3 == 0) cat("3의 배수입니다.\n") else cat("3의 배수가 아닙니다.\n")
    }
    # -3 은(는) 0 또는 음수이고 3의 배수입니다.
    ```
    
- 조건문의 결과가 두 개 이상의 논리값을 주는 경우
    
    ```r
    x <- c(5, 0, -5)
    x > 0
    # TRUE FALSE FALSE
    
    if (x > 0) y <- 1 else y <- 0
    # Error in if (x > 0) y <- 1 else y <- 0: the condition has length > 1
    
    y
    # 0
    
    if (x[3] > 0) y <- 1 else y <- 0
    y
    # 0
    ```
    
- 복합 조건
    
    ```r
    x <- 3
    y <- -4
    if ( x >= 0 ) {
      if ( y >= 0 ) {
        print(x + y)
      } else {
        warning("x와 y는 모두 0 이상이어야 합니다.")
      }
    } else {
      warning("x와 y는 모두 0 이상이어야 합니다.")
    }
    # Warning: x와 y는 모두 0 이상이어야 합니다.
    
    if ( x >= 0 && y >= 0 ) {
      print(x + y)
    } else {
      warning("x와 y는 모두 0 이상이어야 합니다.")
    }
    # Warning: x와 y는 모두 0 이상이어야 합니다.
    
    a <- c(T, F)
    b <- c(T, T)
    a & b
    # TRUE FALSE
    
    a && b
    # Error in a && b: 'length = 2' in coercion to 'logical(1)'
    
    if (a & b) print("TRUE") else print("FALSE") # 오류 발생
    # Error in if (a & b) print("TRUE") else print("FALSE"): the condition has length > 1
    
    if (a && b) print("TRUE") else print("FALSE") # 경고 발생
    # Error in a && b: 'length = 2' in coercion to 'logical(1)'
    
    if (a[1] && b[1]) print("TRUE") else print("FALSE")
    # "TRUE"
    
    a | b
    # TRUE TRUE
    
    a || b
    # Error in a || b: 'length = 2' in coercion to 'logical(1)'
    
    if (a & b) print("TRUE") else print("FALSE") # 오류 발생
    # Error in if (a & b) print("TRUE") else print("FALSE"): the condition has length > 1
    
    if (a && b) print("TRUE") else print("FALSE") # 경고 발생
    # Error in a && b: 'length = 2' in coercion to 'logical(1)'
    
    if (a[1] && b[1]) print("TRUE") else print("FALSE")
    # "TRUE"
    
    if ( x >= 0 || y >= 0 ) {
      print(x + y)
    } else {
      warning("x와 y 중 하나는 0 이상이어야 합니다.")
    }
    # -1
    ```
    
- `if-else` 조건문은 `ifelse()` 함수와는 다름
    
    ```r
    e <- c(5, -4, 3)
    ifelse(e >=0, e, -e)
    # 5 4 3
    ```
    

## 2. `switch` 함수

```r
switch(EXPR, expression_1, ..., expression_n)
```

```r
i <- 2
switch(i, 10, 1:5, pi)
# 1 2 3 4 5

i <- 3
switch(i, 10, 1:5, pi)
# 3.141593

i <- 4
switch(i, 10, 1:5, pi)
```

```r
switch(EXPR, name_1=expression_1, ..., 
       name_n=expression_n, expression_default)
```

```r
menu <- c("(b)anana", "(o)range", "(s)trawberry")
repeat{
  price <- 0
  cat("\n다음 중 메뉴를 골라주세요:", paste(1:3, menu, sep="."), "\n")
  choice <- readline("메뉴 선택 [b|o|s] 또는 종료 [q]: ")
  switch(choice, 
         b = {cat("바나나가 나왔습니다.\n"); price <- 1000},  
         o = {cat("오렌지가 나왔습니다.\n"); price <- 1200}, 
         s = {cat("딸기가 나왔습니다.\n"); price <- 1500},
         q = break,
         cat("번호를 잘못 눌렀습니다.\n"))
  cat("이번 거래는 총",  price, "원 입니다.\n")
}
```

# 2. R 반복문

## 1. `for` 반복문

- 벡터 또는 리스트의 각 요소별로 반복하기
    
    ```r
    for ( variable in vector ) statement
    for ( variable in list ) statement
    ```
    
    ```r
    n <- 1:5
    s <- 0
    for (x in n) s <- s + x
    # 15
    
    s <- 0
    for (x in n) {
      cat("반복 시작: x =", x, ", s =", s, "\n")
      s <- s + x
      cat("반복 끝  : x =", x, ", s =", s, "\n\n")
    }
    # 반복 시작: x = 1 , s = 0
    # 반복 끝  : x = 1 , s = 1
    # 
    # 반복 시작: x = 2 , s = 1
    # 반복 끝  : x = 2 , s = 3
    # 
    # 반복 시작: x = 3 , s = 3
    # 반복 끝  : x = 3 , s = 6
    # 
    # 반복 시작: x = 4 , s = 6
    # 반복 끝  : x = 4 , s = 10
    # 
    # 반복 시작: x = 5 , s = 10
    # 반복 끝  : x = 5 , s = 15
    
    total <- 0
    x_vec <- sample(1:6, size=5, replace = T) 
    x_vec
    # 3 4 2 5 2
    
    for( x in x_vec) {
      if (x>=5) {
        cat("손님이 이겼습니다.\n")
        y <- 1
      } else if ( x >=3 ) {
        cat("무승부입니다.\n")
        y <- 0
      } else {
        cat("딜러가 이겼습니다.\n")
        y <- -1
      }
      cat("주사위 눈금:", x, "\n")
      cat("이번 게임 손익:", y, "\n")
      
      total <- total + y
      cat("지금까지의 총 손익:", total, "\n\n")
    }
    # 무승부입니다.
    # 주사위 눈금: 3
    # 이번 게임 손익: 0 
    # 지금까지의 총 손익: 0 
    # 
    # 무승부입니다.
    # 주사위 눈금: 4 
    # 이번 게임 손익: 0 
    # 지금까지의 총 손익: 0 
    # 
    # 딜러가 이겼습니다.
    # 주사위 눈금: 2 
    # 이번 게임 손익: -1 
    # 지금까지의 총 손익: -1 
    
    # 손님이 이겼습니다.
    # 주사위 눈금: 5 
    # 이번 게임 손익: 1 
    # 지금까지의 총 손익: 0 
    # 
    # 딜러가 이겼습니다.
    # 주사위 눈금: 2 
    # 이번 게임 손익: -1 
    # 지금까지의 총 손익: -1
    ```
    
- 벡터의 인덱스를 이용하여 벡터 요소 반복하기
    
    ```r
    total <- 0
    x_vec <- sample(1:6, size=5, replace = T) 
    x_vec
    # 5 4 5 5 5
    
    for( idx in 1:length(x_vec) ) {
      cat(idx, "번째 게임입니다.\n")
      x <- x_vec[idx]
      if (x>=5) {
        cat("손님이 이겼습니다.\n")
        y <- 1
      } else if ( x >=3 ) {
        cat("무승부입니다.\n")
        y <- 0
      } else {
        cat("딜러가 이겼습니다.\n")
        y <- -1
      }
      cat("주사위 눈금:", x, "\n")
      cat("이번 게임 손익:", y, "\n")
      
      total <- total + y
      cat("지금까지의 총 손익:", total, "\n\n")
    }
    # 1 번째 게임입니다.
    # 손님이 이겼습니다.
    # 주사위 눈금: 5 
    # 이번 게임 손익: 1 
    # 지금까지의 총 손익: 1 
    # 
    # 2 번째 게임입니다.
    # 무승부입니다.
    # 주사위 눈금: 4 
    # 이번 게임 손익: 0 
    # 지금까지의 총 손익: 1 
    # 
    # 3 번째 게임입니다.
    # 손님이 이겼습니다.
    # 주사위 눈금: 5 
    # 이번 게임 손익: 1 
    # 지금까지의 총 손익: 2 
    # 
    # 4 번째 게임입니다.
    # 손님이 이겼습니다.
    # 주사위 눈금: 5 
    # 이번 게임 손익: 1 
    # 지금까지의 총 손익: 3 
    # 
    # 5 번째 게임입니다.
    # 손님이 이겼습니다.
    # 주사위 눈금: 5 
    # 이번 게임 손익: 1 
    # 지금까지의 총 손익: 4
    
    x <- rep(c(1, -1), each=2)
    y <- rep(c(1, -1), times=2)
    x
    # 1 1 -1 -1
    y
    # 1 -1 1 -1
    
    for ( i in seq(along=x)) {
      cat(x[i], "+", y[i], "= ")
      if ( x[i] >= 0 || y[i] >= 0 ) {
        cat(x[i] + y[i], "입니다\n")
      } else {
        warning("x와 y 중 하나는 0 이상이어야 합니다.")
      } 
    }
    # 1 + 1 = 2 입니다
    # 1 + -1 = 0 입니다
    # -1 + 1 = 0 입니다
    # -1 + -1 = 
    # Warning: x와 y 중 하나는 0 이상이어야 합니다.
    ```
    

## 2. `while` 반복문

- 조건에 따라 반복하기
    
    ```r
    while (statement1) statement2
    ```
    
    ```r
    s <- 0
    x <- 1
    while ( x <= 5 ) {
      s <- s + x
      x <- x + 1
    }
    s
    # 15
    ```
    
- 무한 반복이 발생하는 경우 : `statement2` 에서 `statement1` 이 FALSE가 되도록 하는 부분이 없음
- 사용자의 입력에 따라 반복할지 결정하기
    
    ```r
    num <- "1"
    while ( num != "0") {
      n <- as.integer(num)
      hist(iris[[n]], main = names(iris)[n])
      
      cat("히스토그램을 출력할 열을 선택하세요[1-4]. 종료를 원하면 0을 입력")
      num <- readline()
    }
    ```
    

## 3. `repeat` 반복문

```r
repeat statement
```

- `repeat` 문의 무한 반복은 `break` 문으로 빠져나옴
    
    ```r
    repeat {
      cat("히스토그램을 출력할 열을 선택하세요[1-4]. 종료를 원하면 0을 입력")
      num <- readline()
      if (num == "0") {
        cat("Bye~~!")
        break
      }
      n <- as.integer(num)
      hist(iris[[n]], main = names(iris)[n])
    }
    ```
    

## 4. 반복문의 제어 명령

```r
x <- c(5, 4, 8, 9, 10, 11)
s <- 0
for (a in x) {
  if( a %% 2 == 0) next
  cat(a, s, "\n")
  s <- s + a
}
# 5 0 
# 9 5 
# 11 14

s
# 25
```

## 5. R에서 반복문 사용의 주의점

- 명시적 반복문은 되도록 피하기
- 벡터화된 내장 함수로 암시적인 반복 수행
    
    ```r
    set.seed(123)
    n <- 1000000
    x <- rnorm(n)
    y <- rnorm(n)
    system.time(sum(ifelse(x > y, x, y)))
    # 사용자  시스템 elapsed 
    # 0.027   0.012   0.039
    
    s <- 0
    system.time({
      for (i in 1:n){
        if (x[i] > y[i]) s <- s + x[i] else s <- s + y[i]
      }
    })
    # 사용자  시스템 elapsed 
    # 0.075   0.000   0.074
    
    set.seed(111)
    n <- 1000000
    x <- sample(-1000:1000, n, replace=T)
    
    system.time({
      sum( x[x %% 3 == 0] ) 
    })
    # 사용자  시스템 elapsed 
    # 0.028   0.000   0.027
    
    system.time({
      s <- 0
      for (a in x) {
        if (a %% 3 == 0)
        s <- s + a
      }
      print(s)
    })
    # 198993
    # 사용자  시스템 elapsed 
    # 0.177   0.000   0.177
    ```
    
- `apply` 계열 함수로 암시적인 반복 수행
    
    ```r
    set.seed(11)
    n <- 100000
    x <- lapply(1:100, function(i) sample(-1000:1000, n, replace=T))
    
    system.time( {
      s <- sapply(x, function(y) sum(y[y %% 3 == 0]))
      print(max(s))
    })
    # 285816
    # 사용자  시스템 elapsed 
    # 0.250   0.000   0.249
    
    system.time({
      s.max <- -Inf
      for(i in 1:length(x)) {
        s <- sum(x[[i]][x[[i]] %% 3 == 0])
        if(s > s.max) s.max <- s
      }
      print(s.max)
    })
    # 285816
    # 사용자  시스템 elapsed 
    # 0.246   0.004   0.251
    ```
    

# 3. R 함수

- 함수의 필요성
    
    ```r
    typeof(sum)
    # "builtin"
    
    typeof(mean)
    # "closure"
    
    typeof(summary)
    # "closure"
    
    typeof(plot)
    # "closure"
    ```
    

## 1. 함수의 생성과 호출

- 함수 정의하기
    
    ```r
    function_name <- function(formal_arg1, formal_arg2, ...) 
              function_body_expression
    ```
    
    ```r
    g <- function(x, y, z) 100 * x + 10 * y + z
    ```
    
- 함수도 객체임
    
    ```r
    g
    function(x, y, z) 100 * x + 10 * y + z
    ```
    
- 함수 호출하기
    
    ```r
    function_name(actual_arg1, actual_arg2, ...)
    function_name(formal_arg1=actual_arg1, formal_arg2=actual_arg2, ...)
    ```
    
- 형식 인수를 지정하지 않고 호출하기
    
    ```r
    g(1, 2, 0)
    # 120
    
    g(2, 1, 0)
    # 210
    
    g(0, 7, 1)
    # 71
    ```
    
- 벡터화된 함수
    
    ```r
    g(1:3, 1, c(2, 4, 6))
    # 112 214 316
    ```
    
- 형식 인수를 지정하여 함수 호출 하기
    
    ```r
    g(y=2, x=1, z=0)
    # 120
    
    g(z=0, x=1, y=2)
    # 120
    
    g(1, 2, x=3)
    # 312
    
    g(x=1, 2, y=0)
    # 102
    ```
    
- 형식 인수 수와 실질 인수의 수가 다르면 오류 발생
    
    ```r
    g(1, x=2)
    # Error in g(1, x = 2): 기본값이 없는 인수 "z"가 누락되어 있습니다
    
    g(1, 2, 3, 4)
    # Error in g(1, 2, 3, 4): 사용되지 않은 인자 (4)
    ```
    
- 형식 인수의 초기값 설정하기
    
    ```r
    oddsum <- function(b) sum(seq(from=1, to=b, by=2))
    oddsum(5)
    # 9
    
    oddsum(10)
    # 25
    
    oddsum()
    # Error in oddsum(): 기본값이 없는 인수 "b"가 누락되어 있습니다
    
    oddsum <- function(b=100) sum( seq(from=1, to=b, by=2) )
    oddsum()
    # 2500
    
    oddsum(3)
    # 4
    
    oddsum <- function(b=100, a=1) sum(seq(from=a, to=b, by=2))
    oddsum(a=5, b=10)
    # 21
    
    oddsum(3)
    # 4
    
    oddsum(a=97)
    # 196
    ```
    
- R 기본 함수에서의 초기값 사용
    
    ```r
    seq()
    # 1
    
    seq(by=2)
    # 1
    
    seq(1, 5, 2)
    # 1 3 5
    
    seq(to=4)
    # 1 2 3 4
    
    seq(to=-5)
    # 1 0 -1 -2 -3 -4 -5
    
    seq(to=10, by=2)
    # 1 3 5 7 9
    
    read.csv
    function (file, header = TRUE, sep = ",", quote = "\"", dec = ".", 
        fill = TRUE, comment.char = "", ...) 
    read.table(file = file, header = header, sep = sep, quote = quote, 
        dec = dec, fill = fill, comment.char = comment.char, ...)
    # <bytecode: 0x55b10dd0c920>
    # <environment: namespace:utils>
    ```
    
- `...` 형식 인수
    
    ```r
    g(x=1, y=1, z=1, w=1)
    # Error in g(x = 1, y = 1, z = 1, w = 1): 사용되지 않은 인자 (w = 1)
    
    g <- function(x, y, z, ...) 100 * x + 10 * y + z 
    g(x=1, y=1, z=1, w=1, r=2)
    # 111
    
    g <- function(x, y, z, ...) {
      cat(..., sep=",")
      cat("를 추가적으로 입력받았습니다.\n")
      100 * x + 10 * y + z + sum(...)
    }
    g(x=1, y=1, z=1, w=1, r=2)
    # 1,2를 추가적으로 입력받았습니다.
    # 114
    
    c
    # function (...)  .Primitive("c")
    
    c(1:2, c(3, 6), 7:2)
    # 1 2 3 6 7 6 5 4 3 2
    
    sum
    # function (..., na.rm = FALSE)  .Primitive("sum")
    
    sum(1:2, c(3, 6), 7:2)
    # 39
    ```
    
    ```r
    x <- 1:30
    y <- x^2
    plot(x, y)
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/81077628-f0b8-4c1d-a146-157cf2bee76a/Untitled.png)
    
    ```r
    plot
    # function (x, y, ...) 
    # UseMethod("plot")
    # <bytecode: 0x55b10d88dbd0>
    # <environment: namespace:base>
    plot(x, y, type="o", col="red", pch="*", lty=1, lwd=1.5)
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/e70b85c8-f58b-4988-9d2f-4d535ab7a30f/Untitled.png)
    
- 함수의 반환값
    
    ```r
    calPrice <- function(quantity) {
      if (quantity < 500) {
        unitPrice <- 100
      } else {
        unitPrice <- 80
      }
      unitPrice * quantity
    }
    
    calPrice(100)
    # 10000
    
    calPrice(1000)
    # 80000
    
    h <- function(x) {
      if (x < 0) {
        cat("x must be positive.\n")
        return(NULL)
      }
      sqrt(x)
    }
    
    h(2)
    # 1.414214
    
    h(-2)
    # x must be positive.
    # NULL
    
    calPrice2 <- function(quantity) {
      if (quantity < 500) {
        unitPrice <- 100
      } else {
        unitPrice <- 80
      }
      return(unitPrice * quantity)
    }
    
    calPrice2(100)
    # 10000
    
    calPrice2(1000)
    # 80000
    ```
    

## 2. 함수 객체를 인수로 사용하기

- 함수도 객체이므로 실질 인수가 될 수 있음
    
    ```r
    a <- list(x=x, y=y, z=sqrt(x))
    sapply(a, mean)
    #          x          y          z 
    #  15.500000 315.166667   3.736095
    
    mean
    # function (x, ...) 
    # UseMethod("mean")
    # <bytecode: 0x55b10aad8168>
    # <environment: namespace:base>
    ```
    
- `apply` 계열 함수에 사용자 함수 적용하기
    
    ```r
    count10 <- function(x) sum(x >= 10)
    sapply(a, count10)
    #  x  y  z
    # 21 27  0
    ```
    
- 무기명 함수
    
    ```r
    sapply(a, function(x) sum(x >= 5))
    #  x  y  z
    # 26 28  6
    
    sapply(list(x=1:5, y=x^2, z=sqrt(x)), mean)
    #         x          y          z
    #  3.000000 315.166667   3.736095
    ```
    

## 3. R 연산자

```r
1 + 3
# 4

typeof(`+`)
# "builtin"

`+`(1, 2)
# 3

`-`(1, 2)
# -1

`%f%` <- function(x, y) x^2 - y

2 %f% 4
# 0

3 %f% 0
# 9

`%f%`(1, 2)
# -1
```

## 4. 변수 범위

- 변수 범위의 필요성 : 변수 이름의 충돌 가능성 매우 높음
- 함수 본문에 사용되는 변수의 종류
    - 첫번째 범주 : 함수의 형식 인수, 인수 리스트
    - 두번째 범주 : 지역 변수, 함수 본문 안에서 할당
    - 세번째 변주 : 자유 변수, 형식 인수도 지역 변수도 아닌 변수
- 지역 변수, 형식 인수, 자유 변수 순으로 변수 평가 이루어짐
    
    ```r
    rm(x, y, z)
    # Warning in rm(x, y, z): 객체 'z'를 찾을 수 없습니다
    
    f <- function(x) {
      y <- 10
      x + y + z
    }
    ```
    
- 자유 변수는 함수가 정의가 이루어진 환경에서 함수가 호출될 때 평가가 이루어짐
    
    ```r
    f(1)
    # Error in f(1): 객체 'z'를 찾을 수 없습니다
    
    z <- 3
    f(1)
    # 14
    ```
    
- 동일한 이름이어도 함수 내부의 변수와 외부의 변수는 별개의 변수
    
    ```r
    x
    # Error in eval(expr, envir, enclos): 객체 'x'를 찾을 수 없습니다
    
    y
    # Error in eval(expr, envir, enclos): 객체 'y'를 찾을 수 없습니다
    
    x <- 0; y <- 0
    f(2)
    # 15
    
    x
    # 0
    
    y
    # 0
    
    z <- 10
    f(2)
    # 22
    ```
    
- 자유 변수를 함수 내부에서 할당하면 새로운 지역 변수가 됨
    
    ```r
    z <- 10
    f <- function(x) {
      y <- 10
      a <- x + y + z
      z <- 0
      b <- x + y + z
      c(a, b)
    }
    f(2)
    # 22 12
    
    z
    # 10
    ```
    
- 함수 외부 환경의 변수에 값 할당하기
    
    ```r
    x <- 0
    call.count <- function() {
      x <- x + 1
      cat(x, "번 호출되었습니다.")
    }
    call.count()
    # 1 번 호출되었습니다.
    
    call.count()
    # 1 번 호출되었습니다.
    
    x
    # 0
    ```
    
- 수퍼 할당 연산자
    
    ```r
    call.count <- function() {
      x <<- x + 1
      cat(x, "번 호출되었습니다.")
    }
    call.count()
    # 1 번 호출되었습니다.
    
    call.count()
    # 2 번 호출되었습니다.
    
    x
    # 2
    
    rm(w)
    # Warning in rm(w): 객체 'w'를 찾을 수 없습니다
    
    w
    # Error in eval(expr, envir, enclos): 객체 'w'를 찾을 수 없습니다
    
    sq <- function(a) w <<- a^2
    sq(10)
    w
    # 100
    ```
    
- 함수의 외부 환경이 함수인 경우
    
    ```r
    f.out <- function(y){
      f.in <- function(z){
        x <- 2
        x + y + z
      }
      return(f.in) 
    }
    
    x <- 1; y <- 10; z <- 100
    a <- f.out(20)
    a(200)
    # 222
    
    b <- f.out(30)
    b(300)
    # 332
    ```
    
- `environment()`
    
    ```r
    environment(f.out)
    # <environment: R_GlobalEnv>
    
    environment(a); parent.env(environment(a))
    # <environment: 0x55b10d562148>
    # <environment: R_GlobalEnv>
    
    environment(b); parent.env(environment(b))
    # <environment: 0x55b10cdedf78>
    # <environment: R_GlobalEnv>
    
    environment(f.in)
    # Error in eval(expr, envir, enclos): 객체 'f.in'를 찾을 수 없습니다
    ```
    
- `ls()` 와 `get()`
    
    ```r
    ls(environment(a))
    # "f.in" "y"
    
    ls(environment(b))
    # "f.in" "y"
    
    get("y", envir=environment(a))
    # 20
    
    get("y", envir=environment(b))
    # 30
    
    get("y", envir=.GlobalEnv)
    # 10
    ```
