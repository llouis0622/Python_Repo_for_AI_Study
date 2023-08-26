print("구구단 몇단을 계산할까요?")

while True:
    dan = int(input())
    if 1 <= dan and dan <= 9:
        print(f"구구단 {dan}단을 계산합니다.")
        for i in range(1, 10):
            print(f"{dan} X {i} = {dan*i}")
    elif dan == 0:
        print("구구단 게임을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다.")