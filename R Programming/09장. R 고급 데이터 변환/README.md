# 09. R 고급 데이터 변환

```r
library(tidyverse)
```

# 1. 데이터의 단순 결합

## 1. 데이터를 행으로 결합하기

- 열 구조가 다른 데이터를 행으로 결합하기
    
    ```r
    load("advancedDataMgmt.RData")
    
    class1
    #    ID   Name Gender Year Address Midterm Final Team
    # 1  15 김철수      M    1    서울      78    59    A
    # 2  18 김영희      F    3    경기      85    87    A
    # 3  25 이철수      M    3    충남      80    70    B
    # 4  34 이영희      F    2    대전      92    89    B
    # 5 151 홍길동   Male    4    세종      58    66    B
    
    class2
    #   ID Mid Final   Name Team Gen Year
    # 1 12  75    79 장철수    C   M    2
    # 2 19  75    89 장영희    C   F    2
    # 3 28  87    76 최철수    D   M    1
    # 4 45  82    79 최영희    D   F   30
    ```
    
- `rbind()` 는 열의 개수가 다른 데이터 프레임을 행으로 결합하기 못함
    
    ```r
    rbind(class1, class2)
    # Error in rbind(deparse.level, ...): numbers of columns of arguments do not match
    ```
    
- `bind_rows()` 는 열의 개수가 다른 데이터 프레임도 행으로 결합함
    
    ```r
    bind_rows(class1, class2)
    #    ID   Name Gender Year Address Midterm Final Team Mid  Gen
    # 1  15 김철수      M    1    서울      78    59    A  NA <NA>
    # 2  18 김영희      F    3    경기      85    87    A  NA <NA>
    # 3  25 이철수      M    3    충남      80    70    B  NA <NA>
    # 4  34 이영희      F    2    대전      92    89    B  NA <NA>
    # 5 151 홍길동   Male    4    세종      58    66    B  NA <NA>
    # 6  12 장철수   <NA>    2    <NA>      NA    79    C  75    M
    # 7  19 장영희   <NA>    2    <NA>      NA    89    C  75    F
    # 8  28 최철수   <NA>    1    <NA>      NA    76    D  87    M
    # 9  45 최영희   <NA>   30    <NA>      NA    79    D  82    F
    ```
    
- `rbind()` 는 두 데이터의 열의 이름이 다른 경우 행으로 결합하지 못함
    
    ```r
    rbind(select(class1, -Address), class2)
    # Error in match.names(clabs, names(xi)): 이전에 사용된 이름들과 일치하지 않습니다.
    
    rbind(select(class1, -Address), rename(class2, Midterm=Mid, Gender=Gen))
    #    ID   Name Gender Year Midterm Final Team
    # 1  15 김철수      M    1      78    59    A
    # 2  18 김영희      F    3      85    87    A
    # 3  25 이철수      M    3      80    70    B
    # 4  34 이영희      F    2      92    89    B
    # 5 151 홍길동   Male    4      58    66    B
    # 6  12 장철수      M    2      75    79    C
    # 7  19 장영희      F    2      75    89    C
    # 8  28 최철수      M    1      87    76    D
    # 9  45 최영희      F   30      82    79    D
    ```
    
- `rbind()` 와 `bind_rows()` 는 열의 순서를 자동으로 맞춤
    
    ```r
    class12 <- bind_rows(select(class1, -Address), 
                 rename(class2, Midterm = Mid, Gender = Gen))
    #    ID   Name Gender Year Midterm Final Team
    # 1  15 김철수      M    1      78    59    A
    # 2  18 김영희      F    3      85    87    A
    # 3  25 이철수      M    3      80    70    B
    # 4  34 이영희      F    2      92    89    B
    # 5 151 홍길동   Male    4      58    66    B
    # 6  12 장철수      M    2      75    79    C
    # 7  19 장영희      F    2      75    89    C
    # 8  28 최철수      M    1      87    76    D
    # 9  45 최영희      F   30      82    79    D
    ```
    
- 합쳐지는 데이터에 식별자 부여하기
    
    ```r
    bind_rows(select(class1, -Address), 
             rename(class2, Midterm=Mid, Gender=Gen),
             .id="Class")
    #   Class  ID   Name Gender Year Midterm Final Team
    # 1     1  15 김철수      M    1      78    59    A
    # 2     1  18 김영희      F    3      85    87    A
    # 3     1  25 이철수      M    3      80    70    B
    # 4     1  34 이영희      F    2      92    89    B
    # 5     1 151 홍길동   Male    4      58    66    B
    # 6     2  12 장철수      M    2      75    79    C
    # 7     2  19 장영희      F    2      75    89    C
    # 8     2  28 최철수      M    1      87    76    D
    # 9     2  45 최영희      F   30      82    79    D
    ```
    

## 2. 데이터를 열로 결합하기

- 행 순서가 다른 데이터를 열로 결합하기
    
    ```r
    attendance
    #    ID Class Attend
    # 1  12     2    185
    # 2  15     1     90
    # 3  18     1     95
    # 4  19     2    100
    # 5  25     1    100
    # 6  28     2    100
    # 7  34     1    100
    # 8  45     2    100
    # 9 151     1     95
    ```
    
- 정렬 후 열로 결합하기
    
    ```r
    class12.a <- bind_cols(arrange(class12, ID), select(attendance, -ID))
    #    ID   Name Gender Year Midterm Final Team Class Attend
    # 1  12 장철수      M    2      75    79    C     2    185
    # 2  15 김철수      M    1      78    59    A     1     90
    # 3  18 김영희      F    3      85    87    A     1     95
    # 4  19 장영희      F    2      75    89    C     2    100
    # 5  25 이철수      M    3      80    70    B     1    100
    # 6  28 최철수      M    1      87    76    D     2    100
    # 7  34 이영희      F    2      92    89    B     1    100
    # 8  45 최영희      F   30      82    79    D     2    100
    # 9 151 홍길동   Male    4      58    66    B     1     95
    
    class12.b <- bind_cols(class12, 
                    attendance %>% arrange(Class, ID) %>% select(-ID))
    #    ID   Name Gender Year Midterm Final Team Class Attend
    # 1  15 김철수      M    1      78    59    A     1     90
    # 2  18 김영희      F    3      85    87    A     1     95
    # 3  25 이철수      M    3      80    70    B     1    100
    # 4  34 이영희      F    2      92    89    B     1    100
    # 5 151 홍길동   Male    4      58    66    B     1     95
    # 6  12 장철수      M    2      75    79    C     2    185
    # 7  19 장영희      F    2      75    89    C     2    100
    # 8  28 최철수      M    1      87    76    D     2    100
    # 9  45 최영희      F   30      82    79    D     2    100
    ```
    

# 2. 관계형 데이터베이스처럼 데이터 결합하기

## 1. Inner Join과 Outer Join

- inner join
    
    ```r
    inner_join(class12, attendance, by="ID")
    #    ID   Name Gender Year Midterm Final Team Class Attend
    # 1  15 김철수      M    1      78    59    A     1     90
    # 2  18 김영희      F    3      85    87    A     1     95
    # 3  25 이철수      M    3      80    70    B     1    100
    # 4  34 이영희      F    2      92    89    B     1    100
    # 5 151 홍길동   Male    4      58    66    B     1     95
    # 6  12 장철수      M    2      75    79    C     2    185
    # 7  19 장영희      F    2      75    89    C     2    100
    # 8  28 최철수      M    1      87    76    D     2    100
    # 9  45 최영희      F   30      82    79    D     2    100
    ```
    
- 1:1 inner join
    
    ```r
    inner_join(class12, attendance)
    # Joining with `by = join_by(ID)`
    #    ID   Name Gender Year Midterm Final Team Class Attend
    # 1  15 김철수      M    1      78    59    A     1     90
    # 2  18 김영희      F    3      85    87    A     1     95
    # 3  25 이철수      M    3      80    70    B     1    100
    # 4  34 이영희      F    2      92    89    B     1    100
    # 5 151 홍길동   Male    4      58    66    B     1     95
    # 6  12 장철수      M    2      75    79    C     2    185
    # 7  19 장영희      F    2      75    89    C     2    100
    # 8  28 최철수      M    1      87    76    D     2    100
    # 9  45 최영희      F   30      82    79    D     2    100
    ```
    
- 0:1 inner join
    
    ```r
    inner_join(class1, attendance, by="ID")
    #    ID   Name Gender Year Address Midterm Final Team Class Attend
    # 1  15 김철수      M    1    서울      78    59    A     1     90
    # 2  18 김영희      F    3    경기      85    87    A     1     95
    # 3  25 이철수      M    3    충남      80    70    B     1    100
    # 4  34 이영희      F    2    대전      92    89    B     1    100
    # 5 151 홍길동   Male    4    세종      58    66    B     1     95
    ```
    
- outer join
    
    ```r
    x <- data.frame(id = 1:3, name = letters[1:3]); x
    #   id name
    # 1  1    a
    # 2  2    b
    # 3  3    c
    
    y <- data.frame(id = 2:4, addr = LETTERS[2:4]); y
    #   id addr
    # 1  2    B
    # 2  3    C
    # 3  4    D
    
    inner_join(x, y)
    Joining with `by = join_by(id)`
    #   id name addr
    # 1  2    b    B
    # 2  3    c    C
    
    left_join(x, y)
    Joining with `by = join_by(id)`
    #   id name addr
    # 1  1    a <NA>
    # 2  2    b    B
    # 3  3    c    C
    
    right_join(x, y)
    Joining with `by = join_by(id)`
    #   id name addr
    # 1  2    b    B
    # 2  3    c    C
    # 3  4 <NA>    D
    
    full_join(x, y)
    Joining with `by = join_by(id)`
    #   id name addr
    # 1  1    a <NA>
    # 2  2    b    B
    # 3  3    c    C
    # 4  4 <NA>    D
    
    right_join(class1, attendance, by="ID")
    #    ID   Name Gender Year Address Midterm Final Team Class Attend
    # 1  15 김철수      M    1    서울      78    59    A     1     90
    # 2  18 김영희      F    3    경기      85    87    A     1     95
    # 3  25 이철수      M    3    충남      80    70    B     1    100
    # 4  34 이영희      F    2    대전      92    89    B     1    100
    # 5 151 홍길동   Male    4    세종      58    66    B     1     95
    # 6  12   <NA>   <NA>   NA    <NA>      NA    NA <NA>     2    185
    # 7  19   <NA>   <NA>   NA    <NA>      NA    NA <NA>     2    100
    # 8  28   <NA>   <NA>   NA    <NA>      NA    NA <NA>     2    100
    # 9  45   <NA>   <NA>   NA    <NA>      NA    NA <NA>     2    100
    ```
    
- 1:N inner join
    
    ```r
    pjt
    #   Team Project
    # 1    A      80
    # 2    B      90
    # 3    C      85
    # 4    D      75
    
    class12.c <- inner_join(class12.a, pjt, by="Team")
    #    ID   Name Gender Year Midterm Final Team Class Attend Project
    # 1  12 장철수      M    2      75    79    C     2    185      85
    # 2  15 김철수      M    1      78    59    A     1     90      80
    # 3  18 김영희      F    3      85    87    A     1     95      80
    # 4  19 장영희      F    2      75    89    C     2    100      85
    # 5  25 이철수      M    3      80    70    B     1    100      90
    # 6  28 최철수      M    1      87    76    D     2    100      75
    # 7  34 이영희      F    2      92    89    B     1    100      90
    # 8  45 최영희      F   30      82    79    D     2    100      75
    # 9 151 홍길동   Male    4      58    66    B     1     95      90
    ```
    
- 두 열 이상을 기준으로 join
    
    ```r
    cAge
    #   first.name last.name age
    # 1      James    Bolton  34
    # 2      James     Tiger  26
    # 3     Goerge     Tiger  47
    
    cIncome
    #   first.name last.name income
    # 1     Goerge     Tiger     35
    # 2      James    Bolton     24
    # 3      James     Tiger     18
    
    inner_join(cAge, cIncome, by="first.name")
    # Warning in inner_join(cAge, cIncome, by = "first.name"): Detected an unexpected many-to-many relationship between `x` and `y`.
    # ℹ Row 1 of `x` matches multiple rows in `y`.
    # ℹ Row 2 of `y` matches multiple rows in `x`.
    # ℹ If a many-to-many relationship is expected, set `relationship =
    #   "many-to-many"` to silence this warning.
    #   first.name last.name.x age last.name.y income
    # 1      James      Bolton  34      Bolton     24
    # 2      James      Bolton  34       Tiger     18
    # 3      James       Tiger  26      Bolton     24
    # 4      James       Tiger  26       Tiger     18
    # 5     Goerge       Tiger  47       Tiger     35
    
    inner_join(cAge, cIncome, by=c("last.name", "first.name"))
    #   first.name last.name age income
    # 1      James    Bolton  34     24
    # 2      James     Tiger  26     18
    # 3     Goerge     Tiger  47     35
    ```
    

## 2. Filtering Join

```r
semi_join(x, y, by="id")
#   id name
# 1  2    b
# 2  3    c

anti_join(x, y, by="id")
#   id name
# 1  1    a
```

## 3. Join을 수행하는 다른 방법들

- `merge()` 함수
    
    ```r
    merge(x, y)
    #   id name addr
    # 1  2    b    B
    # 2  3    c    C
    
    merge(x, y, all.x = TRUE)
    #   id name addr
    # 1  1    a <NA>
    # 2  2    b    B
    # 3  3    c    C
    
    merge(x, y, all.y = TRUE)
    #   id name addr
    # 1  2    b    B
    # 2  3    c    C
    # 3  4 <NA>    D
    
    merge(x, y, all = TRUE)
    #   id name addr
    # 1  1    a <NA>
    # 2  2    b    B
    # 3  3    c    C
    # 4  4 <NA>    D
    ```
    
- `spldf` 패키지 : SQL 문법을 이용하여 R의 데이터 프레임에서 데이터를 조회하거나 결합할 수 있도록 함

# 3. `tidyr` 패키지를 이용하여 정돈 데이터 형식으로 바꾸기

## 1. `pivot_longer` : 여러 열에 걸친 한 변수의 데이터를 하나의 열로 길게 모으기

```r
table4a
# A tibble: 3 × 3
#   country     `1999` `2000`
#   <chr>        <dbl>  <dbl>
# 1 Afghanistan    745   2666
# 2 Brazil       37737  80488
# 3 China       212258 213766

table4a %>%
  pivot_longer(c(`1999`, `2000`), names_to = "year", values_to ="cases")
# A tibble: 6 × 3
#   country     year   cases
#   <chr>       <chr>  <dbl>
# 1 Afghanistan 1999     745
# 2 Afghanistan 2000    2666
# 3 Brazil      1999   37737
# 4 Brazil      2000   80488
# 5 China       1999  212258
# 6 China       2000  213766
```

- 결측치가 있는 경우
    
    ```r
    na_table4a <- table4a
    na_table4a$`2000`[3] <- NA
    # A tibble: 3 × 3
    #   country     `1999` `2000`
    #   <chr>        <dbl>  <dbl>
    # 1 Afghanistan    745   2666
    # 2 Brazil       37737  80488
    # 3 China       212258     NA
    
    na_table4a %>% 
      pivot_longer(c(`1999`, `2000`), names_to = "year", values_to = "cases")
    # A tibble: 6 × 3
    #   country     year   cases
    #   <chr>       <chr>  <dbl>
    # 1 Afghanistan 1999     745
    # 2 Afghanistan 2000    2666
    # 3 Brazil      1999   37737
    # 4 Brazil      2000   80488
    # 5 China       1999  212258
    # 6 China       2000      NA
    
    na_long_table4a <- na_table4a %>% 
      pivot_longer(c(`1999`, `2000`), names_to = "year",
                   values_to = "cases", values_drop_na = T)
    # A tibble: 5 × 3
    #   country     year   cases
    #   <chr>       <chr>  <dbl>
    # 1 Afghanistan 1999     745
    # 2 Afghanistan 2000    2666
    # 3 Brazil      1999   37737
    # 4 Brazil      2000   80488
    # 5 China       1999  212258
    ```
    
- `gather` 함수
    
    ```r
    table4a %>%
      gather(`1999`, `2000`, key = "year", value ="cases")
    # A tibble: 6 × 3
    #   country     year   cases
    #   <chr>       <chr>  <dbl>
    # 1 Afghanistan 1999     745
    # 2 Brazil      1999   37737
    # 3 China       1999  212258
    # 4 Afghanistan 2000    2666
    # 5 Brazil      2000   80488
    # 6 China       2000  213766
    ```
    

## 2. `pivot_wider` : 한 열에 기술된 여러 변수의 데이터를 여러 열로 넓게 펼치기

```r
table2
# A tibble: 12 × 4
#    country      year type            count
#    <chr>       <dbl> <chr>           <dbl>
#  1 Afghanistan  1999 cases             745
#  2 Afghanistan  1999 population   19987071
#  3 Afghanistan  2000 cases            2666
#  4 Afghanistan  2000 population   20595360
#  5 Brazil       1999 cases           37737
#  6 Brazil       1999 population  172006362
#  7 Brazil       2000 cases           80488
#  8 Brazil       2000 population  174504898
#  9 China        1999 cases          212258
# 10 China        1999 population 1272915272
# 11 China        2000 cases          213766
# 12 China        2000 population 1280428583

table2 %>%
  pivot_wider(names_from = type, values_from = count)
# A tibble: 6 × 4
#   country      year  cases population
#   <chr>       <dbl>  <dbl>      <dbl>
# 1 Afghanistan  1999    745   19987071
# 2 Afghanistan  2000   2666   20595360
# 3 Brazil       1999  37737  172006362
# 4 Brazil       2000  80488  174504898
# 5 China        1999 212258 1272915272
# 6 China        2000 213766 1280428583
```

- 결측치가 있는 경우
    
    ```r
    na_long_table4a
    # A tibble: 5 × 3
    #   country     year   cases
    #   <chr>       <chr>  <dbl>
    # 1 Afghanistan 1999     745
    # 2 Afghanistan 2000    2666
    # 3 Brazil      1999   37737
    # 4 Brazil      2000   80488
    # 5 China       1999  212258
    
    na_long_table4a %>%
      pivot_wider(names_from = year, values_from = cases)
    # A tibble: 3 × 3
    #   country     `1999` `2000`
    #   <chr>        <dbl>  <dbl>
    # 1 Afghanistan    745   2666
    # 2 Brazil       37737  80488
    # 3 China       212258     NA
    ```
    
- `spread` 함수
    
    ```r
    table2 %>%
      spread(key = type, value = count)
    # A tibble: 6 × 4
    #   country      year  cases population
    #   <chr>       <dbl>  <dbl>      <dbl>
    # 1 Afghanistan  1999    745   19987071
    # 2 Afghanistan  2000   2666   20595360
    # 3 Brazil       1999  37737  172006362
    # 4 Brazil       2000  80488  174504898
    # 5 China        1999 212258 1272915272
    # 6 China        2000 213766 1280428583
    ```
    

## 3. `seperate` : 한 셀을 여러 셀로 분리하기

```r
table3
# A tibble: 6 × 3
#   country      year rate             
#   <chr>       <dbl> <chr>            
# 1 Afghanistan  1999 745/19987071     
# 2 Afghanistan  2000 2666/20595360    
# 3 Brazil       1999 37737/172006362  
# 4 Brazil       2000 80488/174504898  
# 5 China        1999 212258/1272915272
# 6 China        2000 213766/1280428583
```

### 1. 특정 문자를 기준으로 분리하기

```r
table3 %>%
  separate(rate, into=c("cases", "population"), sep="/")
# A tibble: 6 × 4
#   country      year cases  population
#   <chr>       <dbl> <chr>  <chr>     
# 1 Afghanistan  1999 745    19987071  
# 2 Afghanistan  2000 2666   20595360  
# 3 Brazil       1999 37737  172006362 
# 4 Brazil       2000 80488  174504898 
# 5 China        1999 212258 1272915272
# 6 China        2000 213766 1280428583
```

### 2. 분리한 열의 형변환

```r
x <- table3 %>%
  separate(rate, into=c("cases", "population"), sep="/", convert = TRUE) 
# A tibble: 6 × 4
#   country      year  cases population
#   <chr>       <dbl>  <int>      <int>
# 1 Afghanistan  1999    745   19987071
# 2 Afghanistan  2000   2666   20595360
# 3 Brazil       1999  37737  172006362
# 4 Brazil       2000  80488  174504898
# 5 China        1999 212258 1272915272
# 6 China        2000 213766 1280428583

x %>% summarise(total_cases=sum(cases), mean_pop=mean(population))
# A tibble: 1 × 2
#   total_cases   mean_pop
#         <int>      <dbl>
# 1      547660 490072924.
```

### 3. 문자 수를 기준으로 분리하기

```r
table3 %>%
  separate(rate, into=c("cases", "population"), sep=3)
# A tibble: 6 × 4
#   country      year cases population
#   <chr>       <dbl> <chr> <chr>
# 1 Afghanistan  1999 745   /19987071
# 2 Afghanistan  2000 266   6/20595360
# 3 Brazil       1999 377   37/172006362
# 4 Brazil       2000 804   88/174504898
# 5 China        1999 212   258/1272915272
# 6 China        2000 213   766/1280428583

table3 %>%
  separate(rate, into=c("cases", "population"), sep=-3)
# A tibble: 6 × 4
#   country      year cases          population
#   <chr>       <dbl> <chr>          <chr>
# 1 Afghanistan  1999 745/19987      071
# 2 Afghanistan  2000 2666/20595     360
# 3 Brazil       1999 37737/172006   362
# 4 Brazil       2000 80488/174504   898
# 5 China        1999 212258/1272915 272
# 6 China        2000 213766/1280428 583

table3 %>% 
  separate(year, into=c("century", "year"), sep=2)
# A tibble: 6 × 4
#   country     century year  rate
#   <chr>       <chr>   <chr> <chr>
# 1 Afghanistan 19      99    745/19987071
# 2 Afghanistan 20      00    2666/20595360
# 3 Brazil      19      99    37737/172006362
# 4 Brazil      20      00    80488/174504898
# 5 China       19      99    212258/1272915272
# 6 China       20      00    213766/1280428583

table3 %>% 
  separate(year, into=c("century", "year"), sep=2, convert = T)
# A tibble: 6 × 4
#   country     century  year rate
#   <chr>         <int> <int> <chr>
# 1 Afghanistan      19    99 745/19987071
# 2 Afghanistan      20     0 2666/20595360
# 3 Brazil           19    99 37737/172006362
# 4 Brazil           20     0 80488/174504898
# 5 China            19    99 212258/1272915272
# 6 China            20     0 213766/1280428583
```

## 4. `unite` : 여러 셀의 데이터를 하나의 셀로 병합하기

```r
table5 %>%
  unite(c(century, year), col = "year")
# A tibble: 6 × 3
#   country     year  rate
#   <chr>       <chr> <chr>
# 1 Afghanistan 19_99 745/19987071
# 2 Afghanistan 20_00 2666/20595360
# 3 Brazil      19_99 37737/172006362
# 4 Brazil      20_00 80488/174504898
# 5 China       19_99 212258/1272915272
# 6 China       20_00 213766/1280428583

table5 %>%
  unite(c(century, year), col = "year", sep="")
# A tibble: 6 × 3
#   country     year  rate             
#   <chr>       <chr> <chr
# 1 Afghanistan 1999  745/19987071
# 2 Afghanistan 2000  2666/20595360
# 3 Brazil      1999  37737/172006362
# 4 Brazil      2000  80488/174504898
# 5 China       1999  212258/1272915272
# 6 China       2000  213766/1280428583
```
