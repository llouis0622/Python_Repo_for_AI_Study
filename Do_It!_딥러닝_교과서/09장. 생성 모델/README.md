# 09장. 생성 모델

# 1. 생성 모델

## 1. 베이즈 정리와 주변화

- 확률의 곱 법칙 : 결합 확률 분포를 인수분해해서 두 확률분포의 곱 형태로 표현하는 것

$$
p(A\cap B)=p(A|B)p(B)
$$

- 확률의 합 법칙 : 결합 확률분포에서 일부 확률변수의 분포를 구하기 위해 나머지 확률변수에 대해 합산하는 것, 주변화(Marginalization)
    
    $$
    p(A)=\sum_{B_{k}}p(A\cap B_k)=\sum_{B_k}p(A|B_i)p(B_k)
    $$
    
- 베이즈 정리(Bayes’ Theorem) : 사전 확률분포에 증거를 반영하면 사후 확률분포가 되는 과정
    
    $$
    p(A|B)=\frac{p(A\cap B)}{p(B)}=\frac{p(B|A)p(A)}{p(B)}
    $$
    
    - 가설(Hypothesis) $A$
    - 증거(Evidence) $B$

## 2. 판별 모델과 생성 모델

- 판별 모델(Discriminative Model) : 관측 데이텉가 클래스에 속할 조건부 확률분포를 예측
- 생성 모델(Generative Model) : 입력의 확률분포 가정
- 잠재변수 모델(Latent Variable Model) : 클래스를 잠재변수로 일반화

## 3. 생성 모델의 종류

- 최대우도추정 → 명시적 추정 → 확률분포를 정확히 추정하는 방식 → 자기회귀 모델, 확률분포를 근사적으로 추정하는 방식 → VAE / 암묵적 추정 → GAN
- 명시적 추정(Explicit Density) : 확률분포의 파라미터 추정
- 암묵적 추정(Implicit Density) : 모델이 확률분포를 따르는 샘플을 생성하도록 확률분포를 표현
- 자기회귀 모델(Autoregressive Model) : 이미 생성된 자신의 데이터를 이용해서 나머지 데이터를 생성하는 모델, FVBN(Fully Visible Belief)
    
    $$
    p(x)=p(x_1, \cdots, x_n)=\prod^n_{i=1}p(x_i|x_1, \cdots, x_{i-1})
    $$
    
- VAE(Variational AutoEncoder) : 변분 오토인코더, 인코더-디코더로 구성된 잠재변수 모델로 확률분포를 변분적으로 근사
- GAN : 생성자와 판별자가 적대적 관계에서 훈련하는 모델

## 4. 생성 모델 예시

- 새로운 객체 생성 : 새로운 예술 작품 생성, 이미지 변환, 다양한 복구 작업(인페인팅, 고해상도 이미지로 변환, 이미지 색칠), 데이터 증강, 개인 정보 생성
- 확률 추정 : 이상 데이터 탐지
- 표현 학습 : 잠재 공간에서의 데이터 표현 학습
- 시계열 데이터 생성 : 강화 학습에서 미래의 상태 및 행동을 시뮬레이션하거나 계획

# 2. VAE

## 1. 오토인코더

### 1. 표현 학습(Representation Learning)

- 데이터를 가장 잘 표현하는 특징을 학습하는 방법
- 인코더 형태의 모델을 통해 학습
- 차원 축소, 데이터 압축(Data Compression), 클러스터링

### 2. 오토인코더

- 자기 자신을 잘 복구하는 표현을 학습하는 신경망
- 저차원 특징으로 인코딩 → 고차원 입력 데이터로 디코딩
- 복원 손실(Reconstruction Loss)

### 3. 전이 학습에 사용

- 사전 학습 모델(Pretrained Model) : 자기 자신을 잘 복원하는 특징을 학습
- 사전에 학습된 모델로 파라미터를 초기화해서 적은 데이터셋으로 세부 튜닝을 함

### 4. 오토인코더를 확률 모델로 확장한다면?

- 변분 오토인코더, VAE

## 2. 잠재변수 확률 모델

### 1. 가우시안 혼합(Gaussian Mixture) 분포

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/14f9645e-d1be-4be3-a500-059faabc60c4/1.png)

$$
p(x)=\sum_z p(x|z)p(z)
$$

$$
p(x)=\sum_z p(x, \ z)
$$

### 2. 가우시안 무한 혼합 분포

$$
p(x)=\int p(x|z)p(z)dz
$$

### 3. 가우시안 무한 혼합의 신경망 구현

$$
p_\theta(x|z)=N(\mu_\theta(z), \sigma^2_\theta(z))
$$

### 4. 몬테카를로 추정 방식으로 적분식을 근사

- 몬테카를로 추정(Monte Carlo Estimate) : 무작위 추출된 난수를 이용하여 함수 값 계산
    
    $$
    p(x)=\int p(x|z)p(z)dz
    \\ =\mathbb{E}_{z\sim p(z)}[p(x|z)]
    \\ \approx\frac{1}{N}\sum_zp(x|z)
    $$
    

## 3. 확률분포 추정

### 1. 최대우도추정을 위한 최적화 문제 정의

$$
p_\theta(X)=\prod^N_{i=1}p_\theta(x_i)
$$

$$
\log p_\theta(X)=\log \prod^N_{i=1}p_\theta(x_i)=\sum^N_{i=1}\log p_\theta(x_i)
$$

$$
\theta\leftarrow\argmax_\theta\sum^N_{i=1}\log p_\theta(x_i)
$$

### 2. 잠재변수 확률 모델로 확장

$$
p(x_i)=\int p_\theta(x_i|z_i)p(z_i)dz_i
$$

$$
\theta\leftarrow\argmax_\theta\sum^N_{i=1}\log\int p_\theta(x_i|z_i)p(z_i)dz_i
$$

$$
\theta\leftarrow\argmax_\theta\sum^N_{i=1}\mathbb{E}_{z_i\sim p(z_i)}[\log p_\theta(x_i|z_i)]
$$

### 3. 잠재 공간의 분화를 위한 사후 분포의 활용

$$
\theta\leftarrow\argmax_\theta\sum^N_{i=1}\mathbb{E}_{z_i\sim p_\theta(z_i|x_i)}[\log p_\theta(x_i|z_i)]
$$

### 4. 사후 확률분포의 변분 근사(Variational Approximation)

$$
\theta\leftarrow\argmax_\theta\sum^N_{i=1}\mathbb{E}_{z_i\sim q_\phi(z_i|x_i)}[\log p_\theta(x_i|z_i)]
$$

$$
p(z_i|x_i)=\frac{p_\theta(x_i|z_i)p(z_i)}{p_\theta(x_i)}=\frac{p_\theta(x_i|z_i)p(z_i)}{\int p_\theta(x_i|z_i)p(z_i)dz_i}
$$

### 5. 변분 함수의 신경망 구현

$$
q_\phi(z_i|x_i)=N(\mu_\phi(x_i), \sigma^2_\phi(x_i))
$$

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/6b4f1589-bbe2-4641-b79f-1f6e3973d17d/1.png)

## 4. VAE 유도 과정

$$
\log p_\theta(X)=\mathbb{E}_{z\sim q_\phi}(z|x)[\log p_\theta(X|Z)]-D_{KL}(q_\phi(Z|X)\|p(Z))+D_{KL}(q_\phi(Z|X)\|p_\theta(Z|X))
$$

### 1. 엔센 부등식을 이용해서 VAE 하한을 유도하는 과정

$$
\log p_\theta(X)=\mathbb{E}_{z\sim q_\phi}(z|x)[\log p_\theta(X|Z)]-D_{KL}(q_\phi(Z|X)\|p(Z))=\mathfrak{L}(X, \theta, \phi)
$$

### 2. 쿨백 라이블러 발산에서 시작하는 VAE 유도 과정

$$
\log p_\theta(X)=\mathfrak{L}(X, \theta, \phi)+D_{KL}(q_\phi(Z|X)\|p(Z))
$$

### 3. VAE의 목적 함수

$$
\mathfrak{L}(X, \theta, \phi)=\mathbb{E}_{z\sim q_\phi}(z|x)[\log p_\theta(X|Z)]-D_{KL}(q_\phi(Z|X)\|p(Z))
$$

## 5. VAE 학습

### 1. 미분이 불가능한 확률분포 샘플링

- 역전파 알고리즘으로 학습 불가
- 재파라미터화 트릭(Reparameterization Trick) : 확률변수를 다른 확률변수의 함수로 매핑
    
    $$
    z=g(\theta, \epsilon), \epsilon\sim p(\epsilon)
    $$
    
    $$
    z=\mu+\epsilon\sigma, \epsilon\sim N(0, 1)
    $$
    
    $$
    z=\mu_\phi(x)+\epsilon\odot\sigma_\phi(x), \epsilon\sim N(0, 1)
    $$
    

## 6. 쿨백-라이블러 발산

- 두 확률분포가 얼마나 다른지를 나타내는 측도
    
    $$
    D_{KL}(p\|q)=\mathcal{H}(p, q)-\mathcal{H}(p)
    $$
    
    $$
    D_{KL}(q\|p)=\mathcal{H}(q, p)-\mathcal{H}(q)
    $$
    
- 순방향 KL : 전체 분포를 덮는 형태로 근사, 0보다 값이 큰 영역에서 두 분포의 차이를 줄임
- 역방향 KL : 가장 높은 봉우리로 근사, 가장 높은 봉우리에서 두 분포의 차이를 줄임
