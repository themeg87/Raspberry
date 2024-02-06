#
#      공대선배 라즈베리파이썬 #14 python flask 4편
#      youtube 바로가기: https://www.youtube.com/c/공대선배
#      웹사이트에서 라즈베리파이의 현재 상태(스위치 눌림 여부, 센서값 등)를 확인하는 코드
#
from flask import Flask, render_template   # flask 모듈과 관련함수 불러옴
import RPi.GPIO as GPIO     # 라즈베리파이 GPIO 관련 모듈을 불러옴

sw_pin_list = [14, 15, 18]  # 3개의 스위치 핀을 list형 변수로 선언
GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정
app = Flask(__name__)       # Flask라는 이름의 객체 생성

# 각각의 스위치 핀들을 풀다운 저항이 있는 입력으로 설정
GPIO.setup(sw_pin_list[0], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)   
GPIO.setup(sw_pin_list[1], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sw_pin_list[2], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
sw_state_list = [0, 0, 0]   # 스위치의 눌림여부를 기록한 list형 변수 선언

@app.route('/')                       # 기본 주소
def home():
    for ii in range(3):               # 스위치의 눌림여부를 현황 변수에 저장
        sw_state_list[ii] = GPIO.input(sw_pin_list[ii]) 
    return render_template(‘buttonState.html', sw_state_list = sw_state_list)   
    #buttonState.html에 스위치의 눌림 여부 현황을 전달

if __name__ == "__main__":  # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분
   app.run(host="192.168.0.46", port = "8080")
   # host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정
   # 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능
