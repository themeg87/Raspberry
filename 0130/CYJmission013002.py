import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# LED 켜기 함수
def turn_on_led():
    GPIO.output(LED_PIN, GPIO.HIGH)

# LED 끄기 함수
def turn_off_led():
    GPIO.output(LED_PIN, GPIO.LOW)

# LED 3초간 점점 밝게하기 함수
def fade_in_led():
    p = GPIO.PWM(LED_PIN, 100)
    p.start(0)
    for duty_cycle in range(0, 101, 5):
        p.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)
    p.stop()

# LED 3초간 점점 어둡게하기 함수
def fade_out_led():
    p = GPIO.PWM(LED_PIN, 100)
    p.start(100)
    for duty_cycle in range(100, -1, -5):
        p.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)
    p.stop()

# LED 3초간 점점 밝다가 3초간 점점 어둡기 함수
def fade_in_out_led():
    fade_in_led()
    fade_out_led()

# 밝아지고 어두워지는 시간을 입력으로 받아 LED를 점점 밝아지고 어둡게 하는 함수
def fade_led(duration):
    p = GPIO.PWM(LED_PIN, 100)
    p.start(0)
    steps = int(duration / 0.1)  # 0.1초마다 한 단계씩 증가 또는 감소
    for duty_cycle in range(0, 101, int(100 / steps)):
        p.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)
    for duty_cycle in range(100, -1, -int(100 / steps)):
        p.ChangeDutyCycle(duty_cycle)
        time.sleep(0.1)
    p.stop()


# 메뉴 출력
while True:
    print("1. LED 켜기")
    print("2. LED 끄기")
    print("3. LED 3초간 점점 밝게하기")
    print("4. LED 3초간 점점 어둡게하기")
    print("5. LED 3초간 점점 밝다가 3초간 점점 어둡기")
    print("6. 원하는 초 입력 입력한 초 동안 밝아지다가 어두워지기")
    print("0. 종료")
    choice = input("원하는 기능을 선택하세요: ")

    if choice == '1':
        turn_on_led()
    elif choice == '2':
        turn_off_led()
    elif choice == '3':
        fade_in_led()
    elif choice == '4':
        fade_out_led()
    elif choice == '5':
        fade_in_out_led()
    elif choice == '6':
        custom_duration = float(input("원하는 초를 입력하세요: "))
        fade_led(custom_duration)
    elif choice == '0':
        GPIO.cleanup()
        break
    else:
        print("올바른 선택이 아닙니다. 다시 선택하세요.")

