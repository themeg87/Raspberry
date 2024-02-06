import RPi.GPIO as GPIO
import time

led_red = 4
led_green = 5
led_blue = 6

# GPIO 핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# LED 핀을 출력으로 설정
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)

# LED를 20번 켜고 끄기
for i in range(20):  # range(20)을 사용하여 0부터 19까지의 수를 생성
    GPIO.output(led_red, True)
    time.sleep(0.5)
    GPIO.output(led_red, False)
    time.sleep(0.5)
    print("RED ON")

    GPIO.output(led_green, True)
    time.sleep(0.5)
    GPIO.output(led_green, False)
    time.sleep(0.5)
    print("GREEN ON")

    GPIO.output(led_blue, True)
    time.sleep(0.5)
    GPIO.output(led_blue, False)
    time.sleep(0.5)
    print("BLUE ON")
    print(f"{i}번 실행")
# GPIO 설정 초기화
GPIO.cleanup()
