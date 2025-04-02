def calculate_rfm():
    try:
        gender = int(input("여성이면 1, 남성이면 0을 입력하세요: "))
        if gender not in [0, 1]:
            print("잘못된 입력입니다. 0 또는 1을 입력하세요.")
            return

        height = float(input("키(cm)를 입력하세요: "))
        waist = float(input("허리둘레(cm)를 입력하세요: "))
        if gender == 1:
            rfm = 76 - (20 * (height / waist))
        else:
            rfm = 64 - (20 * (height / waist))

        print(f"당신의 RFM은 {rfm:.2f} 입니다.")
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력하세요.")
if __name__ == "__main__":
    calculate_rfm()