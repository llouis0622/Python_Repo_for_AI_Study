import this

#결과 :
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# 1. True를 출력해 보세요.
True
# 결과 : True

# 2. False를 출력해 보세요.
False
# 결과 : False

# 3. True는 1과 같음을 표현해 보세요. 파이썬에서는 같음을 비교할 때 == 연산을 사용합니다.
False == 0
# 결과 : True

# 4. 하지만 True는 문자 1과 다릅니다. 1을 따옴표로 감싸면 문자열이 됩니다.
True == "1"
# 결과 : False

# 5. 문자열 1과 True는 다릅니다.
True != "1"
# 결과 : True

# 6. False도 마찬가지 입니다.
False = "0"
# 결과 : False

# 7. False는 문자열 0과 다릅니다.
False != "0"
# 결과 : True

# 8. and 연산으로 True 값 끼리 비교합니다.
#     and는 모든 값이 True 일때만 True가 됩니다.
True and True
# 결과 : True

# 9. and는 조건 중 하나라도 False라면 False가 됩니다.
True and False
# 결과 : False

# 10. or은 하나만 True 라도 True가 됩니다.
True or False
# 결과 : True

# "Hello World!"를 출력해 봅니다.
"Hello World!"
# 결과 : 'Hello World!'

# 주소 "경기도 성남시 분당구"를 출력해 봅니다.
"경기도 성남시 분당구"
# 결과 : '경기도 성남시 분당구'

# til 이라는 변수에 문자열을 담아봅니다.
til = "Today I Learned"
til
# 결과 : 'Today I Learned'

# 모두 소문자로 만들어 보세요.
til.lower()
# 결과 : 'today i learned'

# 모두 대문자로 만들어 보세요.
til.upper()
# 결과 : 'TODAY I LEARNED'

# 비어있는 리스트를 만듭니다. lang이라는 변수에 담습니다.
lang = []
lang
# 결과 : []

# python, java, c를 원소에 추가합니다.
lang.append("python")
lang.append("java")
lang.append("c")
lang
# 결과 : ['python', 'java', 'c']

# lang이라는 변수에 담겨있는 언어명을 인덱싱을 통해 가져옵니다.
lang[0]
# 결과 : 'python'

# 1번 인덱스를 가져옵니다.
lang[1]
# 결과 : 'java'

# 마지막 인덱스를 가져옵니다.
lang[-1]
# 결과 : 'c'

# 반복문을 통해 리스트의 원소를 하나씩 출력합니다.
for i in lang:
    print(i)
# 결과 : python
#           java
#           c

# 위 코드에서 python일 때는 그대로 출력하고 나머지 텍스트는 "기타"라고 출력합니다.
# 출력 결과가 아래의 순서로 나오도록 합니다.
# python
# 기타
# 기타
for i in lang:
    if i == "python":
        print("python")
    else:
        print("기타")
# 결과 : python
#           기타
#           기타

# 특정 횟수만큼 반복문을 실행하도록 합니다.
for i in range(5):
    print(i)
# 결과 : 0
#           1
#           2
#           3
#           4

# for문과 if문을 함께 사용해 봅니다.
# 짝수일 때 python을 홀수일 때 java를 출력합니다.
for i in range(1, 10):
    if i % 2 == 0:
        print("python")
    else:
        print("java")
# 결과: java
#          python
#          java
#          python
#          java
#          python
#          java
#          python
#          java

# enumerate를 사용하면 인덱스 번호와 원소를 같이 가져올 수 있습니다.
for i, val in enumerate(lang):
    print(i, val)
#결과 : 0 pyhon
#          1 java
#          2 c

# 주소를 address 변수에 담습니다.
address = " 경기도 성남시 분당구 불정로 6 NAVER 그린팩토리 16층"
address
# 결과 : '경기도 성남시 분당구 불정로 6 NAVER 그린팩토리 16층"

# 앞뒤 공백을 제거합니다.
# 데이터 전처리 시 주로 사용합니다.
address = address.strip()
address
# 결과 : '경기도 성남시 분당구 불정로 6 NAVER 그린팩토리 16층'

# 문자열의 길이
len(address)
# 결과 : 33

# 공백으로 문자열 분리
address_list = address.split()
address_list
# 결과 : ['경기도', '성남시', '분당구', '불정로', '6', 'NAVER', '그린팩토리', '16층']

# 리스트 길이
len(address_list)
# 결과 : 8

# 슬라이싱으로 문자 가져오기
address:[:2]
# 결과 : '경기'

# startswith를 사용하면 특정 문자가 포함되는지 여부를 확인할 수 있습니다.
address.startswith("경기")
# 결과 : True

# in을 사용하게 되면 특정 문자열을 포함하고 있는지 여부를 확인할 수 있습니다.
"경기" in address
# 결과 : True

# 인덱싱으로 리스트의 원소 가져오기 - 주소에서 구를 가져와 gu라는 변수에 담아보세요.
gu = address_list[2]
gu
# 결과 : '분당구'

# 인덱싱으로 리스트의 원소 가져오기 - 주소에서 도로명을 가져와 street라는 변수에 담아보세요
street = address_list[3]
street
# 결과 : '불정로'

# 리스트의 마지막을 가져옵니다.
address_list[-1]
# 결과 : '16층'

# "  ".join(리스트)를 사용하면 리스트를 공백 문자열을 연결할 수 있습니다.
# 리스트로 분리된 문자열을 다시 연결합니다.
" ".join(address_list)
# 결과 : '경기도 성남시 분당구 불정로 6 NAVER 그린팩토리 16층'

# in을 사용하게 되면 리스트에 해당 데이터를 포함하고 있는지 여부를 확인할 수 있습니다.
# "경기"가 리스트에 포함되는지를 봅니다.
"경기" in address_list
# 결과 : False --> "경기도" 처럼 완전하게 적어야 True가 나옵니다.

# in을 사용하게 되면 리스트에 해당 데이터를 포함하고 있는지 여부를 확인할 수 있습니다.
# "분당구"가 리스트에 포함되는지를 봅니다.
"분당구" in address_list
# 결과 : True