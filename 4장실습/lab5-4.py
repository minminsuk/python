n = int(input("정수를 입력하시오: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1

print(n, "!은", fact, "이다.")