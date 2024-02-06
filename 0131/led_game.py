import RPi.GPIO as GPIO
import random
import time

# GPIO 핀 번호 설정
LED_RED = 4
LED_GREEN = 5
LED_BLUE = 6

# GPIO 핀 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

# LED 초기화
GPIO.output(LED_RED, GPIO.LOW)
GPIO.output(LED_GREEN, GPIO.LOW)
GPIO.output(LED_BLUE, GPIO.LOW)

# 게임 시작
print("------------------------------------------------")
print("                빛의 삼원색 게임 ")
print("- 색을 확인하고 합쳐지면 어떤 색이 되는지 맞춰보자 -")
print("------------------------------------------------\n")

# 랜덤 색 2개 or 3개 선정
randColor = [0, 0, 0]
if random.randint(0, 2) != 0:
    # 화이트 이외의 다른 색
    randColor[0] = random.randint(1, 3)
    randColor[1] = random.randint(1, 3)
    while randColor[0] == randColor[1]:
        randColor[1] = random.randint(1, 3)
else:
    # 화이트가 되는 경우
    randColor[2] = 7

# 랜덤 색 출력
time.sleep(1)
if randColor[2] == 7:
    GPIO.output(LED_RED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_BLUE, GPIO.LOW)
else:
    # 다른 색인 경우
    if randColor[0] == 1:
        GPIO.output(LED_RED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_RED, GPIO.LOW)
    elif randColor[0] == 2:
        GPIO.output(LED_GREEN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_GREEN, GPIO.LOW)
    elif randColor[0] == 3:
        GPIO.output(LED_BLUE, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_BLUE, GPIO.LOW)

    if randColor[1] == 1:
        GPIO.output(LED_RED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_RED, GPIO.LOW)
    elif randColor[1] == 2:
        GPIO.output(LED_GREEN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_GREEN, GPIO.LOW)
    elif randColor[1] == 3:
        GPIO.output(LED_BLUE, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_BLUE, GPIO.LOW)

# 선택 옵션 출력
print("---------------------------")
print("1. yellow")
print("2. magenta")
print("3. cyan")
print("4. white")
print("---------------------------\n")

# 답 입력 받기
number = int(input("숫자를 입력하세요: "))

# 정답일 경우
if number + 2 == randColor[0] + randColor[1] or number + 3 == randColor[2]:
    print("정답입니다.")
    GPIO.output(LED_RED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_GREEN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_BLUE, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.LOW)
else:
    # 오답일 경우
    print("오답입니다.")
    GPIO.output(LED_RED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_RED, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LED_RED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_RED, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LED_RED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_RED, GPIO.LOW)

GPIO.cleanup()