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
