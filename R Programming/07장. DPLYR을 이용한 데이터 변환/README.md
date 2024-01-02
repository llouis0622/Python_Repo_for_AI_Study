# 07. DPLYR을 이용한 데이터 변환

# 1. 정돈 데이터(Tidy Data)

## 1. 정돈 데이터 형식의 조건

- 데이터 행렬의 각 행과 관측은 일대일의 관계
- 데이터 행렬의 각 열과 변수는 일대일의 관계
- 측정값은 각 셀과 일대일의 관계
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/3a0cd617-0f69-4f88-99a6-b28bf07f4922/1.png)
    

## 2. 비정돈 데이터 형식

- 시계열 데이터
- 데이터를 매우 압축적인 방식으로 표현 가능
- 같은 시간대의 데이터를 비교하기 쉬움

## 3. 정돈 데이터를 사용하는 이유

- 표준화된 데이터 변환 작업
- 데이터 변환이나 데이터를 이용한 그래픽 작업을 데이터의 내용에 무관하게 항상 일정한 형식으로 수행 가능

# 2. `tidyverse` 패키지

- 정돈 데이터 패러다임을 따른 R 패키지를 한 번에 설치하고 적재할 수 있도록 돕는 패키지

## 1. `tidyverse` 패키지 설치

```r
install.packages("tidyverse")
```

## 2. `tidyverse` 패키지 적재

```r
library(tidyverse)
# ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
# ✔ dplyr     1.1.2     ✔ readr     2.1.4
# ✔ forcats   1.0.0     ✔ stringr   1.5.0
# ✔ ggplot2   3.4.2     ✔ tibble    3.2.1
# ✔ lubridate 1.9.2     ✔ tidyr     1.3.0
# ✔ purrr     1.0.1     
# ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
# ✖ dplyr::filter() masks stats::filter()
# ✖ dplyr::lag()    masks stats::lag()
# ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors
```

# 3. `dplyr` 패키지와 정돈 데이터의 변환

## 1. `dplyr` 패키지

- 정돈 데이터 변환 패키지

## 2. 정돈 데이터 변환의 종류

- 행 선택
    - `filter()` : 특정 열의 값이 조건에 맞는 행만 선택
    - `slice()` : 특정 위치의 행만 선택
- 행 정렬
    - `arrange()` : 특정 열의 값을 기준으로 데이터의 행 정렬
- 열 선택
    - `select()` : 열의 이름, 위치, 데이터 형식 등으로 일부 열만 데이터에서 선택
- 열 추가
    - `mutate()` : 기존 열을 사용하여 새로운 열 데이터에 추가
- 데이터 요약
    - `summarize()` : 데이터 전체 또는 특정 열을 하나의 통계량으로 요약
    - `group_by()` : 그룹 별로 데이터 통계 요약
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/309f3b92-e8ae-456b-a0e1-fcad1fd81fbb/1.png)
    

## 3. `dplyr` 패키지 vs R의 기본 기능

- 데이터 프레임의 열을 변수처럼 사용 가능
- 오직 하나의 기능만을 수행, 기능 중복 없음
- 공통된 입력과 출력 형식 사용

## 4. `mpg` 데이터

```r
mpg
# A tibble: 234 × 11
#    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
#    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
#  1 audi         a4           1.8  1999     4 auto… f        18    29 p     comp…
#  2 audi         a4           1.8  1999     4 manu… f        21    29 p     comp…
#  3 audi         a4           2    2008     4 manu… f        20    31 p     comp…
#  4 audi         a4           2    2008     4 auto… f        21    30 p     comp…
#  5 audi         a4           2.8  1999     6 auto… f        16    26 p     comp…
#  6 audi         a4           2.8  1999     6 manu… f        18    26 p     comp…
#  7 audi         a4           3.1  2008     6 auto… f        18    27 p     comp…
#  8 audi         a4 quattro   1.8  1999     4 manu… 4        18    26 p     comp…
#  9 audi         a4 quattro   1.8  1999     4 auto… 4        16    25 p     comp…
# 10 audi         a4 quattro   2    2008     4 manu… 4        20    28 p     comp…
# ℹ 224 more rows
```

# 4. `filter()` 로 행 선택하기

## 1. 선택 조건이 하나인 경우

```r
filter(데이터프레임, 조건)
```

```r
filter(mpg, manufacturer=="hyundai")
# A tibble: 14 × 11
#    manufacturer model   displ  year   cyl trans    drv     cty   hwy fl    class
#    <chr>        <chr>   <dbl> <int> <int> <chr>    <chr> <int> <int> <chr> <chr>
#  1 hyundai      sonata    2.4  1999     4 auto(l4) f        18    26 r     mids…
#  2 hyundai      sonata    2.4  1999     4 manual(… f        18    27 r     mids…
#  3 hyundai      sonata    2.4  2008     4 auto(l4) f        21    30 r     mids…
#  4 hyundai      sonata    2.4  2008     4 manual(… f        21    31 r     mids…
#  5 hyundai      sonata    2.5  1999     6 auto(l4) f        18    26 r     mids…
#  6 hyundai      sonata    2.5  1999     6 manual(… f        18    26 r     mids…
#  7 hyundai      sonata    3.3  2008     6 auto(l5) f        19    28 r     mids…
#  8 hyundai      tiburon   2    1999     4 auto(l4) f        19    26 r     subc…
# 9 hyundai      tiburon   2    1999     4 manual(… f        19    29 r     subc…
# 10 hyundai      tiburon   2    2008     4 manual(… f        20    28 r     subc…
# 11 hyundai      tiburon   2    2008     4 auto(l4) f        20    27 r     subc…
# 12 hyundai      tiburon   2.7  2008     6 auto(l4) f        17    24 r     subc…
# 13 hyundai      tiburon   2.7  2008     6 manual(… f        16    24 r     subc…
# 14 hyundai      tiburon   2.7  2008     6 manual(… f        17    24 r     subc…

filter(mpg, cty>28)
# A tibble: 3 × 11
#   manufacturer model      displ  year   cyl trans  drv     cty   hwy fl    class
#   <chr>        <chr>      <dbl> <int> <int> <chr>  <chr> <int> <int> <chr> <chr>
# 1 volkswagen   jetta        1.9  1999     4 manua… f        33    44 d     comp…
# 2 volkswagen   new beetle   1.9  1999     4 manua… f        35    44 d     subc…
# 3 volkswagen   new beetle   1.9  1999     4 auto(… f        29    41 d     subc…

filter(mpg, cty>=28)
# A tibble: 5 × 11
#   manufacturer model      displ  year   cyl trans  drv     cty   hwy fl    class
#   <chr>        <chr>      <dbl> <int> <int> <chr>  <chr> <int> <int> <chr> <chr>
# 1 honda        civic        1.6  1999     4 manua… f        28    33 r     subc…
# 2 toyota       corolla      1.8  2008     4 manua… f        28    37 r     comp…
# 3 volkswagen   jetta        1.9  1999     4 manua… f        33    44 d     comp…
# 4 volkswagen   new beetle   1.9  1999     4 manua… f        35    44 d     subc…
# 5 volkswagen   new beetle   1.9  1999     4 auto(… f        29    41 d     subc…

filter(mpg, cty * 2 > 60)
# A tibble: 2 × 11
#   manufacturer model      displ  year   cyl trans  drv     cty   hwy fl    class
#   <chr>        <chr>      <dbl> <int> <int> <chr>  <chr> <int> <int> <chr> <chr>
# 1 volkswagen   jetta        1.9  1999     4 manua… f        33    44 d     comp…
# 2 volkswagen   new beetle   1.9  1999     4 manua… f        35    44 d     subc…

filter(mpg, sqrt(cty) < 3.2)
# A tibble: 5 × 11
#   manufacturer model       displ  year   cyl trans drv     cty   hwy fl    class
#   <chr>        <chr>       <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
# 1 dodge        dakota pic…   4.7  2008     8 auto… 4         9    12 e     pick…
# 2 dodge        durango 4wd   4.7  2008     8 auto… 4         9    12 e     suv  
# 3 dodge        ram 1500 p…   4.7  2008     8 auto… 4         9    12 e     pick…
# 4 dodge        ram 1500 p…   4.7  2008     8 manu… 4         9    12 e     pick…
# 5 jeep         grand cher…   4.7  2008     8 auto… 4         9    12 e     suv
```

## 2. 여러 조건을 만족하는 행 추출하기

```r
filter(데이터프레임, 조건1, 조건2, ..., 조건n)
```

```r
filter(mpg, manufacturer=="hyundai", cty>=20)
# A tibble: 4 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 3 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 4 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…

filter(mpg, manufacturer=="hyundai", cty>=20, displ>=2.4)
# A tibble: 2 × 11
#   manufacturer model  displ  year   cyl trans      drv     cty   hwy fl    class
#   <chr>        <chr>  <dbl> <int> <int> <chr>      <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata   2.4  2008     4 auto(l4)   f        21    30 r     mids…
# 2 hyundai      sonata   2.4  2008     4 manual(m5) f        21    31 r     mids…
```

## 3. 논리 연산자로 복합 조건 만들기

```r
filter(mpg, model=="sonata" | cty>=28)
# A tibble: 12 × 11
#    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
#    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
#  1 honda        civic        1.6  1999     4 manu… f        28    33 r     subc…
#  2 hyundai      sonata       2.4  1999     4 auto… f        18    26 r     mids…
#  3 hyundai      sonata       2.4  1999     4 manu… f        18    27 r     mids…
#  4 hyundai      sonata       2.4  2008     4 auto… f        21    30 r     mids…
#  5 hyundai      sonata       2.4  2008     4 manu… f        21    31 r     mids…
#  6 hyundai      sonata       2.5  1999     6 auto… f        18    26 r     mids…
#  7 hyundai      sonata       2.5  1999     6 manu… f        18    26 r     mids…
#  8 hyundai      sonata       3.3  2008     6 auto… f        19    28 r     mids…
#  9 toyota       corolla      1.8  2008     4 manu… f        28    37 r     comp…
# 10 volkswagen   jetta        1.9  1999     4 manu… f        33    44 d     comp…
# 11 volkswagen   new beetle   1.9  1999     4 manu… f        35    44 d     subc…
# 12 volkswagen   new beetle   1.9  1999     4 auto… f        29    41 d     subc…

filter(mpg, model=="sonata" | cty>=28, year==2008)
# A tibble: 4 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 3 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 4 toyota       corolla   1.8  2008     4 manual(m… f        28    37 r     comp…

filter(mpg, (model=="sonata" | cty>=28) & year==2008)
# A tibble: 4 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 3 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 4 toyota       corolla   1.8  2008     4 manual(m… f        28    37 r     comp…

filter(mpg, model=="sonata" | cty>=28 & year==2008)
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  1999     4 auto(l4)  f        18    26 r     mids…
# 2 hyundai      sonata    2.4  1999     4 manual(m… f        18    27 r     mids…
# 3 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 4 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 5 hyundai      sonata    2.5  1999     6 auto(l4)  f        18    26 r     mids…
# 6 hyundai      sonata    2.5  1999     6 manual(m… f        18    26 r     mids…
# 7 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 8 toyota       corolla   1.8  2008     4 manual(m… f        28    37 r     comp…
```

## 4. `%in%` 연산자

```r
filter(mpg, year==2008, hwy>=28, model=="sonata" | model=="corolla" | model=="jetta")
# A tibble: 9 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 3 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 4 toyota       corolla   1.8  2008     4 manual(m… f        28    37 r     comp…
# 5 toyota       corolla   1.8  2008     4 auto(l4)  f        26    35 r     comp…
# 6 volkswagen   jetta     2    2008     4 auto(s6)  f        22    29 p     comp…
# 7 volkswagen   jetta     2    2008     4 manual(m… f        21    29 p     comp…
# 8 volkswagen   jetta     2.5  2008     5 auto(s6)  f        21    29 r     comp…
# 9 volkswagen   jetta     2.5  2008     5 manual(m… f        21    29 r     comp…

a <- 1:3
0 %in% a
# FALSE

1 %in% a
# TRUE

3 %in% a
# TRUE

4 %in% a
# FALSE

filter(mpg, year==2008, hwy>=28, model %in% c("sonata","corolla","jetta"))
# A tibble: 9 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 3 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 4 toyota       corolla   1.8  2008     4 manual(m… f        28    37 r     comp…
# 5 toyota       corolla   1.8  2008     4 auto(l4)  f        26    35 r     comp…
# 6 volkswagen   jetta     2    2008     4 auto(s6)  f        22    29 p     comp…
# 7 volkswagen   jetta     2    2008     4 manual(m… f        21    29 p     comp…
# 8 volkswagen   jetta     2.5  2008     5 auto(s6)  f        21    29 r     comp…
# 9 volkswagen   jetta     2.5  2008     5 manual(m… f        21    29 r     comp…
```

# 5. `slice()` 로 행 선택하기

```r
slice(데이터프레임, 선택위치1, 선택위치2, ...)
```

```r
a <- filter(mpg, manufacturer=="hyundai", year==2008)
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 3 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 4 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 5 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…
# 6 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 7 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 8 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…

slice(a, 1)
# A tibble: 1 × 11
#   manufacturer model  displ  year   cyl trans    drv     cty   hwy fl    class  
#   <chr>        <chr>  <dbl> <int> <int> <chr>    <chr> <int> <int> <chr> <chr>  
# 1 hyundai      sonata   2.4  2008     4 auto(l4) f        21    30 r     midsize

slice(a, 1:3)
# A tibble: 3 × 11
#   manufacturer model  displ  year   cyl trans      drv     cty   hwy fl    class
#   <chr>        <chr>  <dbl> <int> <int> <chr>      <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata   2.4  2008     4 auto(l4)   f        21    30 r     mids…
# 2 hyundai      sonata   2.4  2008     4 manual(m5) f        21    31 r     mids…
# 3 hyundai      sonata   3.3  2008     6 auto(l5)   f        19    28 r     mids…

slice(a, 1:3, 6:7)
# A tibble: 5 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 3 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 4 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 5 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…

slice(a, -1, -(4:6))
# A tibble: 4 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 2 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 3 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 4 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…
```

## 1. `slice_sample()` 로 표본 추출하기

```r
slice_sample(a, n=3)
# A tibble: 3 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 3 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…

slice_sample(a, prop=0.8)
# A tibble: 6 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 2 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…
# 3 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 4 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…
# 5 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 6 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
```

## 2. `slice_head()` 와 `slice_tail()`

```r
slice_head(mpg, n=4)
# A tibble: 4 × 11
#   manufacturer model displ  year   cyl trans      drv     cty   hwy fl    class 
#   <chr>        <chr> <dbl> <int> <int> <chr>      <chr> <int> <int> <chr> <chr> 
# 1 audi         a4      1.8  1999     4 auto(l5)   f        18    29 p     compa…
# 2 audi         a4      1.8  1999     4 manual(m5) f        21    29 p     compa…
# 3 audi         a4      2    2008     4 manual(m6) f        20    31 p     compa…
# 4 audi         a4      2    2008     4 auto(av)   f        21    30 p     compa…

slice_tail(mpg, prop=0.05)
# A tibble: 11 × 11
#    manufacturer model      displ  year   cyl trans drv     cty   hwy fl    class
#    <chr>        <chr>      <dbl> <int> <int> <chr> <chr> <int> <int> <chr> <chr>
#  1 volkswagen   new beetle   2    1999     4 manu… f        21    29 r     subc…
#  2 volkswagen   new beetle   2    1999     4 auto… f        19    26 r     subc…
#  3 volkswagen   new beetle   2.5  2008     5 manu… f        20    28 r     subc…
#  4 volkswagen   new beetle   2.5  2008     5 auto… f        20    29 r     subc…
#  5 volkswagen   passat       1.8  1999     4 manu… f        21    29 p     mids…
#  6 volkswagen   passat       1.8  1999     4 auto… f        18    29 p     mids…
#  7 volkswagen   passat       2    2008     4 auto… f        19    28 p     mids…
#  8 volkswagen   passat       2    2008     4 manu… f        21    29 p     mids…
#  9 volkswagen   passat       2.8  1999     6 auto… f        16    26 p     mids…
# 10 volkswagen   passat       2.8  1999     6 manu… f        18    26 p     mids…
# 11 volkswagen   passat       3.6  2008     6 auto… f        17    26 p     mids…
```

## 3. `slice_min()` 과 `slice_max()`

```r
slice_min(a, cty, n=2)
# A tibble: 3 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 2 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 3 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…

slice_min(a, hwy, n=2)
# A tibble: 3 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 2 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 3 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…

slice_min(a, cty, n=2, with_ties=F)
# A tibble: 2 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 2 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
```

# 6. `arrange()` 로 행 정렬하기

```r
arrange(데이터프레임, 첫번째 정렬 기준 변수, 두번째 정렬 기준 변수, ....)
```

```r
a <- filter(mpg, manufacturer=="hyundai", year==2008)
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 3 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 4 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 5 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…
# 6 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 7 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 8 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…

arrange(a, cyl)
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 3 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 4 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…
# 5 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 6 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 7 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 8 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…

arrange(a, cyl, cty)
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 2 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…
# 3 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 4 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 5 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 6 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 7 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…
# 8 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…

arrange(a, model, trans)
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 2 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 3 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 4 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…
# 5 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 6 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 7 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…
# 8 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
```

## 1. `desc()` 를 이용하여 내림차순으로 정렬하기

```r
arrange(a, desc(cyl))
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 2 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 3 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 4 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…
# 5 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 6 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 7 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 8 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…

arrange(a, desc(cyl), cty)
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 2 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
# 3 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…
# 4 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 5 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 6 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…
# 7 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 8 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…

arrange(a, model, desc(trans))
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans     drv     cty   hwy fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <int> <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 manual(m… f        21    31 r     mids…
# 2 hyundai      sonata    3.3  2008     6 auto(l5)  f        19    28 r     mids…
# 3 hyundai      sonata    2.4  2008     4 auto(l4)  f        21    30 r     mids…
# 4 hyundai      tiburon   2.7  2008     6 manual(m… f        16    24 r     subc…
# 5 hyundai      tiburon   2    2008     4 manual(m… f        20    28 r     subc…
# 6 hyundai      tiburon   2.7  2008     6 manual(m… f        17    24 r     subc…
# 7 hyundai      tiburon   2    2008     4 auto(l4)  f        20    27 r     subc…
# 8 hyundai      tiburon   2.7  2008     6 auto(l4)  f        17    24 r     subc…
```

# 7. `select()` 를 이용하여 변수 이름으로 열 선택하기

## 1. 변수 이름을 나열하여 선택하기

```r
select(데이터프레임, 변수이름1, 변수이름 2, ....)
```

```r
select(a, model, year, cty, hwy)
# A tibble: 8 × 4
#   model    year   cty   hwy
#   <chr>   <int> <int> <int>
# 1 sonata   2008    21    30
# 2 sonata   2008    21    31
# 3 sonata   2008    19    28
# 4 tiburon  2008    20    28
# 5 tiburon  2008    20    27
# 6 tiburon  2008    17    24
# 7 tiburon  2008    16    24
# 8 tiburon  2008    17    24
```

## 2. 변수 이름으로 변수 범위를 선택하기

```r
select(데이터프레임, 범위시작_변수이름:범위종료_변수이름, ...)
```

```r
select(a, model:trans)
# A tibble: 8 × 5
#   model   displ  year   cyl trans     
#   <chr>   <dbl> <int> <int> <chr>     
# 1 sonata    2.4  2008     4 auto(l4)  
# 2 sonata    2.4  2008     4 manual(m5)
# 3 sonata    3.3  2008     6 auto(l5)  
# 4 tiburon   2    2008     4 manual(m5)
# 5 tiburon   2    2008     4 auto(l4)  
# 6 tiburon   2.7  2008     6 auto(l4)  
# 7 tiburon   2.7  2008     6 manual(m6)
# 8 tiburon   2.7  2008     6 manual(m5)

select(a, model:trans, cty:hwy)
# A tibble: 8 × 7
#   model   displ  year   cyl trans        cty   hwy
#   <chr>   <dbl> <int> <int> <chr>      <int> <int>
# 1 sonata    2.4  2008     4 auto(l4)      21    30
# 2 sonata    2.4  2008     4 manual(m5)    21    31
# 3 sonata    3.3  2008     6 auto(l5)      19    28
# 4 tiburon   2    2008     4 manual(m5)    20    28
# 5 tiburon   2    2008     4 auto(l4)      20    27
# 6 tiburon   2.7  2008     6 auto(l4)      17    24
# 7 tiburon   2.7  2008     6 manual(m6)    16    24
# 8 tiburon   2.7  2008     6 manual(m5)    17    24
```

```r
select(데이터프레임, -(범위시작_변수이름:범위종료_변수이름), ...)
```

```r
select(a, -(model:trans))
# A tibble: 8 × 6
#   manufacturer drv     cty   hwy fl    class     
#   <chr>        <chr> <int> <int> <chr> <chr>     
# 1 hyundai      f        21    30 r     midsize   
# 2 hyundai      f        21    31 r     midsize   
# 3 hyundai      f        19    28 r     midsize   
# 4 hyundai      f        20    28 r     subcompact
# 5 hyundai      f        20    27 r     subcompact
# 6 hyundai      f        17    24 r     subcompact
# 7 hyundai      f        16    24 r     subcompact
# 8 hyundai      f        17    24 r     subcompact

select(a, -(model:trans), -manufacturer)
# A tibble: 8 × 5
#   drv     cty   hwy fl    class     
#   <chr> <int> <int> <chr> <chr>     
# 1 f        21    30 r     midsize   
# 2 f        21    31 r     midsize   
# 3 f        19    28 r     midsize   
# 4 f        20    28 r     subcompact
# 5 f        20    27 r     subcompact
# 6 f        17    24 r     subcompact
# 7 f        16    24 r     subcompact
# 8 f        17    24 r     subcompact
```

## 3. 변수 위치로 매칭하여 선택하기

```r
select(a, 1:3)
# A tibble: 8 × 3
#   manufacturer model   displ
#   <chr>        <chr>   <dbl>
# 1 hyundai      sonata    2.4
# 2 hyundai      sonata    2.4
# 3 hyundai      sonata    3.3
# 4 hyundai      tiburon   2  
# 5 hyundai      tiburon   2  
# 6 hyundai      tiburon   2.7
# 7 hyundai      tiburon   2.7
# 8 hyundai      tiburon   2.7

select(a, 1:3, 5)
# A tibble: 8 × 4
#   manufacturer model   displ   cyl
#   <chr>        <chr>   <dbl> <int>
# 1 hyundai      sonata    2.4     4
# 2 hyundai      sonata    2.4     4
# 3 hyundai      sonata    3.3     6
# 4 hyundai      tiburon   2       4
# 5 hyundai      tiburon   2       4
# 6 hyundai      tiburon   2.7     6
# 7 hyundai      tiburon   2.7     6
# 8 hyundai      tiburon   2.7     6

select(a, -(4:10))
# A tibble: 8 × 4
#   manufacturer model   displ class     
#   <chr>        <chr>   <dbl> <chr>     
# 1 hyundai      sonata    2.4 midsize   
# 2 hyundai      sonata    2.4 midsize   
# 3 hyundai      sonata    3.3 midsize   
# 4 hyundai      tiburon   2   subcompact
# 5 hyundai      tiburon   2   subcompact
# 6 hyundai      tiburon   2.7 subcompact
# 7 hyundai      tiburon   2.7 subcompact
# 8 hyundai      tiburon   2.7 subcompact
```

## 4. 변수 이름을 매칭하여 선택하기

- `starts_with("abc")` : abc로 이름이 시작하는 모든 변수
- `ends_with("abc")` : abc로 이름이 끝나는 모든 변수
- `contains("abc")` : abc를 이름에 포함하고 있는 모든 변수
- `matches("(.)\\1")` : 정규 표현식을 만족하는 이름을 가진 모든 변수
- `num_range("x", 1:3)` : “x1”, “x2”, “x3”이라는 이름의 변수
    
    ```r
    select(a, starts_with("c"))
    # A tibble: 8 × 3
    #     cyl   cty class     
    #   <int> <int> <chr>     
    # 1     4    21 midsize   
    # 2     4    21 midsize   
    # 3     6    19 midsize   
    # 4     4    20 subcompact
    # 5     4    20 subcompact
    # 6     6    17 subcompact
    # 7     6    16 subcompact
    # 8     6    17 subcompact
    ```
    

## 5. 변수의 형식이나 조건으로 매칭하여 선택하기

```r
select(a, where(is.character))
# A tibble: 8 × 6
#   manufacturer model   trans      drv   fl    class     
#   <chr>        <chr>   <chr>      <chr> <chr> <chr>     
# 1 hyundai      sonata  auto(l4)   f     r     midsize   
# 2 hyundai      sonata  manual(m5) f     r     midsize   
# 3 hyundai      sonata  auto(l5)   f     r     midsize   
# 4 hyundai      tiburon manual(m5) f     r     subcompact
# 5 hyundai      tiburon auto(l4)   f     r     subcompact
# 6 hyundai      tiburon auto(l4)   f     r     subcompact
# 7 hyundai      tiburon manual(m6) f     r     subcompact
# 8 hyundai      tiburon manual(m5) f     r     subcompact

select(a, where(function(x) is.numeric(x) && mean(x)>=10))
# A tibble: 8 × 3
#    year   cty   hwy
#   <int> <int> <int>
# 1  2008    21    30
# 2  2008    21    31
# 3  2008    19    28
# 4  2008    20    28
# 5  2008    20    27
# 6  2008    17    24
# 7  2008    16    24
# 8  2008    17    24

select(a, where(~ is.numeric(.x) && mean(.x)<10))
# A tibble: 8 × 2
#   displ   cyl
#   <dbl> <int>
# 1   2.4     4
# 2   2.4     4
# 3   3.3     6
# 4   2       4
# 5   2       4
# 6   2.7     6
# 7   2.7     6
# 8   2.7     6
```

## 6. 변수 이름 바꾸기

```r
select(a, model, city=cty, highway=hwy)
# A tibble: 8 × 3
#   model    city highway
#   <chr>   <int>   <int>
# 1 sonata     21      30
# 2 sonata     21      31
# 3 sonata     19      28
# 4 tiburon    20      28
# 5 tiburon    20      27
# 6 tiburon    17      24
# 7 tiburon    16      24
# 8 tiburon    17      24

rename(a, city=cty, highway=hwy)
# A tibble: 8 × 11
#   manufacturer model   displ  year   cyl trans   drv    city highway fl    class
#   <chr>        <chr>   <dbl> <int> <int> <chr>   <chr> <int>   <int> <chr> <chr>
# 1 hyundai      sonata    2.4  2008     4 auto(l… f        21      30 r     mids…
# 2 hyundai      sonata    2.4  2008     4 manual… f        21      31 r     mids…
# 3 hyundai      sonata    3.3  2008     6 auto(l… f        19      28 r     mids…
# 4 hyundai      tiburon   2    2008     4 manual… f        20      28 r     subc…
# 5 hyundai      tiburon   2    2008     4 auto(l… f        20      27 r     subc…
# 6 hyundai      tiburon   2.7  2008     6 auto(l… f        17      24 r     subc…
# 7 hyundai      tiburon   2.7  2008     6 manual… f        16      24 r     subc…
# 8 hyundai      tiburon   2.7  2008     6 manual… f        17      24 r     subc…
```

## 7. 변수 순서 바꾸기

```r
select(a, cty, hwy)
# A tibble: 8 × 2
#     cty   hwy
#   <int> <int>
# 1    21    30
# 2    21    31
# 3    19    28
# 4    20    28
# 5    20    27
# 6    17    24
# 7    16    24
# 8    17    24

select(a, hwy, cty)
# A tibble: 8 × 2
#     hwy   cty
#   <int> <int>
# 1    30    21
# 2    31    21
# 3    28    19
# 4    28    20
# 5    27    20
# 6    24    17
# 7    24    16
# 8    24    17

select(a, cty, hwy, everything())
# A tibble: 8 × 11
#     cty   hwy manufacturer model   displ  year   cyl trans     drv   fl    class
#   <int> <int> <chr>        <chr>   <dbl> <int> <int> <chr>     <chr> <chr> <chr>
# 1    21    30 hyundai      sonata    2.4  2008     4 auto(l4)  f     r     mids…
# 2    21    31 hyundai      sonata    2.4  2008     4 manual(m… f     r     mids…
# 3    19    28 hyundai      sonata    3.3  2008     6 auto(l5)  f     r     mids…
# 4    20    28 hyundai      tiburon   2    2008     4 manual(m… f     r     subc…
# 5    20    27 hyundai      tiburon   2    2008     4 auto(l4)  f     r     subc…
# 6    17    24 hyundai      tiburon   2.7  2008     6 auto(l4)  f     r     subc…
# 7    16    24 hyundai      tiburon   2.7  2008     6 manual(m… f     r     subc…
# 8    17    24 hyundai      tiburon   2.7  2008     6 manual(m… f     r     subc…
```
