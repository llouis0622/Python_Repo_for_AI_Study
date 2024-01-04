# 08. GGPlot2 시작하기

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

# 1. ggplot2 시작하기

## 1. ggplot2 그래프 그려보기

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/d273b562-6987-4550-b8ac-717a32b1f6a2/1.png)

# 2. 도형의 속성에 데이터 열을 대응시키기(Aesthetic Mapping)

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/b155f049-4ed0-4b6f-aef6-d63087a03721/1.png)

## 1. 범주형 변수를 색상 속성에 매핑하기

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy, color=class), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/2cf4d617-dea8-4dcf-887e-a2e5a6765891/1.png)

## 2. 범주형 변수를 모양 속성에 매핑하기

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy, shape=drv), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/4ef0f922-3cbc-409e-8cdf-fa43973c9478/1.png)

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy, shape=class), data=mpg)
# Warning: The shape palette can deal with a maximum of 6 discrete values because
# more than 6 becomes difficult to discriminate; you have 7. Consider
# specifying shapes manually if you must have them.
# Warning: Removed 62 rows containing missing values (`geom_point()`).
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6c737c91-83c8-47cc-b5ee-841934cec1d5/1.png)

## 3. 연속형 변수를 크기, 투명도, 색상 속성에 매핑하기

```r
ggplot() + geom_point(mapping=aes(x=cty, y=hwy, size=displ), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/0ec77adc-a46a-4296-9ae1-055e0931f2e0/1.png)

```r
ggplot() + geom_point(mapping=aes(x=cty, y=hwy, color=displ), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6fcd047e-899c-4053-b1d5-157ce5065d40/1.png)

```r
ggplot() + geom_point(mapping=aes(x=cty, y=hwy, alpha=cyl), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/48fa1d68-d0af-45b6-b26d-be1e03b4a0ba/1.png)

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy, size=class), data=mpg)
# Warning: Using size for a discrete variable is not advised.
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/d18ff4b6-643b-4cec-8526-6cd347126a8e/1.png)

## 4. 도형의 여러 속성에 데이터 열을 매핑시키기

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy, color=drv, shape=drv), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/365f15ca-e164-4a86-9213-104d2c0c95bc/1.png)

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy, color=class, shape=drv), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/a7322706-e4e8-47f2-8fcb-10708b7cd19e/1.png)

## 5. 도형 속성에 데이터 열을 매핑하기 - 예제

```r
ggplot() + geom_point(mapping=aes(x=cty, y=hwy, color=drv, shape=drv), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6934e36c-ed76-41bd-89dd-1741fc06ac02/1.png)

```r
head(iris)
#   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
# 1          5.1         3.5          1.4         0.2  setosa
# 2          4.9         3.0          1.4         0.2  setosa
# 3          4.7         3.2          1.3         0.2  setosa
# 4          4.6         3.1          1.5         0.2  setosa
# 5          5.0         3.6          1.4         0.2  setosa
# 6          5.4         3.9          1.7         0.4  setosa

ggplot() + geom_point(mapping=aes(x=Sepal.Length, y=Sepal.Width, color=Species, shape=Species), data=iris)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/1f206dab-8f3d-4882-8a02-6f9c1c569980/1.png)

## 6. 도형의 속성에 대응시키기 vs 도형의 속성 인수를 설정하기

### 1. 도형의 속성 인수 설정하기

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy), data=mpg, color="blue")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/4e2cf10c-1c9e-491c-8d27-56abc50f231a/1.png)

### 2. 도형의 속성 인수를 속성 대응시키기에 잘못 설정하는 경우

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy, color="blue"), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/981edb74-3afa-41d3-b433-f09c41f7d979/1.png)

## 7. `group` 속성

- 도형의 시각적 표현을 직접적으로 변형하는 것이 아닌 도형을 그릴 때 데이터를 어떤 식으로 그룹으로 묶어 사용할지만 지정

## 8. 그룹으로 나누어 선 그래프 그리기

```r
Orange
#    Tree  age circumference
# 1     1  118            30
# 2     1  484            58
# 3     1  664            87
# 4     1 1004           115
# 5     1 1231           120
# 6     1 1372           142
# 7     1 1582           145
# 8     2  118            33
# 9     2  484            69
# 10    2  664           111
# 11    2 1004           156
# ......
```

```r
ggplot() + geom_point(mapping=aes(x=age, y=circumference), data=Orange)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/af000c6a-9cf9-44b2-8312-99c460fefc90/1.png)

```r
ggplot() + geom_line(mapping=aes(x=age, y=circumference), data=Orange)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/41c4b55c-ef35-45fd-bd85-a1728844cebf/1.png)

```r
ggplot() + geom_line(mapping=aes(x=age, y=circumference, group=Tree), data=Orange)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/7a70429a-1ebc-44b7-99dc-2ac4faa1956b/1.png)

## 9. 이산형 변수는 `group` 속성으로 자동 매핑

```r
Orange$Tree
# 1 1 1 1 1 1 1 2 2 2 2 2 2 2 3 3 3 3 3 3 3 4 4 4 4 4 4 4 5 5 5 5 5 5 5
# Levels: 3 < 1 < 5 < 2 < 4
```

```r
ggplot() + geom_line(mapping=aes(x=age, y=circumference, group=Tree, color=Tree), data=Orange)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/79c4f057-77c1-4e0e-bf4f-445690fee690/1.png)

```r
ggplot() + geom_line(mapping=aes(x=age, y=circumference, color=Tree), data=Orange)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/f7f2de35-c7ab-445a-a95e-a3ca6018c1ae/1.png)

```r
ggplot() + geom_line(mapping=aes(x=age, y=circumference, linetype=Tree), data=Orange)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/26e57bcf-824d-4556-9b37-a8d1727255bc/1.png)

## 10. `geom_smooth()` 함수에서 `group` 속성

```r
ggplot() + geom_smooth(mapping=aes(x=age, y=circumference), data=Orange)
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/18401470-4911-47e7-b396-56d7f0cb70b9/1.png)

```r
ggplot() + geom_smooth(mapping=aes(x=age, y=circumference, color=Tree), data=Orange)
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/8c789372-e8da-47f7-9d18-0a485892a571/1.png)

```r
ggplot() + geom_smooth(mapping=aes(x=age, y=circumference, color=Tree), data=Orange, se=F)
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/c0f9ee0d-b6dd-4d96-b28f-aa720fe9ec08/1.png)

# 3. 측면(Facets)으로 나누어 그리기

## 1. `facet_wrap()` 로 일차원 측면 그래프 그리기

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy), data=mpg) +facet_wrap(~class, nrow=2)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/cc0ac190-47c3-497c-baa1-88309ef97a70/1.png)

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy), data=mpg) + facet_wrap(~drv + year, nrow=2)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/3f98542e-b21f-466a-a32f-2b3b860edc2b/1.png)

## 2. `facet_grid()` 로 이차원 측면 그래프 그리기

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy), data=mpg) + facet_grid(drv~cyl)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ff0ffe69-45ee-4887-956e-c4ab0cfac43d/1.png)

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy), data=mpg) + facet_grid(drv+year~cyl)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/1ac20c05-709c-4b70-b69c-7ef9575945c7/1.png)

# 4. 그래프 계층(Layers)과 도형(Geoms)

## 1. `geom` 함수의 순서와 그래프 계층

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy), data=mpg)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/aae54710-8631-4d9e-900f-c20a04bada5c/1.png)

```r
ggplot() + geom_smooth(mapping=aes(x=displ, y=hwy), data=mpg)
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/d1088027-5c0e-44b4-8409-88fabcd1822f/1.png)

```r
ggplot() + geom_point(mapping=aes(x=displ, y=hwy), data=mpg) + geom_smooth(mapping=aes(x=displ, y=hwy), data=mpg)
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/140c28eb-e149-4c25-8c1b-f914056aa198/1.png)

## 2. `ggplot()` 함수는 좌표축을 자동 조정함

```r
ggplot() + 
  geom_point(mapping=aes(x=displ, y=hwy), data=mpg) +
  geom_smooth(mapping=aes(x=displ, y=hwy), data=mpg) + 
  geom_point(mapping=aes(x=displ, y=cty), data=mpg, col="red", shape=1) +
  geom_smooth(mapping=aes(x=displ, y=cty), data=mpg, linetype=2, col="red")
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/f76ed66e-115d-4000-8787-a94246046845/1.png)

## 3. 여러 데이터를 사용하여 그래프 계층 만들기

```r
head(iris)
#   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
# 1          5.1         3.5          1.4         0.2  setosa
# 2          4.9         3.0          1.4         0.2  setosa
# 3          4.7         3.2          1.3         0.2  setosa
# 4          4.6         3.1          1.5         0.2  setosa
# 5          5.0         3.6          1.4         0.2  setosa
# 6          5.4         3.9          1.7         0.4  setosa

ggplot() + 
  geom_point(mapping=aes(x=displ, y=hwy), data=mpg) +
  geom_smooth(mapping=aes(x=displ, y=hwy), data=mpg) + 
  geom_point(mapping=aes(x=displ, y=cty), data=mpg, col="red", shape=1) +
  geom_smooth(mapping=aes(x=displ, y=cty), data=mpg, linetype=2, col="red") +
  geom_point(mapping=aes(x=Sepal.Length, y=Sepal.Width), data=iris, col="orange") 
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/524ae764-a4e6-4090-bf54-a44a70bff828/1.png)

## 4. 다른 데이터 범위로 그래프 계층 만들기

```r
ggplot() +
  geom_point(mapping=aes(displ, hwy), data=mpg) +
  geom_point(mapping=aes(displ, hwy), 
             data=filter(mpg, displ>5, hwy>20), 
             color="red", size=2)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/276c1c90-0699-43a4-a2d6-95f4d68ea881/1.png)

## 5. 공통 `data` 와 `mapping` 의 설정

### 1. `ggplot` 함수에 공통 데이터와 매핑 설정하기

```r
ggplot(data=mpg, mapping=aes(x=displ, y=hwy)) +
  geom_point() + geom_smooth()
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/5b5a3045-cc94-4fd2-8ce6-1c2624d1116a/1.png)

```r
ggplot(data=mpg, mapping=aes(x=displ, y=cty)) +
  geom_point() + geom_smooth()
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/1ad21ff7-40c6-4fdf-bf68-59500669f2a5/1.png)

### 2. `geom` 함수에서 데이터와 매핑의 재정의

```r
ggplot(data=mpg, mapping=aes(x=displ, y=hwy, color=drv)) +
  geom_point() + geom_smooth()
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/8838782c-bc56-40b4-b037-88102eed78b1/1.png)

```r
ggplot(data=mpg, mapping=aes(x=displ, y=hwy)) +
  geom_point(mapping=aes(color=drv)) + geom_smooth()
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/f8892e88-7dcf-4fa2-b246-eb13bb826ee5/1.png)

```r
ggplot(data=mpg, mapping=aes(x=displ, y=hwy)) +
  geom_point() + geom_smooth(mapping=aes(color=drv))
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/7bc5d5d2-90ff-4b0f-9205-3b0950c49b1f/1.png)

```r
ggplot(data=mpg, mapping=aes(x=displ, y=hwy, color=drv)) + 
  geom_point(mapping=aes(shape=drv)) + 
  geom_smooth(mapping=aes(linetype=drv))
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/e33f0e19-76ec-4c6e-a053-1e194827bfff/1.png)

```r
ggplot(data=mpg, mapping=aes(x=displ, y=hwy)) + 
  geom_point() + geom_smooth() + 
  geom_point(mapping=aes(y=cty), col="red", shape=1) + 
  geom_smooth(mapping=aes(y=cty), linetype=2, col="red")
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/199e6d75-fb63-43e6-844b-c0738d04ca14/1.png)

```r
ggplot(data=mpg, mapping=aes(x=displ, y=hwy)) + 
  geom_point(aes(color=class)) + 
  geom_smooth(data=filter(mpg, class=="suv"))
# `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/a3c021f0-532a-4264-a20a-84dab9920d7b/1.png)

### 3. `ggplot()` 과 `geom` 함수에서 대표 인수의 이름을 생략하기

```r
ggplot(mpg, aes(displ, hwy)) + 
  geom_point() + geom_smooth() + 
  geom_point(aes(y=cty), col="red", shape=1) +
  geom_smooth(aes(y=cty), linetype=2, col="red")
```

# 5. `ggplot` 명령문을 입력할 때 자주 발생하는 문제들

- 대소문자 구분
- 명령문의 키워드 철자 오류
- `()` 와 `""` 의 짝 맞추기
- `+` 뒤에서 줄바꿈하기
    
    ```r
    ggplot(mpg, aes(x=displ, y=hwy, color=drv)) + geom_point() + geom_smooth()
    # `geom_smooth()` using method = 'loess' and formula = 'y ~ x'
    ```
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/19275dc1-568c-449f-958d-729e017b55ab/1.png)
    
    ```r
    ggplot(mpg, aes(x=displ, y=hwy, color=drv)) + 
      geom_point() + 
      geom_smooth()
    ```
    
    ```r
    ggplot(mpg, aes(x=displ, y=hwy, color=drv))  
      + geom_point()  
    # Error:
    # ! Cannot use `+` with a single argument
    # ℹ Did you accidentally put `+` on a new line?
    ```
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/0cb66312-ae69-4542-af19-6fa6e2df61d1/1.png)
    

# 6. 통계 변환

## 1. 범주형 변수의 통계 요약

```r
diamonds
# A tibble: 53,940 × 10
#    carat cut       color clarity depth table price     x     y     z
#    <dbl> <ord>     <ord> <ord>   <dbl> <dbl> <int> <dbl> <dbl> <dbl>
#  1  0.23 Ideal     E     SI2      61.5    55   326  3.95  3.98  2.43
#  2  0.21 Premium   E     SI1      59.8    61   326  3.89  3.84  2.31
#  3  0.23 Good      E     VS1      56.9    65   327  4.05  4.07  2.31
#  4  0.29 Premium   I     VS2      62.4    58   334  4.2   4.23  2.63
#  5  0.31 Good      J     SI2      63.3    58   335  4.34  4.35  2.75
#  6  0.24 Very Good J     VVS2     62.8    57   336  3.94  3.96  2.48
#  7  0.24 Very Good I     VVS1     62.3    57   336  3.95  3.98  2.47
#  8  0.26 Very Good H     SI1      61.9    55   337  4.07  4.11  2.53
#  9  0.22 Fair      E     VS2      65.1    61   337  3.87  3.78  2.49
# 10  0.23 Very Good H     VS1      59.4    61   338  4     4.05  2.39
# ℹ 53,930 more rows

cut_table <- diamonds %>% 
  group_by(cut) %>%
  summarize(n=n())
# A tibble: 5 × 2
#   cut           n
#   <ord>     <int>
# 1 Fair       1610
# 2 Good       4906
# 3 Very Good 12082
# 4 Premium   13791
# 5 Ideal     21551
```

```r
ggplot(cut_table) + geom_col(aes(x=cut, y=n))
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/d439f37c-beba-45b1-a093-2f86f125098a/1.png)

```r
ggplot(diamonds) + geom_bar(aes(x=cut), stat="count")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/f2caf093-bf99-4cf3-978f-a5e373e37447/1.png)

```r
ggplot(diamonds) + geom_bar(aes(x=color))
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/12e75771-a977-4342-b7ee-6e1eb89459d7/1.png)

```r
ggplot(diamonds) + geom_bar(aes(clarity, after_stat(prop), group=1))
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/4068e4ae-582f-4131-9633-07ff0d029642/1.png)

## 2. 수치형 변수의 통계 요약

```r
ggplot(diamonds) + geom_bar(aes(carat))
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/444d8901-a203-4ccd-be85-45e0cd19fac1/1.png)

### 1. `stat_bin()` 을 이용한 히스토그램

```r
ggplot(diamonds) + geom_bar(aes(carat), stat="bin")
# `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/738552d6-7818-4051-847d-1923a0983bef/1.png)

### 2. `geom_histogram()`

```r
ggplot(diamonds) + geom_histogram(aes(carat))
# `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/0b271ab7-fd5c-47cc-8286-cd48b95512dc/1.png)

```r
ggplot(diamonds) + geom_histogram(aes(table), bins=50)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/5c572afb-3c54-456b-8976-a0be9d3cb780/1.png)

```r
ggplot(diamonds) + geom_histogram(aes(price), binwidth=500)
```

[]()

```r
ggplot(diamonds) + geom_histogram(aes(x=x, y=after_stat(density)))
# `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/09e56235-7cb8-4849-8e1b-63745d680119/1.png)

```r
ggplot(diamonds) + geom_histogram(aes(x=y, y=after_stat(ncount)))
# `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/8ce7a7f4-fa98-4c52-bac7-a6c762f11c86/1.png)

```r
ggplot(diamonds) + geom_histogram(aes(x=z, y=after_stat(ndensity)))
# `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ab42a746-6f4e-46e5-b5a9-5fff260425bd/1.png)

### 3. `geom_boxplot()`

```r
ggplot(diamonds) + geom_boxplot(aes(y = carat))
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/aa676ed9-38c1-404c-98a3-875844d9d4db/1.png)

```r
ggplot(diamonds) + geom_boxplot(aes(x = carat))
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/9b88eb83-852c-48a6-b1f0-6e6992c14e86/1.png)

## 3. 수치형 변수의 범주별 통계요약

```r
ggplot(diamonds) + geom_boxplot(aes(cut, price))
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/be55646d-8483-46d1-97cc-d07c813245c5/1.png)

```r
ggplot(diamonds) + geom_boxplot(aes(cut, carat), notch=T)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/2957704c-f63b-4012-8d12-daee23402c58/1.png)

```r
ggplot(diamonds, aes(cut, depth)) +
  stat_summary(fun=median, fun.max=max, fun.min=min)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/556fc1d3-426f-41a3-b010-cc6602b0bbec/1.png)

# 7. 위치 조정

```r
ggplot(mpg) + geom_bar(aes(class), fill="dark blue")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/df2e27c4-ef96-4d00-854f-23c2285b5ee0/1.png)

```r
ggplot(mpg) + geom_bar(aes(class), color="dark blue")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/de79c4b6-95f9-4d7b-97a0-058874672b84/1.png)

```r
ggplot(mpg) + geom_bar(aes(class, fill=drv))
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/dfc9fd89-cbf4-4771-82ea-590e70fd168f/1.png)

```r
ggplot(mpg) + geom_bar(aes(class, fill=drv), position="dodge")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/467c758b-0f30-4169-8f6a-58f56f8c46b3/1.png)

```r
ggplot(mpg) + geom_bar(aes(class, fill=drv), position="fill")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/114baa03-c1de-4322-809c-3a616e718b44/1.png)

```r
ggplot(mpg) + geom_bar(aes(class, col=drv), position="identity", alpha=0.1)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/28605e09-7f3f-4f03-8d80-0a6e353a4ff6/1.png)

```r
ggplot(mpg) + geom_freqpoly(aes(hwy, color=drv), position="identity")
# `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6f51f117-6e08-4b39-8473-837eb9680b82/1.png)

```r
ggplot(mpg) + geom_freqpoly(aes(hwy, color=drv))
```

# 8. `ggplot2` 그래프의 종류

- `geom_bar()` : Bar Chart, color, fill, alpha
- `geom_boxplot()` : Box Plot, color, fill, alpha, notch, width
- `geom_density()` : Density Plot, color, fill, alpha, linetype
- `geom_histogram()` : Histogram, color, fill, alpha, linetype, binwidth
- `geom_hline()` : Horizontal Lines, color, alpha, linetype, size
- `geom_jitter()` : Jittered Points, color, size, alpha, shape
- `geom_line()` : Line Graph, color, alpha, linetype, size
- `geom_point()` : Scatterplot, color, alpha, shape, size
- `geom_rug()` : Rug Plot, color, side
- `geom_smooth()` : Fitted Line, method, formula, color, fill, linetype, size
- `geom_text()` : Text Annoations, 많은 옵션이 있으므로 도움말 참조
- `geom_violin()` : Violin Plot, color, fill, alpha, linetype
- `geom_vline()` : Vertical Lines, color, alpha, linetype, size

## 1. 직선을 그리는 그래픽 함수

```r
p <- ggplot(mpg, aes(cty, hwy)) + geom_point()
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/542a5166-5909-411a-bd7b-f7b90bcdb09b/1.png)

```r
p + geom_vline(xintercept = mean(mpg$cty), linetype=2, color="red")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/fb2afc01-c76c-4a8a-ba72-74fed99ad8e2/1.png)

```r
p1 <- p + geom_vline(xintercept = mean(mpg$cty), linetype=2, color="red") +
  geom_hline(yintercept = mean(mpg$hwy), linetype=2, color="red")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/7d680da6-09f8-4cb0-ba05-82d0fa868e8f/1.png)

```r
p1 + geom_abline(a=0, b=1, linetype=3, color="blue") +
  scale_x_continuous(limits = c(0, 45)) +
  scale_y_continuous(limits = c(0, 45))
# Warning in geom_abline(a = 0, b = 1, linetype = 3, color = "blue"): Ignoring unknown parameters: `a` and `b`
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/2b6a85d7-beee-4edb-94d1-a040061ae85e/1.png)

## 2. 한 범주형 변수의 그래프

```r
unique(mpg$class)
# [1] "compact"    "midsize"    "suv"        "2seater"    "minivan"   
# [6] "pickup"     "subcompact"
```

```r
ggplot(data=데이터, mapping=aes(x=범주형.변수.이름)) + geom_bar()
ggplot(데이터, aes(범주형.변수.이름)) + geom_bar()
ggplot(데이터) + geom_bar(aes(범주형.변수.이름))
ggplot() + geom_bar(aes(범주형.변수.이름), 데이터)
```

```r
ggplot(mpg, aes(class)) + geom_bar()
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/3daf8af5-530b-4952-a2e7-a88b7923dccc/1.png)

```r
ggplot(mpg, aes(cyl)) + geom_bar()
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ec536f88-b3fa-4ced-a562-1ed37cd96fb1/1.png)

```r
unique(mpg$cty)
# 18 21 20 16 19 15 17 14 11 13 12 22  9 28 24 25 23 26 33 35 29
```

```r
ggplot(mpg, aes(cty)) + geom_bar()
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/c0775d1f-9eb5-4c02-9d30-1a3411fa7dad/1.png)

```r
ggplot(mpg, aes(drv)) + geom_bar()
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/9ad40c05-0d7a-41e7-884b-4ebf12f11faa/1.png)

```r
ggplot(mpg, aes(factor(drv, levels=c("f", "r", "4")))) + 
  geom_bar() +
  labs(x="drv")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/bc8afb3b-fc30-4682-8260-737069bd643f/1.png)

```r
ggplot(mpg) + 
  geom_bar(aes(reorder(class, class, length))) +
  labs(x="class")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/fc77ee58-dd7b-4c92-b3cb-89a6192818b8/1.png)

```r
ggplot(mpg) + 
  geom_bar(aes(reorder(class, class, function(x) -length(x))))+
  labs(x="class")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/e675151c-656c-4ad7-8ad0-27cc7ce19052/1.png)

```r
ggplot(mpg) + 
  geom_bar(aes(reorder(class, hwy, mean))) +
  labs(x="class")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/88e554ed-fe6f-4353-964b-e6cf47551354/1.png)

```r
mpg %>%
  group_by(class) %>%
  summarise(hwy_mean = mean(hwy)) %>%
  arrange(hwy_mean)
# A tibble: 7 × 2
#   class      hwy_mean
#   <chr>         <dbl>
# 1 pickup         16.9
# 2 suv            18.1
# 3 minivan        22.4
# 4 2seater        24.8
# 5 midsize        27.3
# 6 subcompact     28.1
# 7 compact        28.3
```

```r
ggplot(mpg, aes(class, fill=factor(year))) + geom_bar() + labs(fill="year")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/71fbe3d0-26b1-4db5-8117-93c4084a1573/1.png)

```r
ggplot(mpg, aes(class, fill=factor(year))) +
  geom_bar(position="fill") + labs(fill="year")
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/3dc4fe42-65ee-4df0-aaba-ad58df204054/1.png)

## 3. 한 수치형 변수의 그래프

```r
ggplot(mpg, aes(hwy)) + geom_histogram(binwidth=2)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/679ba2d4-d329-4285-8c42-efa9845dc07c/1.png)

```r
ggplot(mpg, aes(hwy)) + geom_histogram(binwidth=1)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6ef73dfa-9b30-4777-be12-e93a5c486af0/1.png)

```r
ggplot(mpg, aes(hwy, fill=drv)) + geom_histogram(binwidth=1)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/f5b2a266-cc07-4ee0-9537-180abe9be648/1.png)

```r
ggplot(mpg, aes(hwy)) + geom_freqpoly(binwidth=2)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/b9ba45a5-58cb-4d4c-a556-37c6de2bead0/1.png)

```r
ggplot(mpg, aes(hwy, color=drv)) + geom_freqpoly(binwidth=2)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/0938a90e-fc87-42aa-a5f5-9bef08dbcbaa/1.png)

```r
ggplot(mpg, aes(hwy, after_stat(density), color=drv)) + geom_freqpoly(binwidth=2)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/59708343-267b-43f8-a669-fec4c369fcbd/1.png)

```r
ggplot(mpg, aes(hwy)) + geom_density()
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/00e359e8-fdbf-4bdb-85d8-ab9402605525/1.png)

```r
ggplot(mpg, aes(hwy, color=drv)) + geom_density()
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/f85f42fe-57e9-4a26-acfa-634d62e83b1b/1.png)

## 4. 두 범주형 변수의 그래프

```r
ggplot(mpg, aes(class)) + geom_bar() +
  facet_wrap(~drv)
```

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/be916ca0-5da0-4531-ab3a-bcca13e37bea/1.png)

```r
ggplot(mpg, aes(class, after_stat(prop), group=drv)) + geom_bar() +
  facet_wrap(~drv)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/d06ffb05-9900-45e1-8a73-4db9c5163269/Untitled.png)

```r
ggplot(mpg, aes(class, drv)) + geom_point()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/838bcc89-eeb0-437e-ad20-16fec998ec2e/Untitled.png)

```r
ggplot(mpg, aes(class, drv)) + geom_jitter(width=0.2, height=0.2)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/39160260-d5b7-4d39-a7c6-050928a212c5/Untitled.png)

```r
ggplot(mpg, aes(class, drv)) + geom_count()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ab678439-23cf-44e7-b305-2658324b9565/Untitled.png)

## 5. 범주형 변수와 수치형 변수의 그래프

```r
p <- ggplot(mpg, aes(class, cty))
p + geom_point()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/260f0bed-2964-4818-a6f3-8cd9775fbd25/Untitled.png)

```r
p + geom_jitter(width = 0.2)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6fa0db05-bb6a-4980-8c66-fa7085517425/Untitled.png)

```r
p + geom_boxplot()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/af72aaea-163d-4253-82e1-43d1ec28b8db/Untitled.png)

```r
p + geom_boxplot(notch = T)
# Notch went outside hinges
# ℹ Do you want `notch = FALSE`?
# Notch went outside hinges
# ℹ Do you want `notch = FALSE`?
# Notch went outside hinges
# ℹ Do you want `notch = FALSE`?
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/a353a1bd-936c-4a98-bd59-ac0c6a5ba0c5/Untitled.png)

```r
p + geom_boxplot(notch = T) +
  stat_summary(fun=mean, color="red", size=5, shape="*", geom = "point")
# Notch went outside hinges
# ℹ Do you want `notch = FALSE`?
# Notch went outside hinges
# ℹ Do you want `notch = FALSE`?
# Notch went outside hinges
# ℹ Do you want `notch = FALSE`?
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/13bfe6d9-7eb6-46a8-a332-2aa686a893d7/Untitled.png)

```r
p + geom_violin()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/9ae95891-099d-469f-92c8-4bb44d968207/Untitled.png)

```r
p + geom_boxplot(width=0.1) +
  geom_violin(alpha=0.3)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/d73512ee-9478-4a76-85b4-f7eee4299e82/Untitled.png)

## 6. 두 수치형 변수의 그래프

- `geom_text()`
    
    ```r
    df <- filter(mpg, class == "midsize", year == 2008) 
    ggplot(df, aes(cty, hwy)) + geom_text(aes(label=model))
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/73e409b9-a4ff-46eb-97f2-9dc76008b088/Untitled.png)
    
    ```r
    ggplot(df, aes(cty, hwy)) + 
      geom_text(aes(label=model), size=3, 
                position=position_jitter(width=0.3, height=0.3))
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/709b45e9-6abb-4873-8352-d4478c4634b5/Untitled.png)
    
    ```r
    ggplot(df, aes(cty, hwy)) + geom_text(aes(label=model), check_overlap = T)
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/d41642db-eaa1-48a3-9727-0614e8e5bc1d/Untitled.png)
    
    ```r
    ggplot(df, aes(cty, hwy)) + geom_point() + 
      geom_text(aes(label=model), nudge_y=0.3, size=3)
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ba2af826-95c7-4447-96e8-de714b7dc93b/Untitled.png)
    
    ```r
    ggplot(df, aes(cty, hwy)) + 
      geom_point() + 
      geom_text(aes(label=model),  size=3,
                position=position_jitter(width=0.3, height=0.3))
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/63d54d29-a619-4384-b8bf-70a1fd3a5bfb/Untitled.png)
    
- `geom_label()`
    
    ```r
    ggplot(df, aes(cty, hwy)) + 
      geom_point() + 
      geom_label(aes(label=model), nudge_y=0.2, size=3)
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/753aee4a-d296-4c9e-b408-75b9e477286f/Untitled.png)
    
- `geom_bin2d()`
    
    ```r
    ggplot(mpg, aes(cty, hwy)) + geom_bin2d(binwidth=c(2,2))
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/4248c15e-f5ee-4cac-89da-24e8a5545de1/Untitled.png)
    

## 7. 세 변수 이상의 그래프

```r
ggplot(mpg, aes(displ, cty)) + 
  geom_point() + geom_smooth(method="lm") + 
  facet_wrap(~drv)
# `geom_smooth()` using formula = 'y ~ x'
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/c5a21732-fdb9-4d00-8c39-b84f95f90602/Untitled.png)

```r
ggplot(mpg, aes(displ, cty)) + 
  geom_point() + geom_smooth(method="lm") + 
  facet_wrap(~class)
# `geom_smooth()` using formula = 'y ~ x'
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/2bf4a16a-c476-421a-b6b8-baca4017819a/Untitled.png)

```r
ggplot(mpg, aes(displ, cty, col=drv)) + 
  geom_point() + geom_smooth(method="lm") 
# `geom_smooth()` using formula = 'y ~ x'
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/cf7e128d-e356-477e-9281-24f183491029/Untitled.png)

```r
ggplot(mpg, aes(displ, cty, col=drv, linetype=factor(year))) + 
  geom_point() + geom_smooth(method="lm") + labs(linetype="year")
# `geom_smooth()` using formula = 'y ~ x'
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/9024799a-01dd-4334-85d3-593382feb2c7/Untitled.png)

```r
ggplot(mpg, aes(displ, cty)) + 
  geom_point() + geom_smooth(method="lm") + 
  facet_grid(year~drv)
# `geom_smooth()` using formula = 'y ~ x'
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/74edb4fd-9179-496d-b280-6c64b68124e1/Untitled.png)

# 9. 그래프의 외양 바꾸기

## 1. 좌표축의 조정

- `name` : 축의 이름
- `breaks` : 축에 표시될 눈금의 위치
- `minor_breaks` : 축에 표시될 세부 눈금의 위치
- `labels` : 축 눈금에 씌여질 레이블
- `limits` : 축의 상한과 하한
- `trans` : 축에 별도의 변환을 적용할지 여부
- `position` : 축의 그래프 상에서의 위치 등
    
    ```r
    midwest
    # A tibble: 437 × 28
    #      PID county  state  area poptotal popdensity popwhite popblack popamerindian
    #    <int> <chr>   <chr> <dbl>    <int>      <dbl>    <int>    <int>         <int>
    #  1   561 ADAMS   IL    0.052    66090      1271.    63917     1702            98
    #  2   562 ALEXAN… IL    0.014    10626       759      7054     3496            19
    #  3   563 BOND    IL    0.022    14991       681.    14477      429            35
    #  4   564 BOONE   IL    0.017    30806      1812.    29344      127            46
    #  5   565 BROWN   IL    0.018     5836       324.     5264      547            14
    #  6   566 BUREAU  IL    0.05     35688       714.    35157       50            65
    #  7   567 CALHOUN IL    0.017     5322       313.     5298        1             8
    #  8   568 CARROLL IL    0.027    16805       622.    16519      111            30
    #  9   569 CASS    IL    0.024    13437       560.    13384       16             8
    # 10   570 CHAMPA… IL    0.058   173025      2983.   146506    16559           331
    # ℹ 427 more rows
    # ℹ 19 more variables: popasian <int>, popother <int>, percwhite <dbl>,
    #   percblack <dbl>, percamerindan <dbl>, percasian <dbl>, percother <dbl>,
    #   popadults <int>, perchsd <dbl>, percollege <dbl>, percprof <dbl>,
    #   poppovertyknown <int>, percpovertyknown <dbl>, percbelowpoverty <dbl>,
    #   percchildbelowpovert <dbl>, percadultpoverty <dbl>,
    #   percelderlypoverty <dbl>, inmetro <int>, category <chr>
    ```
    
    ```r
    p <- ggplot(midwest, aes(percwhite, percollege)) + geom_point()
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/8721a194-a63f-4c68-880b-c4dcfe444d5c/Untitled.png)
    
    ```r
    p + scale_x_continuous(breaks=seq(0, 100, by=10), 
                      labels=paste0(seq(0, 100, by=10), "%"))
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/7601d1cf-a57c-4e05-98c5-b3b4646302d0/Untitled.png)
    
    ```r
    p + scale_x_continuous(breaks=seq(0, 100, by=10),  
                           labels=paste0(seq(0, 100, by=10),"%"),
                           limits=c(60, 100)) +
      scale_y_continuous(name="Percent college educated")
    # Warning: Removed 2 rows containing missing values (`geom_point()`).
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/7389ffae-7fb3-492c-9c10-135ac073040b/Untitled.png)
    
    ```r
    p + scale_x_continuous(position="top") +
      scale_y_continuous(position="right")
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/7e158790-e700-400d-a2ec-1deb8b61d433/Untitled.png)
    
    ```r
    ap <- ggplot(midwest, aes(area, poptotal)) + geom_point() +
      geom_smooth(method="lm")
    # `geom_smooth()` using formula = 'y ~ x'
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/251656d9-ae44-4bbf-8950-df6c85840e87/Untitled.png)
    
    ```r
    ap + scale_y_continuous(trans="log10")
    `geom_smooth()` using formula = 'y ~ x'
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/5aaa1524-5ac5-4d92-a23d-4722ffcb9201/Untitled.png)
    

## 2. 좌표계의 변경

```r
p <- ggplot(mpg, aes(cty)) + geom_histogram(binwidth=1)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/60369431-daae-4038-af96-d41c81a5144c/Untitled.png)

```r
p + coord_flip()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/0557f9c2-e286-4142-b236-95b088d8effa/Untitled.png)

```r
p + coord_polar()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/2006ed21-8594-4d0e-9e28-0b7ef517295d/Untitled.png)

```r
ggplot(mpg, aes(class, fill=drv)) + 
  geom_bar(position="fill") + coord_polar()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/02285160-5bc1-41e7-9f3c-952d1f684030/Untitled.png)

## 3. 색상 척도(Color Scales)의 변경

```r
p <- ggplot(mpg, aes(displ, hwy))
p + geom_point(aes(color=drv), size=2)
p + geom_point(aes(color=cty), size=2)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6e93d57e-5905-4a9c-9b48-fb797e622a4f/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/9d9b7ace-694b-4c2c-aeb4-94e5b452157a/Untitled.png)

```r
p <- ggplot(mpg, aes(displ, hwy))
p + geom_point(aes(color=year), size=2)
p + geom_point(aes(color=factor(year)), size=2)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/c95be160-238b-4bce-b332-929901764c19/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/331fb233-70ca-4d01-9901-08988fd1c7f1/Untitled.png)

```r
RColorBrewer::display.brewer.all()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ece04978-6bd1-4c99-bc63-17878a1c1fff/Untitled.png)

```r
RColorBrewer::brewer.pal.info
#          maxcolors category colorblind
# BrBG            11      div       TRUE
# PiYG            11      div       TRUE
# PRGn            11      div       TRUE
# PuOr            11      div       TRUE
# RdBu            11      div       TRUE
# RdGy            11      div      FALSE
# RdYlBu          11      div       TRUE
# RdYlGn          11      div      FALSE
# Spectral        11      div      FALSE
# Accent           8     qual      FALSE
# Dark2            8     qual       TRUE
# Paired          12     qual       TRUE
# Pastel1          9     qual      FALSE
# Pastel2          8     qual      FALSE
# Set1             9     qual      FALSE
# Set2             8     qual       TRUE
# Set3            12     qual      FALSE
# Blues            9      seq       TRUE
# BuGn             9      seq       TRUE
# BuPu             9      seq       TRUE
# GnBu             9      seq       TRUE
# Greens           9      seq       TRUE
# Greys            9      seq       TRUE
# Oranges          9      seq       TRUE
# OrRd             9      seq       TRUE
# PuBu             9      seq       TRUE
# PuBuGn           9      seq       TRUE
# PuRd             9      seq       TRUE
# Purples          9      seq       TRUE
# RdPu             9      seq       TRUE
# Reds             9      seq       TRUE
# YlGn             9      seq       TRUE
# YlGnBu           9      seq       TRUE
# YlOrBr           9      seq       TRUE
# YlOrRd           9      seq       TRUE
```

```r
p_drv <- p + geom_point(aes(color=drv), size=2)
p_drv + scale_color_brewer(palette = "Set1")
p_drv + scale_color_brewer(palette = "Accent")
p_drv + scale_color_brewer(palette = "Spectral")
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/b728c822-1871-4e8a-a404-4685127dc900/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6a8b1f2b-0a67-4692-8b32-ca1eeebc39f2/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/b7c03028-be40-41f8-86ae-cde4251d0f36/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/8abdc61e-6176-4e9f-95ac-786db4b31139/Untitled.png)

```r
p_cty <- p + geom_point(aes(color=cty), size=2)
p_cty + scale_color_distiller(palette = "RdPu")
p_cty + scale_color_distiller(palette = "YlOrBr")
p_cty + scale_color_distiller(palette = "Greens")
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/46875f3d-bbee-48a0-a4cc-4e0befe32722/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/1c5b8f49-f3e5-4fe9-80f2-6c01fd4ad385/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/96fe44a0-b4a5-4316-a76d-b524ef414d76/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/a922379d-66ea-48d0-b55f-32352be297fd/Untitled.png)

## 4. 레이블 조정

```r
p <- ggplot(mpg, aes(displ, cty, color=class, shape=factor(cyl))) + geom_point()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/fc02579b-fc62-48fa-aa30-b64d59909346/Untitled.png)

```r
p <- p + labs(title="displacement vs. city fuel economy", 
         x="displacement(liter)", y="city fuel economy(miles/gallon)",
         color="car class", shape="number of cylinders")
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/293563d3-0648-4755-b068-068e3ed35192/Untitled.png)

## 5. 테마 변경

```r
p + theme_gray()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/72421197-b559-4ff5-8e20-59692a5a4f5f/Untitled.png)

```r
p + theme_bw()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/f6b53a35-22a0-4dde-9ed2-cfad3d2072bf/Untitled.png)

```r
p + theme_dark()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/0cb989e6-4648-4956-8226-e4ba2093d29f/Untitled.png)

```r
p + theme_light()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/c662dbf9-f69f-411e-88d5-44961f808fc2/Untitled.png)

```r
p + theme_linedraw()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/707a71cd-c314-4672-b18b-52f1b72aac73/Untitled.png)

```r
p + theme_classic()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/3518c87a-15e3-4d7d-b35e-5f81bf029b29/Untitled.png)

```r
p + theme_minimal()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6715e093-285c-471a-a1fb-d9ec27293d06/Untitled.png)

```r
install.packages("ggthemes")
# '/home/sys4ppl/R/x86_64-pc-linux-gnu-library/4.3'의 위치에 패키지(들)을 설치합니다.
# (왜냐하면 'lib'가 지정되지 않았기 때문입니다)
```

```r
p + ggthemes::theme_base()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/5f357725-be30-4e6d-ae51-0fc7b6bb974e/Untitled.png)

```r
p + ggthemes::theme_economist()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/c5bea482-24aa-4bd6-a83e-667c38953266/Untitled.png)

```r
p + ggthemes::theme_excel()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/8f81ebf3-c941-4ba3-9d8e-d40995930def/Untitled.png)

```r
p + ggthemes::theme_few()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/545128c7-1657-4599-a6ff-a446c9bec74e/Untitled.png)

```r
p + ggthemes::theme_tufte()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/2830ef92-b9c4-4948-bc03-51b4cc9de030/Untitled.png)

```r
oldTheme <- theme_get()
p
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ee3e0a36-e557-410e-b7fc-143f6870e767/Untitled.png)

```r
theme_set(theme_classic()) 
p
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/19bab9d4-2755-4779-9634-d5019b38d760/Untitled.png)

```r
p + labs(shape = "실린더 수", color = "분류")
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/63c1ce0d-0449-4fc1-a2bb-4dfd21f10634/Untitled.png)

```r
p + geom_hline(yintercept = mean(mpg$cty), linetype=2)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/cd8d68b0-632d-46f1-917c-ad2331d13db7/Untitled.png)

```r
theme_set(oldTheme)
p
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/7a919fdd-7dc5-4dd5-b0c2-db047919190d/Untitled.png)

```r
p + theme(legend.position = "bottom")
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/9de86646-1d71-435e-b511-c5f794f1e996/Untitled.png)

```r
myTheme <- theme(
    plot.title=element_text(face="bold.italic", size=16, color="orange", hjust=0.5),
    panel.background = element_rect(fill="lightyellow", color="green"),
    legend.position = "top")
p + myTheme
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/7001a1e2-20be-4b9f-85e4-eeac3667c531/Untitled.png)

```r
ggplot(mpg, aes(hwy, fill=drv)) + geom_histogram() + 
  labs(title="A graph with my theme") + myTheme 
# `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/75e1d89b-ae09-4d6a-8df3-31e5679a153c/Untitled.png)

```r
p
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/e8b0a70c-589e-4522-b71e-42b82ded3873/Untitled.png)

```r
oldTheme <- theme_update(
    plot.title=element_text(face="bold.italic", size=16, color="orange", hjust=0.5),
    panel.background = element_rect(fill="lightyellow", color="green"),
    legend.position = "top")
p
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/502ce78c-e22c-4b7f-83ca-5cbf2c0f649b/Untitled.png)

```r
p + geom_hline(yintercept = mean(mpg$cty), linetype=2)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/3b7061e3-6c21-492f-99f3-7e672190503a/Untitled.png)

```r
theme_set(oldTheme)
```

# 10. 기타 유용한 팁들

## 1. 여러 그래프를 한 도표에 넣기

```r
install.packages("gridExtra")

library(gridExtra)
# 다음의 패키지를 부착합니다: 'gridExtra'
# The following object is masked from 'package:dplyr':
#     combine
```

```r
p1 <- ggplot(mpg, aes(drv, displ)) + geom_jitter()
p2 <- ggplot(mpg, aes(drv, displ)) + geom_boxplot()
p3 <- ggplot(mpg, aes(drv, displ)) + geom_violin()
grid.arrange(p1, p2, p3, ncol=3)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ba70ed15-bb13-4dd5-b831-39df8efc4642/Untitled.png)

```r
grid.arrange(p1, p2, p3, nrow=2, ncol=2)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ebe4c209-7d54-4e4c-a992-e704365fd4a4/Untitled.png)

```r
grid.arrange(p1, p2, p3, ncol=3, widths=c(0.5, 0.25, 0.25))
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/0c0409c4-7152-446f-b317-d58285970809/Untitled.png)

```r
grid.arrange(p1, p2, p3, nrow=3, heights=c(0.25, 0.25, 0.5))
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/b01f81b4-123d-4ba0-b989-5370f3527bb9/Untitled.png)

```r
grid.arrange(p1, arrangeGrob(p2, p3, ncol=2, widths=c(0.6, 0.4)), nrow=2, heights=c(0.4, 0.6))
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/c54ab4d3-c38d-4460-9a75-bd71320d6eca/Untitled.png)

## 2. 그래프 저장하기
