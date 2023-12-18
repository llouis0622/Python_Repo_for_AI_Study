# 08장. 순환 신경망

# 1. 기억을 갖는 신경망 모델 RNN

- 순차 데이터(Sequence Data) : 시간적 공간적 순서 관계가 있는 데이터
- 시공간의 순서 관계로 형성되는 문맥, 콘텍스트를 가짐

## 1. 연상 기억을 하는 홉필드 네트워크

- 연상 메모리 : 기억 저장, 연상
- 새로운 입력이 들어오면 특정 패턴으로 수렴하게 만들어 기억해둔 패턴 연상
- 순환 연산을 통해 입력 데이터의 패턴 연상

## 2. 기억을 전달하는 순환 신경망(RNN, Recurrent Neural Network)

- 데이터의 순차 구조 인식, 데이터의 콘텍스트 범위가 넓더라도 처리 가능

### 1. 순차 구조를 인식하며 콘텍스트를 기억하는 모델 구조

- 데이터를 시간 순서대로 하나씩 입력받음
- 은닉 계층에 피드백 연결을 가짐
- 은닉 상태 : 시간 단계별로 입력된 데이터가 순차적으로 추상화되어 형성된 콘텍스트
- 피드백 연결 : 시간의 흐름에 따라 콘텍스트를 기억하는 과정

### 2. 순환 연결 방식

- 입력 계층은 새로운 입력 데이터를 입력받음
- 이전 상태와 입력 데이터를 합침
- 함수를 실행해서 은닉 상태 출력
- 함수는 순환 신경망의 종류에 따라 달라짐, 은닉 계층의 가중치 적용
- 은닉 상태는 출력 계층과 다음 단계의 은닉 계층에 전달
- 출력 계층은 은닉 상태를 입력받아 뉴련 연산 후 출력

### 3. 기본 순환 신경망 모델

$$
h_t=\tanh(W_{hh}h_{t-1}+W_{xh}x_t)
\\=\tanh((W_{hh}W_{xh})\begin{pmatrix} h_{t-1} \\ x_t \end{pmatrix})
\\=\tanh(W\begin{pmatrix} h_{t-1} \\ x_t \end{pmatrix}), \ W=(W_{hh}W_{xh})
$$

## 3. 순환 신경망의 입력, 은닉 상태, 출력

$$
h_1=f_w(h_0, \ x_1)
\\ h_2=f_w(h_1, \ x_2)
\\ \cdots
\\ h_t=f_w(h_{t-1}, \ x_t)
$$

$$
h_t=f_w(f_w(\cdots f_w(f_w(f_w(h_0, \ x_1), x_2), x_3), \cdots, x_{t-1}), x_t)
$$

$$
h_t=f_w(h_{t-1}, \ x_t)
$$

- 순차 구조 포착 가능
- 가변 길이 데이터 처리 쉬움
- 파라미터 수 절약, 정규화 효과

# 2. 순환 신경망의 주요 모델

## 1. 다대일 모델(Many-to-One)

- 입력은 순차열, 출력은 순차열이 아님
- 모든 단계에서 입력, 마지막 단계에서만 출력

## 2. 다대다 모델(Many-to-Many)

- 입출력의 길이가 같은 순차열일 때 사용
- 모든 단계에서 입력, 모든 단계에서 출력
- 티처 포싱(Teacher Forcing) : 현재 단계의 출력을 다음 단계에 입력하는 방법

## 3. 일대다 모델(One-to-Many)

- 입력은 순차열이 아님, 출력은 순차열
- 첫 번째 단계에서만 입력, 모든 단계에서 출력

## 4. 양방향 모델(Bidirectional)

- 입력을 양쪽으로 살펴봄
- 공간적 순서 관계 → 상대적인 순서

## 5. 인코더-디코더 모델(Encoder-Decoder)

- 입력과 출력의 길이가 서로 다른 순차열
- 인코더 : 입력 데이터 요약
- 디코더 : 요약 데이터 → 출력 데이터 생성
- Seq2Seq(Sequence-to-Sequence) 모델

# 3. 시간펼침 역전파(BPTT, BackPropagation Through Time)

## 1. 순환 신경망의 손실 함수

- 시간 순서대로 펼쳐 놓은 상태에서 정의
- 회귀 문제 : 평균제곱오차
- 분류 문제 : 크로스 엔트로피
    
    $$
    L_1=J(f(x_1; \ \theta), \ t_1)
    \\ L_2=J(f(x_1, x_2; \ \theta), \ t_2)
    \\ L_3=J(f(x_1, x_2, x_3; \ \theta), \ t_3)
    \\ L_4=J(f(x_1, x_2, x_3, x_4; \ \theta), \ t_4)
    $$
    
    $$
    J(f(X; \ \theta), \ t)=L_1+L_2+L_3+L_4
    $$
    

## 2. 시간펼침 역전파

![1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/81ce352b-f505-4b7c-ba55-561d76267295/fcdbc3fc-a593-49cc-9cb5-bad5486a8cb2/1.png)

- 시간의 역순으로 모든 은닉 계층을 따라 단계별로 은닉 계층에서 입력 계층으로 역전파 분기
- 영향을 미친 모든 단계에서 오차가 역전파되어 돌아옴
- 역전파는 마지막 단계에서 시작해서 시간의 역순으로 단계별로 순차 진행

## 3. 절단 시간펼침 역전파(Truncated BPTT)

- 일정 단계를 묶어서 순방향 진행을 하고 역전파를 실행
- 묶음 단위로 역전파 → 묶음 간 은닉 상태 전달 → 연속된 콘텍스트

# 4. LSTM(Long Short-Term Memory)과 GRU(Gated Recurrent Unit)

## 1. 기본 순환 신경망의 문제점

- 장기의존성(Long-Term Dependency) : 콘텍스트 범위가 넓을 때 멀리 떨어진 입력에 대한 의존성이 있음에도 불구하고 입력의 영향이 점점 사라지는 현상
- 그레이디언트 소실과 폭발(Gradient Vanishing and Exploding) : 학습하면서 그레이디언트가 없어지거나 발산하는 현상
    
    $$
    h_t=\tanh((W_{hh}W_{xh})\begin{pmatrix} h_{t-1} \\ x_t \end{pmatrix})=\tanh(W\begin{pmatrix} h_{t-1} \\ x_t \end{pmatrix})
    $$
    
- 그레이디언트 클리핑(Gradient Clipping) : 그레이디언트가 일정 크기 이상으로 커지지 않게 함
    
    $$
    g\leftarrow\frac{g}{\|g\|}v, \ \text{if}\|g\|>v
    $$
    

## 2. LSTM

- 그레이디언트 소실의 원인이 되는 가중치 $W$와의 행렬곱 연산이 그레이디언트 경로에 나타나지 않도록 구조를 변경한 모델
- 그레이디언트 소실을 막기 위한 별도의 셀 상태 추가
- 셀 상태 : 뇌의 장기 기억
    - 셀 상태를 $W$의 방해 없이 그대로 전달되는 구조
- 은닉 상태 : 뇌의 단기 기억
    - 은닉 상태에 최근 사건에 대한 콘텍스트가 형성되도록 $W$가 곱해지는 구조
- 망각 게이트(Forget Gate) : 장기 기억을 지속할지 잊을지 판단
- 입력 게이트(Input Gate) : 새로운 사건으로 형성된 기억 중 장기 기억으로 전환해야 할 기억 선택
- 기억 게이트(Remember Gate) : 장기 기억을 새롭게 갱신하기 위해 망각 게이트를 통과한 장기 기억에 입력 게이트를 통과한 새로운 기억을 더함
- 출력 게이트(Output Gate) : 갱신된 장기 기억에서 갱신된 단기 기억에 필요한 기억 선택
    
    $$
    \begin{pmatrix} i_t \\ f_t \\ o_t \\ g_t \end{pmatrix}=\begin{pmatrix} \sigma \\ \sigma \\ \sigma \\ \tanh \end{pmatrix}W\begin{pmatrix} h_{t-1} \\ x_t \end{pmatrix}, \ W=\begin{bmatrix} W_{hi} & W_{xi} \\ W_{hf} & W_{xf} \\ W_{ho} & W_{xo} \\ W_{hg} & W_{xg} \end{bmatrix}
    $$
    
    $$
    C_t=f_t\odot C_{t-1}+i_t\odot g_t
    $$
    
    $$
    h_t=o_t\odot \tanh(C_t)
    $$
    
    $$
    \frac{\partial{C_t}}{\partial{C_{t-1}}}=f_t
    $$
    

## 3. GRU

- LSTM의 장점을 유지하면서 게이트 구조를 단순하게 만든 순환 신경망
- 리셋 게이트(Reset Gate) : 새로운 사건이 발생했을 때 기억을 새롭게 형성하기 위해 장기 기억과 단기 기억에서 필요한 부분 선택
- 업데이트 게이트(Update Gate) : 기억을 갱신하기 위해 기존 기억과 새롭게 형성된 기억의 가중 평균을 계산하는 가중치 역할
    
    $$
    \begin{pmatrix} r_t \\ z_t \end{pmatrix}=\begin{pmatrix} \sigma \\ \sigma \end{pmatrix}W\begin{pmatrix} h_{t-1} \\ x_t \end{pmatrix}, W = \begin{bmatrix} W_{hr} & W_{xr} \\ W_{hz} & W_{xz} \end{bmatrix}
    $$
    
    $$
    \tilde{h}_t=\tanh((W_{hh}W_{xh})\begin{pmatrix} r_t\odot h_{t-1} \\ x_t \end{pmatrix})
    $$
    
    $$
    h_t=(1-z)\odot h_{t-1}+z_t\odot\tilde{h}_t
    $$
    

# 5. 순환 신경망 개선

## 1. 어텐션(Attention)

- 모든 기억을 동등하게 기억하지 않고 연관성 있는 기억에 집중해서 기억하도록 구조화
- 어텐션값(Attention Value) : 연관성
    
    $$
    어텐션=\text{attention}(q, k, v)
    $$
    
- 어텐션 점수(Attention Score) : 쿼리와 키의 연관 정도
    
    $$
    \text{score}(q, k)=\frac{q^Tk}{\sqrt{n}}
    $$
    
    $$
    \text{softmax}(\text{score}(q, k))
    $$
    
- 셀프 어텐션(Self Attention) : 자기 자신을 구성하는 부분끼리 연관성을 찾고자 할 때 사용
- 하드 어텐션(Hard Attention) : 가장 집중하는 정보를 선택, 최댓값
- 소프트 어텐션(Soft Attention) : 어텐션 점수를 가중치로 사용해서 전체 정보를 가중 합산

## 2. 인코더-디코더에서 어텐션 사용

- 디코더가 새로운 단어 생성 → 입력 문장에서 연관된 단어 정보 가져옴 → 인코더의 모든 은닉 상태와 어텐션 계산

## 3. 트랜스포머에서 어텐션 사용

- 트랜스포머(Transformer) : 순환 신경망을 사용하지 않고 순수하게 어텐션 메커니즘으로 구성된 인코더-디코더 모델
    
    $$
    \text{attention}(Q, K, V)=\text{softmax}(\frac{QK^T}{\sqrt{d_k}})V
    $$
    

## 4. 시간 팽창 콘벌루션(Temporal Dilated Convolution)

- 순환 구조는 사용하지 않고 긴 콘텍스트를 다루기 위해 오래 전 기억이 빠르게 전달되도록 함
- 오디오 생성 모델 웨이브넷
- 메타러닝 모델 SNAIL
