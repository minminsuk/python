from turtle import TurtleScreen, RawTurtle, TK  # 터틀 및 TKinter 모듈 임포트

def main():  # main 함수 정의 시작
    # TKinter 설정
    root = TK.Tk()  # TKinter 윈도우(root) 생성
    cv1 = TK.Canvas(root, width=300, height=200, bg="#ddffff")  # 첫 번째 캔버스 생성 (배경색: 연한 청록)
    cv2 = TK.Canvas(root, width=300, height=200, bg="#ffeeee")  # 두 번째 캔버스 생성 (배경색: 연한 분홍)
    cv1.pack()  # 첫 번째 캔버스를 창에 배치
    cv2.pack()  # 두 번째 캔버스를 창에 배치

    # TurtleScreen 및 RawTurtle 설정
    screen1 = TurtleScreen(cv1)  # 첫 번째 캔버스를 기반으로 TurtleScreen 생성
    screen1.bgcolor(0.5, 0.5, 1)  # screen1의 배경색 설정 (RGB 비율)
    screen2 = TurtleScreen(cv2)  # 두 번째 캔버스를 기반으로 TurtleScreen 생성
    screen2.bgcolor(1, 0.5, 0.5)  # screen2의 배경색 설정 (RGB 비율)

    t1 = RawTurtle(screen1)  # screen1에 터틀 객체 t1 생성
    t2 = RawTurtle(screen2)  # screen2에 터틀 객체 t2 생성

    for t in (t1, t2):  # t1과 t2 두 터틀 객체에 대해 반복
        t.shape("turtle")  # 터틀 모양 설정

    # 사용자 입력에 따라 도형 그리기
    s = screen1.textinput("", "도형을 입력하시오 (사각형/원/삼각형/별): ")  # 사용자로부터 도형 종류 입력 받음
    if s == "사각형":  # 입력값이 "사각형"인 경우
        w = int(screen1.textinput("", "가로 길이를 입력하시오: "))  # 가로 길이 입력 받고 정수로 변환
        h = int(screen1.textinput("", "세로 길이를 입력하시오: "))  # 세로 길이 입력 받고 정수로 변환
        for t in (t1, t2):  # t1과 t2에 대해 반복하여 사각형 그리기
            for _ in range(2):  # 사각형은 두 쌍의 변으로 구성되므로 2회 반복
                t.forward(w)  # 가로 길이만큼 전진
                t.right(90)   # 90도 오른쪽 회전
                t.forward(h)  # 세로 길이만큼 전진
                t.right(90)   # 90도 오른쪽 회전
    elif s == "원":  # 입력값이 "원"인 경우
        r = int(screen1.textinput("", "반지름을 입력하시오: "))  # 반지름 입력 받고 정수로 변환
        for t in (t1, t2):  # t1과 t2에 대해 반복하여 원 그리기
            t.circle(r)  # 반지름 r을 가진 원을 그림
    elif s == "삼각형":  # 입력값이 "삼각형"인 경우
        l = int(screen1.textinput("", "한 변의 길이를 입력하시오: "))  # 한 변의 길이 입력 받고 정수로 변환
        for t in (t1, t2):  # t1과 t2에 대해 반복하여 삼각형 그리기
            for _ in range(3):  # 삼각형은 3변이 있으므로 3회 반복
                t.forward(l)  # 변의 길이만큼 전진
                t.left(120)   # 120도 왼쪽 회전 (삼각형 내각에 맞게 회전)
    elif s == "별":  # 입력값이 "별"인 경우
        size = int(screen1.textinput("", "별의 크기를 입력하시오: "))  # 별 그리기에 사용할 크기를 입력 받고 정수로 변환
        for t in (t1, t2):  # t1과 t2에 대해 반복하여 별 그리기
            for _ in range(5):  # 별은 5개의 꼭짓점이 있으므로 5회 반복
                t.forward(size)  # 지정된 크기만큼 전진
                t.right(144)  # 별 모양을 위해 144도 오른쪽 회전
    else:  # 입력값이 위 도형들 중에 없을 경우
        screen1.textinput("", "알 수 없는 도형입니다. 프로그램을 종료합니다.")  # 경고 메시지 표시
        return  # 함수 종료

if __name__ == '__main__':  # 스크립트가 직접 실행될 때
    main()  # main 함수 호출하여 실행
    TK.mainloop()  # TKinter 이벤트 루프 실행, 창이 닫히지 않도록 유지