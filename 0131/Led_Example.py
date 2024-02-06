#파이썬으로 라즈베리파이 LED 제어하기

import RPi.GPIO as GPIO #RPi.GPIO 모듈을 GPIO 이름으로 사용
import time #time 모듈
import random #random 모듈

# LED 핀 번호 설정
LED_RED = 7
LED_GREEN = 29
LED_BLUE = 31

# 랜덤 패턴을 저장할 배열
pattern = []

# 밝기 정도 pwm 설정
BRIGHT_VALUE = 100

# 시간 설정
BRIGHT_TIME = 0.1

#점등 패턴 설정
# 빨강 빨강 파랑 파랑 초록 초록 아래는 예시 입니다.
pattern1 = [LED_RED, LED_RED, LED_BLUE, LED_BLUE, LED_GREEN, LED_GREEN]

GPIO.setmode(GPIO.BOARD) 

# 각 LED 핀을 출력으로 설정
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

# PWM 객체 생성
red_pwm = GPIO.PWM(LED_RED, 100)
green_pwm = GPIO.PWM(LED_GREEN, 100)
blue_pwm = GPIO.PWM(LED_BLUE, 100)

# LED 배열을 랜덤하게 생성하는 함수
def generatePattern():
    return [random.choice([LED_RED, LED_GREEN, LED_BLUE]) for i in range(6)]# 6개의 LED를 랜덤하게 생성

# 모든 LED를 꺼주는 함수
def LEDAllOff():
    GPIO.output(LED_RED, 0)
    GPIO.output(LED_GREEN, 0)
    GPIO.output(LED_BLUE, 0)
    
# 패턴과 시간을 입력받고 해당 패턴을 시간만큼 점등하는 함수
def LEDPattern(pattern, time1):
    for i in pattern:
        GPIO.output(i, 1)
        time.sleep(time1)
        GPIO.output(i, 0)
        time.sleep(time1)
               
# 오답이었을때 빨강 점등 점멸
def LEDWrong():
    for i in range(3):
        GPIO.output(LED_RED, 1)
        time.sleep(0.5)
        GPIO.output(LED_RED, 0)
        time.sleep(0.5)

# 정답이었을때 초록 점등 점멸
def LEDCorrect():
    for i in range(3):
        GPIO.output(LED_GREEN, 1)
        time.sleep(0.5)
        GPIO.output(LED_GREEN, 0)
        time.sleep(0.5)
            
# 메인 동작 구간     
# 1. 모든 LED를 꺼준다.
LEDAllOff()
# 2. 질문 
print("안녕하세요 라즈베리파이 LED 패턴 암기 게임입니다.")
time.sleep(1)
print("패턴이 랜덤하게 생성 되어 LED가 점등됩니다.")
time.sleep(1)
print("6개의 패턴을 기억한 후 패턴이 끝나면 정답을 입력해주세요.")
time.sleep(1)
print("아무 키나 누르면 시작합니다.")
input()
# 3. 랜덤 패턴 생성
print("패턴 생성중...")
pattern = generatePattern()
# 4. 패턴 점등
LEDPattern(pattern, 1)
# 5. 정답 입력
print("정답을 입력해주세요. 빨강 = 7, 초록 = 29, 파랑 = 31")
# 플레이어의 정답을 새로운 배열에 저장(배열의 크기는 6)
player_pattern = [0 for i in range(6)]
# 플레이어의 정답을 입력받는다.
for i in range(6):
    player_pattern[i] = int(input())
# 6. 정답 확인
if pattern == player_pattern:
    print("정답입니다!")
    LEDCorrect()
else:
    print("오답입니다!")
    print("정답은 ", pattern, " 입니다.")
    LEDWrong()
    








