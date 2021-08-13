N, B = input().split()

B = int(B)

answer = 0
pow = 0

# ["Z","Z","Z","Z"]를 거꾸로 가져오기
# ["Z","Z","Z","Z"]
for i in N[::-1]:
# for i in N:
    # 숫자일 땐 그대로 출력
    if i.isdigit():
        j = int(i)

    # 알파벳일 때 ASCII - 55
    else:
        j = ord(i) - 55

    # B의 제곱근 * 진법
    print(i)
    answer += (j * (B ** pow))
    pow += 1

print(answer)