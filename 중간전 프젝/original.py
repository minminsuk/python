from turtle import TurtleScreen, RawTurtle, TK  # 터틀 모듈과 TKinter를 불러옴

def main():
    # TKinter 창과 두 개의 캔버스 생성
    root = TK.Tk()  # TKinter 윈도우 생성
    cv1 = TK.Canvas(root, width=300, height=200, bg="#ddffff")  # 첫 번째 캔버스 생성 (배경색: 연한 청록)
    cv2 = TK.Canvas(root, width=300, height=200, bg="#ffeeee")  # 두 번째 캔버스 생성 (배경색: 연한 분홍)
    cv1.pack()  # 첫 번째 캔버스를 창에 배치
    cv2.pack()  # 두 번째 캔버스를 창에 배치

    # 두 개의 TurtleScreen 생성 및 배경색 설정
    s1 = TurtleScreen(cv1)  # 첫 번째 캔버스를 기반으로 TurtleScreen 생성
    s1.bgcolor(0.85, 0.85, 1)  # 첫 번째 TurtleScreen의 배경색 설정
    s2 = TurtleScreen(cv2)  # 두 번째 캔버스를 기반으로 TurtleScreen 생성
    s2.bgcolor(1, 0.85, 0.85)  # 두 번째 TurtleScreen의 배경색 설정

    # 두 개의 터틀 객체 생성
    p = RawTurtle(s1)  # 첫 번째 TurtleScreen에 터틀 생성
    q = RawTurtle(s2)  # 두 번째 TurtleScreen에 터틀 생성

    # 터틀 p와 q의 색상과 굵기 설정
    p.color("red", (1, 0.85, 0.85))  # 터틀 p의 펜 색상과 채우기 색상 설정 (붉은 계열)
    p.width(3)  # 터틀 p의 선 굵기 3으로 설정
    q.color("blue", (0.85, 0.85, 1))  # 터틀 q의 펜 색상과 채우기 색상 설정 (푸른 계열)
    q.width(3)  # 터틀 q의 선 굵기 3으로 설정

    # 두 터틀의 모양 설정 및 초기 회전
    for t in p, q:
        t.shape("turtle")  # 터틀 모양으로 설정
        t.lt(36)  # 왼쪽으로 36도 회전

    q.lt(180)  # 터틀 q를 추가로 180도 회전시켜 반대 방향으로 향하게 함

    # 채우기 시작: 별 모양 그리기를 위한 준비
    for t in p, q:
        t.begin_fill()  # 채우기 시작

    # 오각형 그리기 위한 반복: 5번 반복
    for i in range(5):
        for t in p, q:
            t.fd(50)  # 터틀을 앞으로 50 이동
            t.lt(72)  # 왼쪽으로 72도 회전

    # 채우기 종료 및 추가 동작: 채운 영역을 마감하고 각도를 조정, 터틀을 후진시키기
    for t in p, q:
        t.end_fill()  # 채우기 종료
        t.lt(54)      # 왼쪽으로 54도 회전
        t.pu()        # 펜 올리기 (이동 중 그리지 않음)
        t.bk(50)      # 50만큼 후진

    return "EVENTLOOP"  # 이벤트 루프 상태를 나타내는 문자열 반환

if __name__ == '__main__':
    main()  # main 함수 실행
    TK.mainloop()  # TKinter 이벤트 루프 실행, 창이 닫히지 않도록 유지