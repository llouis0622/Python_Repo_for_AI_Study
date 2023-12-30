# 06. R 데이터 프레임

- 데이터 프레임 : 행렬을 일반화한 것
- 데이터 집합, 데이터 행렬
- `data.frame` 클래스인 리스트

# 1. 범주형 데이터와 요인(Factors)

## 1. 명목형 변수와 요인

- 범주 데이터의 숫자 코딩
    
    ```r
    results <- c(1, 3, 2, 4, 3, 2, 1, 3, 2, 2)
    # 1 3 2 4 3 2 1 3 2 2
    ```
    
- 숫자 코딩의 문제점
    
    ```r
    results[1] <- 5
    # 5 3 2 4 3 2 1 3 2 2
    
    mean(results)
    # 2.7
    ```
    
- `factor()` : 요인 → 범주형 데이터 처리 시 이용
- 수준 Levels
    
    ```r
    results
    # 5 3 2 4 3 2 1 3 2 2
    
    attributes(results)
    # NULL
    
    fResults <- factor(results, levels=1:4)
    # <NA> 3 2 4 3 2 1 3 2 2   
    # Levels: 1 2 3 4
    
    attributes(fResults)
    # $levels
    # "1" "2" "3" "4"
    # $class
    # "factor"
    
    results[1] <- 1
    fResults <- factor(results, levels=1:4)
    # 1 3 2 4 3 2 1 3 2 2
    # Levels: 1 2 3 4
    
    fResults[11] <- 4
    # 1 3 2 4 3 2 1 3 2 2 4
    # Levels: 1 2 3 4
    
    fResults[12] <- 5
    # Warning in `[<-.factor`(`*tmp*`, 12, value = 5): 요인의 수준(factor level)이 올바르지 않아 NA가 생성되었습니다.
    
    fResults
    # 1 3 2 4 3 2 1 3 2 2 4 <NA>
    Levels: 1 2 3 4
    
    fResults[12] <- 2
    # 1 3 2 4 3 2 1 3 2 2 4 2
    # Levels: 1 2 3 4
    
    mean(fResults)
    # Warning in mean.default(fResults): 인자가 수치형 또는 논리형이 아니므로 NA를 반환합니다.
    # NA
    ```
    
- `levels()`
    
    ```r
    levels(fResults)
    # "1" "2" "3" "4"
    
    levels(fResults) <- c("A", "B", "C", "None")
    # A C B None C B A C B B None B
    # Levels: A B C None
    
    typeof(fResults)
    # "integer"
    
    class(fResults)
    # "factor"
    
    unclass(fResults)
    # 1 3 2 4 3 2 1 3 2 2 4 2
    
    attr(, "levels")
    # "A" "B" "C" "None"
    
    levels(fResults)
    # "A" "B" "C" "None"
    
    fResults[11] <- 4
    # Warning in `[<-.factor`(`*tmp*`, 11, value = 4): 요인의 수준(factor level)이 올바르지 않아 NA가 생성되었습니다.
    
    fResults[12] <- "None"
    # A C B None C B A C B B <NA> None
    # Levels: A B C None
    ```
    

## 2. 순서형 변수와 요인

- 요인 : 디폴트로 수준 간에 순서가 없는 명목형 변수로 데이터 처리
    
    ```r
    satisfaction <- c("매우 불만", "매우 만족", "불만", "만족", "보통", "불만", "매우 불만", "보통", "매우 만족", "불만")
    fSatisfaction <- factor(satisfaction, levels=c("매우 불만", "불만", "보통", "만족", "매우 만족"))
    # [1] 매우 불만 매우 만족 불만 만족 보통 불만 매우 불만
    # [8] 보통 매우 만족 불만     
    # Levels: 매우 불만 불만 보통 만족 매우 만족
    
    fSatisfaction >= "만족"
    # Warning in Ops.factor(fSatisfaction, "만족"): 요인(factors)에 대하여 의미있는'>='가 아닙니다.
    # NA NA NA NA NA NA NA NA NA NA
    ```
    
- `ordered` 인수로 순서형 변수 만들기
    
    ```r
    oSatisfaction <- factor(satisfaction, ordered = TRUE, levels=c("매우 불만", "불만", "보통", "만족", "매우 만족"))
    # [1] 매우 불만 매우 만족 불만 만족 보통 불만 매우 불만
    # [8] 보통 매우 만족 불만     
    # Levels: 매우 불만 < 불만 < 보통 < 만족 < 매우 만족
    
    oSatisfaction >= "만족"
    # FALSE TRUE FALSE TRUE FALSE FALSE FALSE FALSE TRUE FALSE
    
    sum(oSatisfaction >= "만족")
    # 3
    
    mean(oSatisfaction >= "만족")
    # 0.3
    
    order(oSatisfaction)
    # 1 7 3 6 10 5 8 4 2 9
    
    oSatisfaction <- factor(satisfaction, ordered = TRUE, levels=c("매우 만족", "만족", "보통", "불만", "매우 불만"))
    # [1] 매우 불만 매우 만족 불만 만족 보통 불만 매우 불만
    # [8] 보통 매우 만족 불만     
    # Levels: 매우 만족 < 만족 < 보통 < 불만 < 매우 불만
    
    oSatisfaction >= "만족"
    # TRUE FALSE TRUE TRUE TRUE TRUE TRUE TRUE FALSE TRUE
    
    sum(oSatisfaction >= "만족")
    # 8
    
    mean(oSatisfaction >= "만족")
    # 0.8
    
    order(oSatisfaction)
    # 2 9 4 5 8 3 6 10 1 7
    ```
    
- 수준의 순서
    
    ```r
    a <- c("F", "M", "F", "M", "F")
    fa1 <- factor(a)
    # F M F M F
    # Levels: F M
    
    unclass(fa1)
    # 1 2 1 2 1
    
    attr(,"levels")
    # "F" "M"
    
    table(fa1)
    # fa1
    # F M
    # 3 2
    
    fa2 <- factor(a, levels=c("M", "F"))
    # F M F M F
    # Levels: M F
    
    unclass(fa2)
    # 2 1 2 1 2
    
    attr(,"levels")
    # "M" "F"
    
    table(fa2)
    # fa2
    # M F
    # 2 3
    ```
    
- `relevel()` 과 `reorder()` 를 이용한 수준의 순서 변경
    
    ```r
    fResults
    # A C B None C B A C B B <NA> None
    # Levels: A B C None
    
    fResults2 <- relevel(fResults, ref="None")
    # A C B None C B A C B B <NA> None
    # Levels: None A B C
    
    table(fResults2)
    # fResults2
    # None    A    B    C
    #    2    2    4    3
    
    head(InsectSprays)
    #   count spray
    # 1    10     A
    # 2     7     A
    # 3    20     A
    # 4    14     A
    # 5    14     A
    # 6    12     A
    
    InsectSprays$spray
    # [1] A A A A A A A A A A A A B B B B B B B B B B B B C C C C C C C C C C C C D D
    # [39] D D D D D D D D D D E E E E E E E E E E E E F F F F F F F F F F F F
    # Levels: A B C D E F
    ```
    
    ```r
    boxplot(count ~ spray, data=InsectSprays)
    ```
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/b61a1b68-2c4d-4fac-8e68-3a8092e19379/1.png)
    
    ```r
    boxplot(count ~ reorder(spray, count, median), data=InsectSprays)
    ```
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ee0f50c1-d275-4fb3-b51f-28ff7208b991/1.png)
    
- `labels` 인수
    
    ```r
    fa3 <- factor(a, levels=c("M", "F"), labels=c("Male", "Female"))
    # Female Male Female Male Female
    # Levels: Male Female
    
    unclass(fa3)
    # 2 1 2 1 2
    
    attr(,"levels")
    # "Male" "Female"
    
    table(fa3)
    # fa3
    # Male Female 
    #    2      3
    
    fa3[6] <- "M"
    # Warning in `[<-.factor`(`*tmp*`, 6, value = "M"): 요인의 수준(factor level)이 올바르지 않아 NA가 생성되었습니다.
    
    fa3[6] <- "Male"
    ```

    # 2. 데이터 프레임 만들기

- `data.frame()` : 벡터, 행렬, 요인, 다른 데이터 프레임을 묶어 새로운 데이터 프레임 생성
    - 벡터는 모두 같은 길이, 행렬/데이터 프레임은 모두 같은 행 수
    - 벡터는 하나의 벡터가 데이터 프레임의 하나의 열, 행렬/데이터 프레임은 각 열이 데이터 프레임의 하나의 열
    
    ```r
    name <- c("김철수", "김영희", "이철수", "이영희", "홍길동")
    grade <- c(1, 4, 3, 2, 1)
    gender <- c(" M", "F", "M", "F", "M")
    student <- data.frame(name, grade, gender)
    #     name grade gender
    # 1 김철수     1      M
    # 2 김영희     4      F
    # 3 이철수     3      M
    # 4 이영희     2      F
    # 5 홍길동     1      M
    
    midterm = c(74, 82, 67, 89, 92)
    final = c(91, 77, 88, 78, 86)
    scores = cbind(midterm, final)
    #      midterm final
    # [1,]      74    91
    # [2,]      82    77
    # [3,]      67    88
    # [4,]      89    78
    # [5,]      92    86
    
    rt <- c(TRUE, FALSE, FALSE, TRUE, FALSE)
    students <- data.frame(student, scores, retake=rt)
    #     name grade gender midterm final retake
    # 1 김철수     1      M      74    91   TRUE
    # 2 김영희     4      F      82    77  FALSE
    # 3 이철수     3      M      67    88  FALSE
    # 4 이영희     2      F      89    78   TRUE
    # 5 홍길동     1      M      92    86  FALSE
    ```
    
- `cbind()`
    
    ```r
    total.scores <- midterm + final
    cbind(students, total.scores)
    #     name grade gender midterm final retake total.scores
    # 1 김철수     1      M      74    91   TRUE          165
    # 2 김영희     4      F      82    77  FALSE          159
    # 3 이철수     3      M      67    88  FALSE          155
    # 4 이영희     2      F      89    78   TRUE          167
    # 5 홍길동     1      M      92    86  FALSE          178
    ```
    
- `rbind()`
    
    ```r
    a <- data.frame(name="Jane Eyre", grade=4, gender="F", midterm=90, final=85, retake=F)
    #        name grade gender midterm final retake
    # 1 Jane Eyre     4      F      90    85  FALSE
    
    rbind(students, a)
    #        name grade gender midterm final retake
    # 1    김철수     1      M      74    91   TRUE
    # 2    김영희     4      F      82    77  FALSE
    # 3    이철수     3      M      67    88  FALSE
    # 4    이영희     2      F      89    78   TRUE
    # 5    홍길동     1      M      92    86  FALSE
    # 6 Jane Eyre     4      F      90    85  FALSE
    ```

# 3. 데이터 프레임 각 열의 지정

- 데이터 프레임은 리스트 타입
    
    ```r
    typeof(students)
    # "list"
    
    attributes(students)
    # $names
    # "name" "grade" "gender" "midterm" "final" "retake"
    # $class
    # "data.frame"
    # $row.names
    # 1 2 3 4 5
    ```
    
- 리스트 형식으로 데이터 프레임의 열 지정
    
    ```r
    data_frame_name$column_name
    data_frame_name[[column_number]]
    data_frame_name[[column_name]]
    ```
    
    ```r
    students$gender
    # "M" "F" "M" "F" "M"
    
    students[["midterm"]]
    # 74 82 67 89 92
    
    students[[5]]
    # 91 77 88 78 86
    
    students$name
    # "김철수" "김영희" "이철수" "이영희" "홍길동"
    
    typeof(students$name)
    # "character"
    ```
    
- 데이터 프레임의 각 열은 벡터
    
    ```r
    students$midterm * 2
    # 148 164 134 178 184
    
    sum(students$midterm)
    # 404
    
    students$midterm[5]
    # 92
    
    students$midterm[5] <- 50
    students[[4]][3:5]
    # 67 89 50
    
    students$hw <- c(8, 9, 7, 8, 10)
    #     name grade gender midterm final retake hw
    # 1 김철수     1      M      74    91   TRUE  8
    # 2 김영희     4      F      82    77  FALSE  9
    # 3 이철수     3      M      67    88  FALSE  7
    # 4 이영희     2      F      89    78   TRUE  8
    # 5 홍길동     1      M      50    86  FALSE 10
    ```
    

# 4. 데이터 프레임의 필터링

## 1. 리스트 형식으로 필터링

- 리스트로서 필터링은 1차원 인덱스 구조를 가짐
    
    ```r
    data_frame_name[index_vector]
    ```
    
    ```r
    students.new <- students[1:2]
    #     name grade
    # 1 김철수     1
    # 2 김영희     4
    # 3 이철수     3
    # 4 이영희     2
    # 5 홍길동     1
    
    students.new <- students[-(1:2)]
    #   gender midterm final retake hw
    # 1      M      74    91   TRUE  8
    # 2      F      82    77  FALSE  9
    # 3      M      67    88  FALSE  7
    # 4      F      89    78   TRUE  8
    # 5      M      50    86  FALSE 10
    
    student.new <- students[c("gender", "grade")]
    #   gender grade
    # 1      M     1
    # 2      F     4
    # 3      M     3
    # 4      F     2
    # 5      M     1
    
    student.new <- students[c(T, F, F, T, T, F)]
    #     name midterm final hw
    # 1 김철수      74    91  8
    # 2 김영희      82    77  9
    # 3 이철수      67    88  7
    # 4 이영희      89    78  8
    # 5 홍길동      50    86 10
    
    height <- c(172, 167, 181, 162, 178)
    students.new <- data.frame(students[2:3], height=height)
    #   grade gender height
    # 1     1      M    172
    # 2     4      F    167
    # 3     3      M    181
    # 4     2      F    162
    # 5     1      M    178
    ```
    
- 열 지정하기 vs 한 열만 데이터 프레임으로 필터링
    
    ```r
    a <- students[2]
    #   grade
    # 1     1
    # 2     4
    # 3     3
    # 4     2
    # 5     1
    
    typeof(a)
    # "list"
    
    attributes(a)
    # $names
    # "grade"
    # $row.names
    # 1 2 3 4 5
    # $class
    # "data.frame"
    
    a <- students[[2]]
    # 1 4 3 2 1
    
    typeof(a)
    # "double"
    
    attributes(a)
    # NULL
    ```
    

## 2. 행렬 형식으로 필터링

- 행렬로서 필터링은 2차원 인덱스 구조를 가짐
    
    ```r
    data_frame_name[row_index_vector, column_index_vector]
    ```
    
    ```r
    students[1,]
    #     name grade gender midterm final retake hw
    # 1 김철수     1      M      74    91   TRUE  8
    
    students[2:3,]
    #     name grade gender midterm final retake hw
    # 2 김영희     4      F      82    77  FALSE  9
    # 3 이철수     3      M      67    88  FALSE  7
    
    students[-(2:3),]
    #     name grade gender midterm final retake hw
    # 1 김철수     1      M      74    91   TRUE  8
    # 4 이영희     2      F      89    78   TRUE  8
    # 5 홍길동     1      M      50    86  FALSE 10
    
    students[,4]
    # 74 82 67 89 50
    
    students[,-4]
    #     name grade gender final retake hw
    # 1 김철수     1      M    91   TRUE  8
    # 2 김영희     4      F    77  FALSE  9
    # 3 이철수     3      M    88  FALSE  7
    # 4 이영희     2      F    78   TRUE  8
    # 5 홍길동     1      M    86  FALSE 10
    
    students[, c(2, 4)]
    #   grade midterm
    # 1     1      74
    # 2     4      82
    # 3     3      67
    # 4     2      89
    # 5     1      50
    
    students[2:4, 3:5]
    #   gender midterm final
    # 2      F      82    77
    # 3      M      67    88
    # 4      F      89    78
    
    students$midterm >= 80
    # FALSE TRUE FALSE TRUE FALSE
    
    students[students$midterm >= 80, ]
    #     name grade gender midterm final retake hw
    # 2 김영희     4      F      82    77  FALSE  9
    # 4 이영희     2      F      89    78   TRUE  8
    
    students[students$midterm >= 80, c("name", "grade", "gender")]
    #     name grade gender
    # 2 김영희     4      F
    # 4 이영희     2      F
    
    students[students$grade != 1, c("name", "grade", "gender")]
    #     name grade gender
    # 2 김영희     4      F
    # 3 이철수     3      M
    # 4 이영희     2      F
    ```
    
- 행렬 필터링 방법을 이용한 데이터 프레임 정렬
    
    ```r
    order(students$grade)
    # 1 5 4 3 2
    
    students[order(students$grade), ]
    #     name grade gender midterm final retake hw
    # 1 김철수     1      M      74    91   TRUE  8
    # 5 홍길동     1      M      50    86  FALSE 10
    # 4 이영희     2      F      89    78   TRUE  8
    # 3 이철수     3      M      67    88  FALSE  7
    # 2 김영희     4      F      82    77  FALSE  9
    
    order(students$final, decreasing = TRUE)
    # 1 3 5 4 2
    
    students[order(students$final, decreasing = TRUE), ]
    #     name grade gender midterm final retake hw
    # 1 김철수     1      M      74    91   TRUE  8
    # 3 이철수     3      M      67    88  FALSE  7
    # 5 홍길동     1      M      50    86  FALSE 10
    # 4 이영희     2      F      89    78   TRUE  8
    # 2 김영희     4      F      82    77  FALSE  9
    
    order(students$grade, students$final)
    # 5 1 4 3 2
    
    students[order(students$grade, students$final), ]
    #     name grade gender midterm final retake hw
    # 5 홍길동     1      M      50    86  FALSE 10
    # 1 김철수     1      M      74    91   TRUE  8
    # 4 이영희     2      F      89    78   TRUE  8
    # 3 이철수     3      M      67    88  FALSE  7
    # 2 김영희     4      F      82    77  FALSE  9
    
    students[order(students$grade, students$final, decreasing=T), ]
    #     name grade gender midterm final retake hw
    # 2 김영희     4      F      82    77  FALSE  9
    # 3 이철수     3      M      67    88  FALSE  7
    # 4 이영희     2      F      89    78   TRUE  8
    # 1 김철수     1      M      74    91   TRUE  8
    # 5 홍길동     1      M      50    86  FALSE 10
    
    students[order(students$grade, -students$final), ]
    #     name grade gender midterm final retake hw
    # 1 김철수     1      M      74    91   TRUE  8
    # 5 홍길동     1      M      50    86  FALSE 10
    # 4 이영희     2      F      89    78   TRUE  8
    # 3 이철수     3      M      67    88  FALSE  7
    # 2 김영희     4      F      82    77  FALSE  9
    ```
    

## 3. `subset()` 을 이용한 필터링

- `subset()` : 벡터, 행렬, 데이터 프레임에서 조건에 맞는 부분을 반환
    
    ```r
    subset(x, subset, select, drop=FALSE, ...)
    ```
    
- `subset()` 을 이용한 벡터 필터링
    
    ```r
    x <- c(7, 9, NA, 5, 2)
    x[x>6]
    # 7 9 NA
    
    subset(x, x> 6)
    # 7 9
    ```
    
- `subset()` 을 이용한 데이터 프레임 필터링
    
    ```r
    y <- 1:5
    z <- -1:-5
    long.name <- data.frame(x, y, z)
    #    x y  z
    # 1  7 1 -1
    # 2  9 2 -2
    # 3 NA 3 -3
    # 4  5 4 -4
    # 5  2 5 -5
    
    rm(x, y, z)
    long.name[long.name$x>6, ]
    #     x  y  z
    # 1   7  1 -1
    # 2   9  2 -2
    # NA NA NA NA
    
    subset(long.name, x>6)
    #   x y  z
    # 1 7 1 -1
    # 2 9 2 -2
    
    long.name[long.name$x>6, 2:3]
    #     y  z
    # 1   1 -1
    # 2   2 -2
    # NA NA NA
    
    subset(long.name, x>6, y:z)
    #   y  z
    # 1 1 -1
    # 2 2 -2
    
    long.name[long.name$x >6, c("x", "z")]
    #     x  z
    # 1   7 -1
    # 2   9 -2
    # NA NA NA
    
    subset(long.name, x>6, c(x, z))
    #   x  z
    # 1 7 -1
    # 2 9 -2
    
    subset(long.name, x>6, -z)
    #   x y
    # 1 7 1
    # 2 9 2
    ```
