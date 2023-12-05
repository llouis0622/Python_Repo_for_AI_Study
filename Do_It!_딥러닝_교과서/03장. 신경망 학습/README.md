# 03장. 신경망 학습

# 1. 신경망 학습의 의미

- 경험 데이터로부터 데이터에 내재한 정보와 규칙을 찾아서 추론 능력을 만드는 과정

### 1. 입출력의 매핑 규칙은 어떤 형태로 존재할까?

- 함수적 매핑 관계
- 가중 합산과 활성 함수가 연결되어 뉴런 구성 → 뉴런이 모여 계층 구성 → 계층이 쌓여 신경망의 계층 구조 정의

### 2. 입출력의 매핑 규칙에서 학습해야 할 것들

- 신경망 모델의 가중치와 편향 조정 → 최적의 값
- 최적화(Optimization) 기법 : 함수의 해를 근사적으로 찾는 방법

# 2. 신경망 학습과 최적화

## 1. 최적화란?

- 유한한 방정식으로 정확한 해를 구할 수 없을 때 근사적으로 해를 구하는 방법
- 다양한 제약 조건을 만족하면서 목적 함수를 최대화하거나 최소화하는 해를 반복하여 조금씩 접근하는 방식으로 찾아가는 방법

### 1. 최적화 문제의 표준 형태

$$
\min_{x \in D} \ \ \ \ f(x)
\\ \text{subject to} \ \ \ \ g_i(x) \leq 0, \ i=1, ..., m
\\ h_j(x)=0, \ j=1, ..., r
$$

- 목적 함수(Objective Function) $f(x)$ + 제약 조건 $g_i(x) \leq 0, h_j=0$
- 표준 최적화 문제 : 변수 $x$에 대한 등식과 부등식으로 표현되는 여러 제약 조건을 만족하면서 목적 함수인 $f(x)$를 최소화하는 $x$의 값을 찾는 문제
- 수렴한다(Converge) : 최적해(Optimal Solution)에 점점 가까이 가는 상태

### 2. 최소화 문제와 최대화 문제의 관계

- 목적 함수의 부호 변환으로 최대화, 최소화 변환 가능
- 최소화 문제의 목적 함수 : 비용 함수(Cost Function), 손실 함수(Loss Function)
- 최대화 문제의 목적 함수 : 유틸리티 함수(Utility Function)

## 2. 신경망 학습을 위한 최적화 문제 정의

### 1. 회귀 문제를 최적화 문제로 정의한다면?

- 타깃과 예측값의 오차를 최소화하는 파라미터를 찾으라
    
    $$
    \min_{\theta} \ \ \frac{1}{N}\sum_{i=1}^N\left\| t_i-y(x_i; \ \theta)\right\|^2_2
    $$
    
- 손실 함수 : 평균제곱오차(MSE, Mean Square Error)

### 2. 분류 문제를 최적화 문제로 정의한다면?

- 관측 확률분포와 예측 확률분포의 차이를 최소화하는 파라미터를 찾으라
    
    $$
    \min_{\theta} \ \ -\frac{1}{N}\sum_{i=1}^N\sum_{k=1}^Kt_{ik}  \ \cdot \ \log\mu(x_i; \ \theta)_k
    $$
    
- 손실 함수 : 크로스 엔트로피(Cross Entropy)

## 3. 최적화를 통한 신경망 학습

- 최적화 : 손실 함수의 최소 지점을 찾아가는 과정

# 3. 경사 하강법

## 1. 신경망의 학습 목표

- 전역 최소(Global Minimum) : 함수 전체에서 가장 낮은 곳, 최소
- 지역 최소(Local Minimum) : 함수에서 부분적으로 낮은 곳, 극소
    
    ![1.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/ec85fff8-a4ff-40d1-bbb9-06a271735ae4/1.jpg)
    
- 최적화 알고리즘의 목표 : 지역 최소를 찾는 것

## 2. 신경망 학습을 위한 최적화 알고리즘

- 1차 미분 : 상대적 수렴 속도 느림, 곡면이 매우 복잡해도 사용 가능
    - 경사 하강법
    - 경사 하강법의 변형 알고리즘 : SGD, SGD 모멘텀, AdaGrad, RMSProp, Adam
- 1.5차 미분 : 1차 미분 → 2차 미분 근사, 메모리 사용량 많음
    - 준 뉴턴 방법(Quasi-Newton Method)
    - 켤레 경사 하강법(Conjugate Gradient Descent)
    - 레번버그-마쿼트 방법(Levenberg-Marquardt Method)
- 2차 미분 : 곡률 사용 → 최적해를 빠르게 찾을 수 있음, 계산 비용, 메모리 사용량 많음
    - 뉴턴 방법(Newton Method)
    - 내부점법(Interior Point Method)

## 3. 경사 하강법(Gradient Descent)

- 손실 함수의 최소 지점을 찾기 위해 경사가 가장 가파른 곳을 찾아서 한 걸음씩 내려가는 방법
- 손실 함수의 기울기를 구하고 기울기의 반대 방향으로 내려감
    
    $$
    \theta^+ = \theta-\alpha\frac{\partial J}{\partial \theta}
    $$
    
- 신경망 모델의 파라미터 $\theta$
- 스텝 크기(Step Size) = 학습률(Learning Rate) $\alpha$ : 이동 폭 결정
- 이동 방향 $-\frac{\partial J}{\partial \theta}$ : 기울기의 음수 방향, 현재 지점에서 가장 가파른 내리막길로 내려감

## 4. 신경망에 경사 하강법 적용

### 1. 2계층 신경망 회귀 모델

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/1e28f66c-96ff-4377-9be2-76ff85fa180a/1.png)

$$
J(y)=\frac{1}{N}\sum_{(x, t)\in D}^{N}\left\| t-y\right\|^2_2 \\ 
\\ y=\text{Identity}(z^2) \\ 
\\ z^2=w^2_1\cdot a^1_1 + w^2_2\cdot a^1_2 + ... + w^2_m\cdot a^1_m \\ 
\\ a^1_m=\text{ReLU}(z^1_m) \\ 
\\ z^1_m=w^1_{1m}\cdot x_1 + w^1_{2m}\cdot x_2 + ... + w^1_{nm}\cdot x_n
$$

- 가중치 $w^1_{nm}$ : 위 첨자 1(계층 번호), 아래 첨자 $n$(이전 뉴런의 인덱스),  $m$(뉴런의 인덱스)
- 가중 합산 출력 변수 $z^1_m$ : 위 첨자 1(계층 번호), 아래 첨자 $m$(뉴런의 인덱스)
- 활성 함수 출력 변수 $a^1_m$ : 위 첨자 1(계층 번호), 아래 첨자 $n$(뉴런의 인덱스)

### 2. 파라미터 업데이트 식

$$
{w^1_{nm}}^+=w^1_{nm}-\alpha\frac{\partial J}{\partial w^1_{nm}}
$$

$$
\frac{\partial J}{\partial w^1_{nm}}=\frac{\partial J}{\partial y} \cdot \frac{\partial y}{\partial z^2} \cdot \frac{\partial z^2}{\partial a^1_m} \cdot \frac{\partial a^1_m}{\partial z^1_m} \cdot \frac{\partial z^1_m}{\partial w^1_{nm}}
$$

### 3. 연쇄 법칙을 사용한 미분 계산

$$
z^1_m=w^1_{1m} \cdot x_1 + w^1_{2m} \cdot x_2 + ... + w^1_{nm} \cdot x_n \ \ ... \ \ \frac{\partial z^1_m}{\partial w^1_{nm}}=x_n
$$

$$
a^1_m=\text{ReLU}(z^1_m) \ \ ... \ \ \frac{\partial a^1_m}{\partial z^1_m}=\text{ReLU}'(z^1_m)
$$

$$
z^2=w^2_1 \cdot a^1_1 + w^2_2 \cdot a^1_2 + ... + w^2_m \cdot a^1_m \ \ ... \ \ \frac{\partial z^2}{\partial a^1_m}=w^2_m
$$

$$
y=\text{Identity}(z^2) \ \ ... \ \ \frac{\partial y}{\partial z^2}=\text{Identity}'(z^2)=1
$$

$$
J(y)=\frac{1}{N}\sum_{(x, t)\in D}^N \left\| t-y\right\|^2_2 \ \ ... \ \ \frac{\partial J}{\partial y} \ \ ... \ \ \frac{\partial J}{\partial y}=-\frac{1}{N}\sum_{(x, t)\in D}^N 2(t-y)
$$

### 4. 신경망에서 연쇄 법칙으로 미분하는 과정

$$
\frac{\partial J}{\partial w^1_{nm}}=\frac{\partial J}{\partial y} \cdot \frac{\partial y}{\partial z^2} \cdot \frac{\partial z^2}{\partial a^1_m} \cdot \frac{\partial a^1_m}{\partial z^1_m} \cdot \frac{\partial z^1_m}{\partial w^1_{nm}}
$$

![1.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/556114b9-4301-46af-a5cb-bc9a7226abd0/1.jpg)

$$
\frac{\partial J}{\partial w^1_{nm}}=\frac{\partial J}{\partial y} \cdot \frac{\partial y}{\partial z^2} \cdot \frac{\partial z^2}{\partial a^1_m} \cdot \frac{\partial a^1_m}{\partial z^1_m} \cdot \frac{\partial z^1_m}{\partial w^1_{nm}} \\ = -\frac{1}{N}\sum_{(x, t)\in D}^N 2(t-y) \cdot 1 \cdot w^2_m \cdot \text{ReLU}'(z^1_m) \cdot x_n
$$

$$
{w^1_{nm}}^+=w^1_{nm} - \alpha\frac{\partial J}{\partial w^1_{nm}} \\ = w^1_{nm} - \alpha(-\frac{1}{N}\sum_{(x, t)\in D}^N 2(t-y) \cdot 1 \cdot w^2_m \cdot \text{ReLU}'(z^1_m) \cdot x_n)
$$

# 4. 역전파 알고리즘

## 1. 역전파 알고리즘(Backpropagation Algorithm)

$$
\frac{\partial J}{\partial w^1_{nm}}=\frac{\partial J}{\partial y} \cdot \frac{\partial y}{\partial z^2} \cdot \frac{\partial z^2}{\partial h^1_m} \cdot \frac{\partial h^1_m}{\partial z^1_m} \cdot \frac{\partial z^1_m}{\partial w^1_{nm}}
$$

$$
\frac{\partial J}{\partial w^1_{n-1m}}=\frac{\partial J}{\partial y} \cdot \frac{\partial y}{\partial z^2} \cdot \frac{\partial z^2}{\partial a^1_m} \cdot \frac{\partial a^1_m}{\partial z^1_m} \cdot \frac{\partial z^1_m}{\partial w^1_{n-1m}}
$$

$$
\frac{\partial J}{\partial w^1_{nm}}=\frac{\partial J}{\partial z^1_m} \cdot \frac{\partial z^1_m}{\partial w^1_{nm}}
$$

$$
\frac{\partial J}{\partial w^1_{n-1m}}=\frac{\partial J}{\partial z^1_m} \cdot \frac{\partial z^1_m}{\partial w^1_{n-1m}}
$$

- 오차 : 각 뉴런의 공통부분에 해당하는 미분값
- 오차를 역방향으로 전파하면서 미분을 계산함

## 2. 역전파 알고리즘의 실행 순서

### 1. 손실 함수 미분

- 손실 함수 지역 미분 : 손실 함수 $J(y)=\frac{1}{N}\sum_{(x, t)\in D}^{N}\left\| t-y\right\|^2_2$의 지역 미분 $\frac{\partial J}{\partial y}$ 계산
- 손실 함수 전역 미분 : 손실 함수 전역 미분은 지역 미분 $\frac{\partial J}{\partial y}$과 같음
- 손실 함수 전역 미분 $\frac{\partial J}{\partial y}$을 출력 계층 $O$에 전달

### 2. 출력 뉴런 미분

- 활성 함수 지역 미분 : 활성 함수 $y=\text{Identity}(z^2)$의 지역 미분 $\frac{\partial y}{\partial z^2}$를 계산
- 활성 함수 전역 미분 : $\frac{\partial J}{\partial y}$과 $\frac{\partial y}{\partial z^2}$을 곱해서 활성 함수 전역 미분 $\frac{\partial J}{\partial z^2}=\frac{\partial J}{\partial y} \cdot \frac{\partial y}{\partial z^2}$를 계산
- 공통부분 계산 : 활성 함수의 전역 미분 $\frac{\partial J}{\partial z^2}$이 뉴런의 공통부분이 됨
- 가중치 지역 미분 : 가중 합산 식에 대해 가중치별로 지역 미분 계산
- 가중치 전역 미분 : 공통부분과 지역 미분을 곱해서 가중치의 전역 미분 계산
- 가중치 업데이트 : 전역 미분으로 가중치 업데이트
- 입력 지역 미분 : 가중 합산 식에 대해 입력별로 지역 미분 계산
- 입력 전역 미분 : 공통부분과 지역 미분을 곱해서 입력의 전역 미분을 계산
- 은닉 뉴런에 미분 전달 : 은닉 뉴런에 입력의 전역 미분을 전달

### 3. 은닉 뉴런 미분

- 활성 함수 지역 미분 : 활성 함수의 지역 미분 계산
- 활성 함수 전역 미분 : 전역 미분과 지역 미분을 곱해서 활성 함수 전역 미분을 계산
- 공통부분 계산 : 활성 함수의 전역 미분이 뉴런의 공통부분
- 가중치 지역 미분 : 가중 합산 식에 대해 가중치별로 지역 미분을 계산
- 가중치 전역 미분 : 공통부분과 지역 미분을 곱해서 가중치의 전역 미분을 계산
- 가중치 업데이트 : 가중치 전역 미분으로 가중치 업데이트
- 입력 계층에는 가중치가 없으므로 미분 전달하지 않음

## 3. 뉴런 관점에서 보는 역전파 알고리즘

$$
\frac{\partial z}{\partial x}=\frac{\partial f(x, y)}{\partial x}
$$

$$
\frac{\partial y}{\partial x}=\frac{\partial f(x, y)}{\partial y}
$$

$$
\frac{\partial J}{\partial x}=\frac{\partial J}{\partial z} \cdot \frac{\partial z}{\partial x}
$$

$$
\frac{\partial J}{\partial y}=\frac{\partial J}{\partial z} \cdot \frac{\partial z}{\partial y}
$$

- 지역 미분을 구하고 전달받은 전역 미분에 곱하는 것

### 1. 계층 단위의 미분

- 그레이디언트 : 뉴런에서 가중치의 미분을 나타냄, 벡터 표현
- 야코비안(Jacobian) : 계층에서 가중치와 미분을 나타냄, 행렬 표현

### 2. 야코비안

- $f:\mathbb{R^n} \rightarrow \mathbb{R^n}$ 형태의 벡터 함수의 미분
    
    $$
    Jf=\begin{pmatrix}
    \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots  & \frac{\partial f_1}{\partial x_n} \\
    \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} &  & \frac{\partial f_2}{\partial x_n} \\
    \vdots  &  & \ddots  & \vdots  \\
    \frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \cdots  & \frac{\partial f_m}{\partial x_n} \\
    \end{pmatrix}
    \\ f(x)=(f_1(x), f_2(x), \cdots , f_m(x))
    \\ x=(x_1, x_2, \cdots , x_n)
    $$
    

## 4. 주요 활성 함수의 미분

- 시그모이드
    
    $$
    f(x)=\frac{1}{1+e^{-x}}
    $$
    
    $$
    f'(x)=f(x)(1-f(x))
    $$
    
- 하이퍼볼릭 탄젠트
    
    $$
    f(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
    $$
    
    $$
    f'(x)=1-f(x)^2
    $$
    
- ReLU
    
    $$
    f(x)=\begin{cases}x & \text{if} \ \ x > 0 \\ 0 & \text{otherwise} \end{cases}
    $$
    
    $$
    f'(x)=\begin{cases}1 & \text{if} \ \ x > 0 \\ 0 & \text{otherwise} \end{cases}
    $$
    
- 리키 ReLU
    
    $$
    f(x)=\begin{cases}x & \text{if} \ \ x > 0 \\ 0.01x & \text{otherwise} \end{cases}
    $$
    
    $$
    f(x)=\begin{cases}1 & \text{if} \ \ x > 0 \\ 0.01 & \text{otherwise} \end{cases}
    $$
