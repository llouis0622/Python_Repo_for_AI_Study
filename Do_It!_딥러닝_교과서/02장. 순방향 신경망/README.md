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
