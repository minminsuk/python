# 사용자로부터 정수를 입력받음
n = int(input("정수를 입력하세요: "))

if n < 5:
    # 입력받은 정수만큼 피라미드 출력
    for i in range(1, n + 1):
        print("*" * i)
else:
    # 정수가 5 이상일 경우 피라미드 출력 후 거꾸로 된 피라미드 출력
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(n - 1, 0, -1):
        print("*" * i)