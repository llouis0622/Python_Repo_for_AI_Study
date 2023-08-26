print("구구단 몇단을 계산할까요? ")
dan = int(input())
print(f"구구단 {dan}단을 계산합니다.")
for i in range(1, 10):
    print(f"{dan} X {i} = {dan*i}")