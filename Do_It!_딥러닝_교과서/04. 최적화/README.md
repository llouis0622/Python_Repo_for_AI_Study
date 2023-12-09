# 04장. 최적화

# 1. 확률적 경사 하강법

- 경사가 가장 가파른 곳으로 내려가다 보면 언젠가 가장 낮은 지점에 도달한다

## 1. 고정된 학습률

- 학습률 : 최적화할 때 한 걸음의 폭을 결정하는 스텝 크기, 학습 속도 결정

### 1. 학습률을 조정하지 않으면 무슨 일이 생길까?

- 학습률 낮음 → 학습 속도 느림
- 학습률 높은 → 최적해로 수렴하지 못함, 손실이 점점 커지는 방향으로 발산

### 2. 학습률 감소(Learning Rate Decay)

- 처음에는 높은 학습률로 시작, 학습이 진행되는 상황에 따라 학습률을 조금씩 낮춤

### 3. 적응적 학습률(Adaptive Learning Rate)

- 학습의 진행 상황이나 곡면의 변화를 알고리즘 내에서 고려해서 학습률을 자동으로 조정

## 2. 협곡에서 학습이 안 되는 문제

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/5f685bf1-3202-4c5f-aacb-f33d0bdcb619/1.png)

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/fb91e6ef-ef46-4bb8-a823-845d3ce93622/1.png)

## 3. 안장점에서 학습 종료

- 임계점(Critical Point) : 미분값이 0인 지점, 최대점(Maximum Point), 최소점(Minimum Point), 안장점(Saddle Point)

### 1. 손실 함수 곡면에는 안장점이 얼마나 많을까?

$$
P(최소점)=\frac{1}{2^n}, \ P(최대점)=\frac{1}{2^n}, \ P(안장점)=1-\frac{1}{2^{n-1}}
$$

### 2. 임계점을 만났을 때 최대점, 최소점, 안장점을 어떻게 구분할까?

- 손실 크기 비교
- 최대점 : 손실 매우 높음
- 최소점 : 손실 매우 낮음
- 안장점 : 손실이 매우 낮지 않음

## 4. 학습 경로의 진동

- 최적화 경로가 최적해를 향해 일관성 있게 진행 → 손실 함수의 표면이 거칠더라도 민감하게 경로 변경 금지

# 2. SGD 모멘텀

## 1. 핵심 개념

- SGD 모멘텀(SGD Momentum) : 지금까지 진행하던 속도에 관성이 작용하도록 만든 방식
- 현재의 속도 벡터 + 그레이디언트 벡터
    
    $$
    v_{t+1}=\rho v_t+\nabla f(x_t)
    \\ x_{t+1}=x_t-\alpha v_{t+1}
    $$
    

## 2. 관성을 이용한 임계점 탈출과 빠른 학습

- 관성 → 진행하던 속도로 계속 진행 → 안장점 탈출

## 3. 오버 슈팅(Overshooting) 문제

- 경사가 가파르면 빠른 속도로 내러오다가 최소 지점을 만나면 그레이디언트는 순간적으로 작아지지만 속도는 여전히 크기 때문에 최소 지점을 지나치는 것

# 3. 네스테로프 모멘텀

## 1. 핵심 개념

- 네스테로프 모멘텀(Nesterov Momemtum) : 관성을 이용해서 현재 속도로 한 걸음 미리 간 지점에서 내리막길로 내려가는 방식
- 현재의 속도 벡터 + 현재 속도로 한 걸음 미리 가 본 위치의 그레이디언트 벡터
    
    $$
    v_{t+1}=\rho v_t-\alpha\nabla f(x_t+\rho v_t)
    \\ x_{t+1}=x_t+v_{t+1}
    $$
    

## 2. 오버 슈팅 억제

- 관성이 커지더라도 오버 슈팅이 될지 미리 살펴보고 교정

## 3. 그레이디언트 계산 트릭

$$
v_{t+1}=\rho v_t-\alpha\nabla f(x_t+\rho v_t)
\\ x_{t+1}=x_t+v_{t+1}
$$

$$
v_{t+1}=\rho v_t-\alpha\nabla f(\tilde{x}_t)
$$

$$
\tilde{x}_{t+1}-\rho v_{t+1}=\tilde{x}_t-\rho v_t+v_{t+1}
$$

$$
v_{t+1}=\rho v_t-\alpha\nabla f(\tilde{x}_t)
\\ \tilde{x}_{t+1}=\tilde{x}_t+v_{t+1}+\rho(v_{t+1}-v_t)
$$

# 4. AdaGrad

## 1. 핵심 개념

- AdaGrad(Adaptive Gradient) : 손실 함수의 곡면의 변화에 따라 적응적으로 학습률을 정하는 알고리즘
- 경사가 가파를 때 → 작은 폭으로 이동
- 경사가 완만할 때 → 큰 폭으로 빠르게 이동
    
    $$
    기울기 벡터=(\nabla f(x_1), \nabla f(x_2), \nabla f(x_3), \cdots, \nabla f(x_t))
    $$
    
    $$
    곡면의 변화량=r_{t+1}=\nabla f(x_1)^2, \nabla f(x_2)^2, \cdots, \nabla f(x_t)^2
    $$
    
- 적응적 학습률 : 곡면의 변화량에 반비례
    
    $$
    r_{t+1}=r_t+\nabla f(x_t)^2
    $$
    
    $$
    x_{t+1}=x_t-\frac{\alpha}{\sqrt {r_{t+1}}+\epsilon} \odot\nabla f(x_t)
    $$
    

## 2. 학습 초반에 학습이 중단되는 현상

- 곡면 변화량을 전체 경로의 기울기 벡터의 크기로 계산 → 적응적 학습률 낮아짐

# 5. RMSProp

## 1. 핵심 개념

- RMSProp(Root Mean Square Propagation) : 최근 경로의 곡면 변화량에 따라 학습률을 적응적으로 결정하는 알고리즘
- 전체 경로가 아닌 최근 경로의 변화량 측정
- 지수가중이동평균(Exponentially Weighted Moving Average)
    
    $$
    r_{t+1}=\beta r_t+(1-\beta)\nabla f(x_t)^2
    $$
    
    $$
    x_{t+1}=x_t-\frac{\alpha}{\sqrt {r_{t+1}}+\epsilon} \odot\nabla f(x_t)
    $$
    

## 2. 최근 경로의 곡면 변화량

$$
r_{t+1}=\beta^tr_1+(1-\beta)(\nabla f(x_t)^2+\beta\nabla f(x_{t-1})^2+\cdots+\beta^{t-1}\nabla f(x_1)^2)
$$

- 최근 경로의 그레이디언트는 많이 반영되고 오래된 경로의 그레이디언트는 작게 반영됨

# 6. Adam

## 1. 핵심 개념

- Adam(Adaptive Moment Estimation) : SGD 모멘텀 + RMSProp, 진행하던 속도에 관성을 주고 동시에 최근 경로의 곡면의 변화량에 따라 적응적 학습률을 갖는 알고리즘
- 1차 관성(First Momemtum) : 속도 계산
    
    $$
    v_{t+1}=\beta_1v_t+(1-\beta_1)\nabla f(x_t)
    $$
    
- 2차 관성(Second Momemtum) : 그레이디언트 제곱의 지수가중이동평균을 구하는 식
    
    $$
    r_{t+1}=\beta_2r_t+(1-\beta_2)\nabla f(x_t)^2
    $$
    
    $$
    x_{t+1}=x_t-\frac{\alpha}{\sqrt {r_{t+1}}+\epsilon} \odot\nabla f(x_t)
    $$
    

## 2. 학습 초기 경로 편향 문제

### 1. 초기 경로에 편향이 발생하는 이유

- $r_1$이 작아짐 → 적응적 학습률이 커짐 → 출발 지점에서 멀리 떨어진 곳으로 이동

### 2. 초기 경로의 편향 제거

- $r_1$ → 그레이디언트 제곱 → 학습률이 급격히 커지는 편향 제거
