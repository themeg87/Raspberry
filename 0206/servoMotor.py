#
#      공대선배 라즈베리파이썬 #20 python flask 10편
#      youtube 바로가기: https://www.youtube.com/c/공대선배
#      웹사이트의 버튼, 슬라이더 바를 이용해 서보모터를 제어하는 코드
#
from flask import Flask, render_template, request   # flask 모듈과 관련함수 불러옴
import RPi.GPIO as GPIO     # 라즈베리파이 GPIO 관련 모듈을 불러옴
import time                 # 시간 관련 모듈을 불러옴


GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정

servo_pin = 14                   # 서보핀은 라즈베리파이 GPIO 14번핀으로 

GPIO.setup(servo_pin, GPIO.OUT)  # 서보핀을 출력으로 설정 
servo = GPIO.PWM(servo_pin, 50)  # 서보핀을 PWM 모드 50Hz로 사용
servo.start(0)  # 서보모터의 초기값을 0으로 설정

servo_min_duty = 3               # 최소 듀티비를 2으로
servo_max_duty = 12              # 최대 듀티비를 13로
current_deg = 90                 # 현재 각도를 90도로
def set_servo_degree(degree):    # 각도를 입력하면 듀티비를 알아서 설정해주고 서보모터를 움직이는 함수
    # #8.5편에 나온 방법대로 서보모터가 떨리지 않게 함
    # 각도는 최소0, 최대 180으로 설정
    GPIO.setup(servo_pin, GPIO.OUT)         # 모터를 움직여야 하니 서보핀을 출력으로 설정
    past_time = time.time()                 # 과거 시간을 기록
    if degree > 180:                        # 입력받은 각도를 0~180도 사이로 재조정
        degree = 180
    elif degree < 0:
        degree = 0
    duty = servo_min_duty+(degree*(servo_max_duty-servo_min_duty)/180.0)    # 각도를 듀티비로 환산
    # 환산한 듀티비를 서보모터에 전달
    servo.ChangeDutyCycle(duty)             # 해당 각도대로 서보모터를 움직임
    while True:                             # 이부분은 sleep(0.5)와 같음(움직이는 시간동안 대기)
        current_time = time.time()
        if current_time - past_time > 0.5:
            break
    GPIO.setup(servo_pin, GPIO.IN)          # 0.5초간 기다린 후 서보핀을 입력으로 설정(서보모터가 움직이지 않음)
    return degree                           # 입력받은 각도를 출력
    
    
set_servo_degree(current_deg)
app = Flask(__name__)               # Flask라는 이름의 객체 생성
@app.route('/')                     # 기본 주소
def home():                         # 여기서 servoMotor.html을 화면에 보여주며, 서보모터 각도를 전달
    return render_template(‘servomotor.html', deg=current_deg)  

@app.route('/servo_control')        # 서보모터를 제어하기 위한 주소
def servo_control():                # 서보모터를 제어하기 위한 뷰함수
    deg = request.args.get('deg')   # html파일에서 각도를 입력받음
    deg = int(deg)                  # 각도를 정수형으로 바꿔주고 적절한 범위로바꿔줌
    if deg < 0: deg = 0
    elif deg > 180: deg = 180
    deg = set_servo_degree(deg)     # 서보모터 각도를 바꿔줌
    # index#20.html로 돌아가는데, 이때, deg 값을 넘겨줌(이 넘겨준 값은 html에서 사용할 수 있음)
    return render_template('index4#20.html', deg=deg)

if __name__ == "__main__":  # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분
   app.run(host="192.168.1.4", port = "8080")
   # host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정
   # 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능