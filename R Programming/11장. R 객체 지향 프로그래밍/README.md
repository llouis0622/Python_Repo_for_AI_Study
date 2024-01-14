# 11. R 객체 지향 프로그래밍


# 1. 객체 지향 프로그래밍

- 절차적 프로그래밍 vs 객체 지향 프로그래밍
- OOP의 기본 특징

# 2. S3 클래스

## 1. S3 클래스 객체 만들기

- S3 클래스 객체는 리스트에 `class` 속성을 부여하여 만듦
    
    ```r
    st1 <- list(name="Gildong", year=2, GPA=3.2)
    class(st1) <- "student"
    st1
    # $name
    # "Gildong"
    # $year
    # 2
    # $GPA
    # 3.2
    # attr(,"class")
    # "student"
    ```
    

## 2. 포괄 함수(Generic Functions)

- `UseMethod()` 로 클래스에 따라 적절한 메소드 호출
    
    ```r
    print
    # function (x, ...) 
    # UseMethod("print")
    # <bytecode: 0x557dbf7f0510>
    # <environment: namespace:base>
    ```
    
- `methods()`
    
    ```r
    head(methods(print))
    # "print.acf" "print.activeConcordance"
    # "print.AES" "print.anova"
    # "print.aov" "print.aovlist"
    ```
    
- 메소드 이름 규칙
    
    ```r
    generic_function_name.class_name
    ```
    
    ```r
     print(f)
    #   X1.3 X6.8
    # 1    1    6
    # 2    2    7
    # 3    3    8
    
    print.data.frame(f)
    #   X1.3 X6.8
    # 1    1    6
    # 2    2    7
    # 3    3    8
    
    f
    #   X1.3 X6.8
    # 1    1    6
    # 2    2    7
    # 3    3    8
    
    grep("integer", methods(print))
    # integer(0)
    
    grep("character", methods(print))
    # integer(0)
    
    grep("list", methods(print))
    # 6 40 97 106 130 141 194 207 209 220 247
    
    methods(print)[grep("list", methods(print))]
    # "print.aovlist" "print.check_package_datalist"
    # "print.Dlist" "print.dummy_coef_list"
    # "print.htmltools.selector.list" "print.listof"
    # "print.rlang:::list_of_conditions" "print.shiny.tag.list"
    # "print.simple.list" "print.summary.aovlist"
    #"print.xfun_strict_list"
    ```
    
- 디폴트 메소드
    
    ```r
    print.default
    # function (x, digits = NULL, quote = TRUE, na.print = NULL, print.gap = NULL, 
    #     right = FALSE, max = NULL, width = NULL, useSource = TRUE, 
    #     ...) 
    # {
    #     args <- pairlist(digits = digits, quote = quote, na.print = na.print, 
    #         print.gap = print.gap, right = right, max = max, width = width, 
    #         useSource = useSource, ...)
    #     missings <- c(missing(digits), missing(quote), missing(na.print), 
    #         missing(print.gap), missing(right), missing(max), missing(width), 
    #         missing(useSource))
    #     .Internal(print.default(x, args, missings))
    # }
    # <bytecode: 0x557dbe2d3e08>
    # <environment: namespace:base>
    
    methods(class="lm")
    # add1           alias          anova          case.names     coerce        
    # confint        cooks.distance deviance       dfbeta         dfbetas       
    # drop1          dummy.coef     effects        extractAIC     family        
    #formula        hatvalues      influence      initialize     kappa         
    # labels         logLik         model.frame    model.matrix   nobs          
    # plot           predict        print          proj           qr            
    # residuals      rstandard      rstudent       show           simulate      
    # slotsFromS3    summary        variable.names vcov          
    # see '?methods' for accessing help and source code
    
    methods(class="student")
    # no methods found
    
    print.default(st1)
    # $name
    # "Gildong"
    # $year
    # 2
    # $GPA
    # 3.2
    # attr(,"class")
    # "student"
    ```
    
- 메소드 정의하기
    
    ```r
    print.student <- function(x) {
      cat(x$name, "\n")
      cat("year", x$year, "\n")
      cat("GPA", x$GPA, "\n")
    }
    methods(class="student")
    # print
    # see '?methods' for accessing help and source code
    
    print(st1)
    # Gildong 
    # year 2 
    # GPA 3.2
    
    summary(a)
    # Call:
    # lm(formula = cars)
    # Residuals:
    #     Min      1Q  Median      3Q     Max 
    # -7.5293 -2.1550  0.3615  2.4377  6.4179 
    # Coefficients:
    #             Estimate Std. Error t value Pr(>|t|)    
    # (Intercept)  8.28391    0.87438   9.474 1.44e-12 ***
    # dist         0.16557    0.01749   9.464 1.49e-12 ***
    # ---
    # Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    # Residual standard error: 3.156 on 48 degrees of freedom
    # Multiple R-squared:  0.6511,    Adjusted R-squared:  0.6438 
    # F-statistic: 89.57 on 1 and 48 DF,  p-value: 1.49e-12
    ```
    

## 3. S3에서 상속성의 구현

- 상위 클래스와 하위 클래스 : 상위 클래스에 부분집합 관계
- 상속성을 구현하는 방법
    
    ```r
    st2 <- list(name="Gilsan", year=1, GPA=3.8, advisor="Sejong")
    class(st2) <- c("gradstudent", "student")
    methods(class="gradstudent")
    # no methods found
    
    st2
    # Gilsan 
    # year 1 
    # GPA 3.8
    ```
    
- 메소드 Overiding
    
    ```r
    print.gradstudent <- function(x) {
      print.student(x)
      cat("Advisor", x$advisor, "\n")
    }
    st2
    # Gilsan 
    # year 1 
    # GPA 3.8 
    # Advisor Sejong
    ```
    

# 3. S4 클래스

- S3 클래스의 안정성 문제
    
    ```r
    # Rows: 5 Columns: 3
    # ── Column specification ────────────────────────────────────────────────────────
    # Delimiter: "&"
    # chr (3): 작업 ,  S3 ,  S4 
    # 
    # ℹ Use `spec()` to retrieve the full column specification for this data.
    # ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ```
    
- 클래스 정의 `setClass()`
    
    ```r
    setClass("newstudent", 
      representation(name="character", year="numeric", GPA="numeric" ))
    ```
    
- 객체 생성 `new()`
    
    ```r
    st3 <- new("newstudent", name="Gildong", year=2, GPA=3.2)
    st3
    # An object of class "newstudent"
    # Slot "name":
    # "Gildong"
    # Slot "year":
    # 2
    # Slot "GPA":
    # 3.2
    
    st4 <- new("newstudent", sname="Gildong", year=2, GPA=3.2)
    # Error in initialize(value, ...): invalid name for slot of class "newstudent": sname
    
    st4 <- new("newstudent", name="Gildong", year=2, GPA="3.2")
    # Error in validObject(.Object): 잘못된 클래스 "newstudent" 객체입니다: invalid object for slot "GPA"
    ```
    
- 객체 요소에 접근 `slot()`
    
    ```r
    st3@name
    # "Gildong"
    
    slot(st3, "GPA")
    # 3.2
    
    st3@year <- 4
    st3@GPa <- 4.0
    # Error in (function (cl, name, valueClass) : 'GPa'는 클래스 "newstudent"내에 있는 슬롯이 아닙니다
    
    st3
    # An object of class "newstudent"
    # Slot "name":
    # "Gildong"
    # Slot "year":
    # 4
    # Slot "GPA":
    # 3.2
    ```
    
- S4 클래스 메소드 생성 `setMethod()`
    
    ```r
    summary(st3)
    # Length      Class Mode 
    #      1 newstudent   S4
    
    setMethod("summary", "newstudent",
        function(object){
          cat(object@name, " is a ", 
              object@year, "th year student with GPA ", 
              object@GPA, "\n", sep="")
        })
    summary(st3)
    # Gildong is a 4th year student with GPA 3.2
    
    removeMethod("summary", "newstudent")
    # TRUE
    
    summary(st3)
    # Length      Class Mode 
    #      1 newstudent   S4
    ```
