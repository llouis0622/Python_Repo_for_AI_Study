# 02장. 순방향 신경망

- 순방향 신경망(FNN, Feedforward Neural Network) : 다층 퍼셉트론
    - 출력 데이터가 다시 입력되는 피드백 연결, 순환이 있는 그래프 구조
- 콘벌루션 신경망(CNN, Convolution Neural Network) : 공간 데이터 가정
- 순환 신경망(RNN, Recurrent Neural Network) : 순차 데이터 가정
- 그래프 신경망(GNN, Graph Neural Network) : 그래프 데이터 가정
- 인공 뉴런(Artificial Network) : 퍼셉트론

# 1. 순방향 신경망의 구조와 설계 항목

## 1. 순방향 신경망의 구조

- 뉴런들이 모여 계층(Layer)을 이루고 계층이 쌓여 전체 신경망을 이루는 구조
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/67481bb0-bd27-4504-90c3-33d2a4106513/1.png)
    

### 1. 순방향 신경망의 계층 구조

- 입력 계층 : 외부에서 데이터 전달받음
- 은닉 계층 : 데이터의 특징 추출
- 출력 계층 : 추출된 특징을 기반으로 추론한 결과를 외부에 출력

### 2. 완전 연결 계층과 뉴런의 역할

- 완전 연결 계층(Fully Connected Layer) : 계층에 속한 각 뉴런이 이전 계층의 모든 뉴런과 모두 연결된 구조
    - 같은 입력 데이터에서 뉴런마다 서로 다른 특징 추출

### 3. 특징을 추출하는 뉴런 구조

- 가중 합산 : 추출할 특징에 중요한 영향을 미치는 데이터를 선택하는 과정
- 활성 함수 : 원하는 형태로 특징을 추출하기 위해 데이터를 비선형(Nonlinear)적으로 변환
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/c8127dbc-6b3a-4ae8-9e34-d2541c8fb078/1.png)
    

### 4. 중요한 데이터를 선택하는 가중 합산 연산

- 뉴런에 입력 데이터가 들어오면 가중치와 곱해서 가중 합산을 함

$$
z=w_1x_1+w_2x_2+...+w_nx_n+b
\\ =w^Tx+b
$$

- 가중치 $w$ : 특징을 추출할 때 영향이 큰 데이터를 선택하는 역할
- 편향 $b$ : 특징을 공간상 임의의 위치에 표현하기 위함

### 5. 비선형 변환을 통해 특징을 추출하는 활성 함수

- ReLU(Rectified Linear Unit) : 기본 활성 함수, 경첩 형태의 비선형 함수
    - 입력값이 0보다 크면 그대로 출력, 0보다 작거나 같으면 0을 출력
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/478c8e63-1ed8-4ae5-98a6-ff87c8f3bc20/1.png)
    

$$
f(z)=\begin{cases} 1 \ \ \ \ \text{if} \ z≥ 0 \\ 0 \ \ \ \ \text{그 \ 외의 \ 경우} \end{cases}
$$

- 뉴런의 활성 함수 : 신경망의 기저 함수(Basis Function)

## 2. 범용 함수 근사기로서의 신경망

### 1. 실함수와 벡터 함수

- 실함수(Real-Valued Function)
    
    $$
    f : R^n \rightarrow R
    \\ f(x)=f(x_1, x_2, ..., x_n)
    \\ x^T=(x_1, x_2, ..., x_n)
    $$
    
- 벡터 함수(Vector Function)
    
    $$
    f:R^n \rightarrow R^m
    \\ f(x)=(f_1(x), f_2(x), ..., f_m(x))
    \\ x^T=(x_1, x_2, ..., x_n)
    $$
    

### 2. 실함수인 뉴런

$$
f(x)=\text{activation}(w^Tx + b)
\\ x^T=(x_1, x_2, ..., x_n)
\\ w^T=(w_1, w_2, ..., w_n)
$$

### 3. 벡터 함수인 계층

- 입력 벡터의 크기 : 이전 계층의 뉴런 수
- 출력 벡터의 크기 : 현재 계층의 뉴런 수
    
    $$
    W=\begin{vmatrix}w_1 & w_2 & ... & w_m \end{vmatrix} = \begin{vmatrix}w_11 & w_21 & ... & w_m1 \\ w_12 & w_22 & ... & w_m2 \\ ... & ... & ... & ... \\ w_1n & w_2n & ... & w_mn \end{vmatrix}
    \\ b^T=\begin{vmatrix}b_1 & b_2 & ... & b_m \end{vmatrix}
    $$
    
    $$
    f(x)=(f_1(x), f_2(x), ..., f_m(x))=\text{activation} (W^Tx + b)
    $$
    

### 4. 벡터 함수들의 합성 함수인 신경망

$$
y=f^L(...f^2(f^1(x)))
$$

### 5. 범용 근사 정리(Universal Approximation Theorem)

- 2계층의 순방향 신경망에서 은닉 뉴런을 충분히 사용하고 검증된 활성 함수를 사용하면, n차원 공간의 임의의 연속 함수를 원하는 정도의 정확도로 근사할 수 있음

## 3. 순방향 신경망의 설계 항목

- 입력 : 입력 형태
- 출력 : 출력 형태, 활성 함수
- 은닉 계층 : 활성 함수
- 네트워크 크기 : 네트워크 깊이(계층 수), 네트워크 폭(계층별 뉴런 수)

# 2. 분류와 회귀 문제

## 1. 분류 문제

- 분류(Classification) : 데이터의 클래스(Class) 또는 카테고리(Category)를 예측
    - 이진 분류(Binary Classification) : 두 개 클래스로 분류
    - 다중 분류(Multiclass Classification) : 여러 클래스로 분류
    - 판별 함수(Discriminative Function) : 대상 판별, 입력 데이터가 속한 클래스 예측
    - 확률 모델(Stochastic Model) : 입력 데이터가 각 클래스에 속할 확률 예측

## 2. 회귀 문제

- 회귀(Regression) : 여러 독립 변수와 종속 변수의 관계를 연속 함수 형태로 분석
    - 예측값이 숫자형 데이터인 것
    - 입력 데이터에 대한 함숫값 예측

# 3. 이진 분류 문제

## 1. 베르누이 분포(Bernoulli Distribution)

$$
p(x;\mu)=\mu^x(1-\mu)^{1-x},\ x\in\{0, 1\}
$$

## 2. 확률 모델 정의

$$
p(t_i \ | \ x_i;\ \theta)=\mathfrak{Bern}(t_i; \ \mu(x_i; \ \theta))
\\ =\mu(x_i; \ \theta)^{t_i}(1-\mu(x_i; \ \theta))^{1-t_i}
$$

## 3. 출력 계층의 활성 함수

- 점수(Score), 로짓(Logit)으로 예측 → 활성 함수를 통해 베르누이 확률분포의 파라미터 $\mu$로 변환

### 1. 시그모이드 함수(Sigmoid)

- 값을 $[0, 1]$ 범위로 만들어 줌
- 스쿼싱(Squashing) 함수 : 값을 고정 범위로 변환

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/70c0041b-f85b-45f0-82dd-51714935c173/1.png)

### 2. 로지스틱 함수의 역함수인 로짓 함수

- 로그 오즈(Log Odds)
    
    $$
    \text{logit}(p) = \log(\frac{p}{1-p})
    $$
    
    $$
    \text{logit}(p)=\text{logistic}^{-1}(p) = \log(\frac{p}{1-p})
    \\ \text{logit}^{-1}(x)=\text{logistic}(x) =\frac{1}{1+e^{-x}}
    $$
    

# 4. 다중 분류 모델

## 1. 카테고리 분포(Categorial Distribution)

- 여러 종류의 사건이 발생할 확률
    
    $$
    p(x \ | \ \mu)=\prod_{k=1}^K\mu_k^{x_k}
    $$
    
    $$
    \mu=(\mu_1, \mu_2, ..., \mu_K)^T, \ \sum_{k=1}^K\mu_k=1
    $$
    
    $$
    x=(x_1, x_2, ..., x_K)^T, \ x_k=\begin{cases}1, \ k=i \\ 0, \ k \neq i \end{cases}, \ i \in \{1, 2, ..., K\}
    $$
    

## 2. 확률 모델 정의

$$
p(x_i \ | \ x_i; \ \theta)=\text{Category}(t_i; \ \mu(x_i; \ \theta))=\prod_{k=1}^K\mu(x_i; \ \theta)_k^{t_{ik}}
$$

## 3. 출력 계층의 활성 함수

### 1. 소프트맥스 함수(Softmax)

- 실수 벡터를 확률 벡터로 변환
- 값을 $[0, 1]$ 범위로 만들어 줌
    
    $$
    \text{softmax}(y_i)=\frac{e^{y_i}}{\sum_{j=1}^Ke^{y_i}}
    $$
    
    ![1.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/c8f06319-9caa-438f-981e-ebcc8ab3e871/1.jpg)
    
- 시그모이드를 여러 클래스에 대해 일반화한 함수
    
    $$
    y=(y_1, y_2, ..., y_K)^T
    $$
    
    $$
    e^y=(e^{y_1}, e^{y_2}, ..., e^{y_K})^T
    $$
    
    $$
    \hat{e}^y=\frac{1}{\sum_{k=1}^Ke^{y_{k}}}(e^{y_1}, e^{y_2}, ..., e^{y_K})^T
    $$
    
    $$
    \sum_{k=1}^K\hat{e}^{y_{k}}=1
    $$
