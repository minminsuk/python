# 자신의 키(m)와 몸무게(kg)를 변수에 저장
height = 1.80  # 키 (미터 단위)
weight = 83    # 몸무게 (킬로그램 단위)

# BMI 계산
bmi = weight / (height ** 2)

# 결과 출력
print("키:", height, "m")
print("몸무게:", weight, "kg")
print("BMI:", round(bmi, 2))