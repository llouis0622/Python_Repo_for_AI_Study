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
    

# 5. 회귀 모델

## 1. 가우시안 분포(Gaussian Distribution)

- 평균을 중심으로 대칭적인 종 모양의 사건이 발생할 확률
    
    $$
    \mathcal{N}(x\ | \ \mu, \ \sigma^2)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/0b1732b4-32d3-414b-a671-dd2b8e2fcf03/1.png)
    
- 관측 데이터의 분포 근사

## 2. 회귀 모델 정의

$$
t_i = y(x_i; \ \theta)+\epsilon, \ \epsilon \sim \mathcal{N}(\epsilon \ | \ 0, \ \beta^{-1})
$$

$$
p(t_i \ | \ x_i; \ \theta)=\mathcal{N}(t_i \ | \ y(x_i; \ \theta), \ \beta^{-1})
$$

## 3. 출력 계층의 활성 함수

- 항등 함수(Identity Function) : 입력값을 그대로 출력하는 함수
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/29e3b51f-e687-43ca-9eb1-bf3ab55f8917/1.png)
    

# 6. 입력 계층

- 입력 데이터를 벡터 형태로 받아서 다음 계층에 전달하는 역할
    
    $$
    x^T=(x_1, x_2, ..., x_n)
    $$
    

# 7. 활성 함수

- 시그모이드(Sigmoid) 계열 : S자형 곡선 형태
    - 시그모이드(Sigmoid)
    - 하이퍼볼릭 탄젠트(Tanh, Hyperbolic Tangent)
    - 연산 속도 느림, 그레이디언트 소실 원인, 스쿼싱 기능
- ReLU(Rectified Linear Unit) 계열 : 구간 선형 함수
    - ReLU
    - 리키 ReLU(Leaky ReLU)
    - 맥스아웃(Maxout)
    - ELU(Exponential Linear Unit)
    - 선형성, 연산 속도 빠름, 학습 과정 안정적

## 1. 계단 함수(Step Function)

- 생체 뉴런의 발화 방식 모방
- 모든 구간에서 미분값이 0
    
    $$
    f(z)=\begin{cases} 1 \ \ \ \ \text{if} \ z≥ 0 \\ 0 \ \ \ \ \text{그 \ 외의 \ 경우} \end{cases}
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/08af994c-3d69-4dc0-9253-968c08c92ce5/1.png)
    

## 2. 시그모이드 함수(Sigmoid Function)

- 모든 구간에서 미분 가능, 증가 함수
- 함수 정의에 지수 함수가 포함되어 있어서 연산 비용이 많이 듦
- 그레이디언트 포화가 발생해서 학습이 중단될 수 있음
    - 시그모이드 함수 끝부분에서 미분값이 0으로 포화되는 상태
- 양수만 출력하므로 학습 경로가 진동하면서 학습 속도가 느려짐
    
    $$
    f(x)=\frac{1}{1+e^{-x}}
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/99dd0174-899c-49d7-aee8-1533b1704eb6/1.png)
    

## 3. 하이퍼볼릭 탄젠트 함수(Tanh, Hyperbolic Tangent Function)

- 함수값이 $[-1, 1]$ 범위에 있는 S형 함수
    
    $$
    f(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/57e0690c-eed1-4caa-a23d-4e81a2535dc1/1.png)
    
    $$
    \tanh(x)=2\sigma(2x)-1
    $$
    
- 함수 정의에 지수 함수가 포함되어 있어서 연산 비용이 많이 듦
- 그레이디언트 포화가 발생해서 학습이 중단될 수 있음
    
    ![1.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/711746e3-d69f-475d-9840-97d90e0b7d80/1.jpg)
    

## 4. ReLU 함수(Rectified Linear Unit Function)

- 0보다 큰 입력이 들어오면 그대로 통과시키고 0보다 작은 입력이 들어오면 0을 출력하는 함수
    
    $$
    f(x)=\begin{cases} x & \text{if} \ x≥ 0 \\ 0 & \text{그 \ 외의 \ 경우} \end{cases}
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/af9555a6-008c-4d0e-ba9a-7840a24f5d53/1.png)
    

### 1. ReLU는 왜 빠를까?

- 추론이 빨라지는 이유 : 연산이 거의 없음
- 학습이 빨라지는 이유 : 미분을 계산할 필요가 없음

### 2. 죽은 ReLU(Dead ReLU)

- 뉴런이 계속 0을 출력하는 상태
- 양수만 출력, 학습 경로가 진동하면서 학습 속도 느려짐
- 죽은 ReLU가 발생하면 학습이 진행되지 않음

## 5. 릭키 ReLU, PReLU, ELU 함수

- 릭키 ReLU(Leaky ReLU) : 음수 구간이 0이 되지 않도록 약간의 기울기가 있는 것
    - 기울기 고정 → 최적의 성능 불가능
    
    $$
    f(x)=\begin{cases} x & \text{if} \ x≥ 0 \\ 0.001x & \text{그 \ 외의 \ 경우} \end{cases}
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/9ad2d95b-9b42-4a58-9b47-57bf70c13e75/1.png)
    
- PReLU(Parametic ReLU) : 뉴런별로 기울기를 학습
- ELU(Exponential Linear Units) : 음수 구간이 $\alpha(e^x-1)$ 와 같이 지수 함수 형태로 정의
    
    $$
    f(x)=\begin{cases} x & \text{if} \ x > 0 \\ \alpha(e^x-1) & \text{그 \ 외의 \ 경우} \end{cases}
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6580c3c4-b679-46f6-8189-54ae6bc68d4e/1.png)
    

## 6. 맥스아웃 함수(Maxout Function)

- 활성 함수를 구간 선형 함수(Piecewise Linear Function)로 가정, 각 뉴런에 최적화된 활성 함수를 학습을 통해 찾아냄
    
    $$
    f(x)=\max(w_i^Tx + b_i), \ i=1, 2, ..., k
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/4837e06b-2340-442e-aeb3-9285cfc4bf27/1.png)
    

### 1. 맥스아웃 유닛(Maxout Unit) 구조

- 맥스아웃 활성 함수를 학습하기 위해 뉴런을 확장한 구조
- 선형 함수를 학습하는 선형 노드(Linear Node) + 최댓값을 출력하는 노드
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/40759d01-0a7b-4d8f-82fa-e863fac9ef4f/1.png)
    

### 2. 볼록 함수 근사 능력

- 선형 노드의 개수에 따라 다른 형태의 볼록 함수(Convex Function) 근사 가능

## 7. Swish 함수 = SiLU(Sigmoid Linear Unit)

- ReLU와 ELU와 비슷한 모양, 원점 근처의 음수 구간에서 잠시 볼록 튀어나왔다가 다시 0으로 포화
    
    $$
    f(x) = x \ \cdot \ \sigma(x)
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/f34bfe79-621c-4fa3-9882-0019ab0b924d/1.png)
    

# 8. 신경망 모델의 크기

- 너비(Width)와 깊이(Depth)로 모델의 크기 정해짐
    - 너비 : 계층별 뉴런 수
    - 깊이 : 계층 수

## 1. 모델 크기 탐색

- 그리드 서치(Grid Search) : 파라미터별로 구간을 정해서 등간격으로 값을 샘플링하는 방법
- 랜덤 서치(Random Search) : 여러 파라미터를 조합해서 랜덤하게 값을 샘플링하는 방법
- NAS(Network Architecture Search) : 네트워크 구조 탐색 방법, 자동 모델 탐색 방법

## 2. 모델 크기 조정

- 성능이 검증된 기본 모델을 선택해서 새로운 문제에 맞게 모델의 크기를 조정하는 것
- 이피션트넷(EfficientNet)에서 신경망의 너비, 깊이, 입력 이미지의 해상도를 고려하여 모델 크기 조정
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/0a38d181-a0b6-432a-9374-1cf321ca9947/1.png)
    
- 기본 모델의 너비 증가 → 성능 향상
- 기본 모델의 깊이 증가 → 성능 향상
- 기본 모델의 해상도 증가 → 성능 향상
- 기본 모델의 너비 증가 + 기본 모델의 깊이 증가 + 기본 모델의 해상도 증가 → 성능 향상
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/33a86609-6cee-45de-b6d6-50da0a3bdc81/1.png)
    

# 9. 신경망 학습 관련 내용

## 1. 시그모이드 함수와 크로스 엔트로피 손실

$$
J(\theta)=-\sum_{i=1}^Nt_i \ \cdot \ \log \mu(x_i; \ \theta)+(1-t_i) \ \cdot \ \log(1-\mu(x_i; \ \theta))
$$

$$
J(\theta)=-\log(\mu(x; \ \theta))
\\ =-\log(\sigma(x))
\\ =-\log(\frac{1}{1+e^{-x}})
\\ =\log(1+e^{-x})
\\ =\text{softplus}(-x)
$$

- 소프트플러스(Softplus) 함수 : 부드러운 곡선 형태의 ReLU 함수
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/e222168e-151a-49be-bf6d-99e6281821f4/1.png)
    
    $$
    \text{softplus}(x)=\log(1+e^x)
    $$
    

## 2. 양수만 출력하는 활성 함수의 최적화 문제

- 활성 함수의 출력이 항상 양수 → 학습 경로의 이동 방향이 크게 진동, 학습이 느려짐
    
    $$
    \frac{\partial J}{\partial w} = \frac{\partial J}{\partial z} \ \cdot \frac{\partial z}{\partial w}
    $$
    
    $$
    \frac{\partial z}{\partial w} = x
    $$
    
    ![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/3b5824d8-e5e3-4265-8b9a-8d58cf61db6d/1.png)
    

## 3. 죽은 ReLU가 발생하는 이유

- 가중치 초기화를 잘 못했거나 학습률이 매우 클 때 발생
    
    $$
    \frac{\partial J}{\partial w} = \frac{\partial J}{\partial z} \ \cdot \frac{\partial z}{\partial w}
    $$
    
    $$
    \frac{\partial z}{\partial w} = x
    $$
    
- 가중치가 한 번 음수가 되면 다음 입력이 들어왔을 때 가중 합산이 음수가 되므로 ReLU는 0을 출력, ReLU의 그레이디언트가 0이 되어 학습이 더 진행되지 않고 계속해서 0을 출력하는 상태 유지

## 4. 미분 불가능한 활성 함수

- 신경망은 근사 방식으로 함수 표현 → 약간의 미분 오차를 허용해도 결과에 미치는 영향은 크지 않음
