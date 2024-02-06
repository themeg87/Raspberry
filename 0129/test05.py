#월요일에 네이버의 주가가 100만 원으로 시작해 3일 연속으로 하한가(-30%)를 기록했을 때 수요일의 종가를 계산해 보세요.

mon_naver = 1000000
mang = mon_naver * 0.3

for i in range(3):
    mon_naver = mon_naver * 0.7
    print(f"{i+1}일, {mon_naver}원")
    