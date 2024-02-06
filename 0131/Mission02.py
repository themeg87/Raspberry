#Mission 2
import RPi.GPIO as GPIO #RPi.GPIO 모듈을 GPIO 이름으로 사용
import time #time 모듈

# LED 핀 번호 설정
LED_RED = 7
LED_GREEN = 29
LED_BLUE = 31

# 밝기 정도 pwm 설정
BRIGHT_VALUE = 100

# 시간 설정
BRIGHT_TIME = 3

GPIO.setmode(GPIO.BOARD) 

# 각 LED 핀을 출력으로 설정
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

# PWM 객체 생성
red_pwm = GPIO.PWM(LED_RED, 100)
green_pwm = GPIO.PWM(LED_GREEN, 100)
blue_pwm = GPIO.PWM(LED_BLUE, 100)

# 밝기 정도 pwm 설정
BRIGHT_VALUE = 100

# 시간 설정
BRIGHT_TIME = 3

# LED를 켜주는 함수
def LEDOn(led):
    led.start(BRIGHT_VALUE)
    
# LED를 꺼주는 함수
def LEDOff(led):
    led.stop()
    
# LED 3초간 점점 밝아지게 하는 함수
def LEDBright(led):
    led.ChangeDutyCycle(0)  # 초기에 밝기를 0으로 설정
    time.sleep(1)
    for i in range(1, BRIGHT_VALUE + 1):
        led.ChangeDutyCycle(i)
        time.sleep(0.1)

# LED 3초간 점점 어두워지게 하는 함수
def LEDDark(led):
    for i in range(BRIGHT_VALUE, 0, -1):
        led.ChangeDutyCycle(i)
        time.sleep(0.1)
    led.ChangeDutyCycle(0)  # 마지막에 밝기를 0으로 설정

# LED 3초간 점점 밝다가 3초간 점점 어둡게 하는 함수
def LEDBrightDark(led):
    LEDBright(led)
    LEDDark(led)

# 원하는 초 입력받고 입력한 초 만큼 점점 밝아지다가 점점 어두워지는 함수
def LEDBrightDarkTime(led, time1):
    for i in range(BRIGHT_VALUE + 1):
        led.ChangeDutyCycle(i)
        time.sleep(time1 / BRIGHT_VALUE)
    for i in range(BRIGHT_VALUE, 0, -1):
        led.ChangeDutyCycle(i)
        time.sleep(time1 / BRIGHT_VALUE)
        
# 메인 동작
# 1. LED 켜기
LEDOn(red_pwm)
LEDOn(green_pwm)
LEDOn(blue_pwm)
time.sleep(1)
# 2. LED 끄기
LEDOff(red_pwm)
LEDOff(green_pwm)
LEDOff(blue_pwm)
time.sleep(1)
# 3. LED 점등
LEDBright(red_pwm)
LEDBright(green_pwm)
LEDBright(blue_pwm)
time.sleep(1)
# 4. LED 점멸
LEDDark(red_pwm)
LEDDark(green_pwm)
LEDDark(blue_pwm)
time.sleep(1)
# 5. LED 점등 점멸
LEDBrightDark(red_pwm)
LEDBrightDark(green_pwm)
LEDBrightDark(blue_pwm)
time.sleep(1)
# 6. LED 점등 점멸
LEDBrightDarkTime(red_pwm, 5)
LEDBrightDarkTime(green_pwm, 5)
LEDBrightDarkTime(blue_pwm, 5)
time.sleep(1)

    