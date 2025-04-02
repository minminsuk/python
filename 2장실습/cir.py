PI = 3.141592
radius = float(input("반지름을 입력하세요: "))
circumference = 2 * PI * radius
area = PI * radius ** 2
print(f"반지름이 {radius}인 원의 둘레는 {circumference:.2f}입니다.")
print(f"반지름이 {radius}인 원의 면적은 {area:.2f}입니다.")