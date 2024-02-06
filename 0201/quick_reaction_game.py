import RPi.GPIO as GPIO
import random
import time

# GPIO 핀 번호 설정
LED_RED = 4
LED_GREEN = 5
LED_BLUE = 6
SW2 = 23
SW3 = 24
SW4 = 25

# GPIO 핀 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.setup(SW2, GPIO.IN)
GPIO.setup(SW3, GPIO.IN)
GPIO.setup(SW4, GPIO.IN)

# LED 초기화
GPIO.output(LED_RED, GPIO.LOW)
GPIO.output(LED_GREEN, GPIO.LOW)
GPIO.output(LED_BLUE, GPIO.LOW)

total = 0     # 총 점수

randColor = [LED_RED, LED_GREEN, LED_BLUE]

for i in range(10):  # 10회 반복 
    judgment = 0 # 판정1 : 버튼을 올바르게 눌렀는지 
    judgment2 = 0 # 판정2 : 시간내에 버튼을 눌었는지 아닌지

    # 색 랜덤으로 출력하기 
    color = randColor[random.randint(0, 2)]
    # 랜덤 시간 설정하기 
    sleep_time = random.uniform(0.5, 1.0)

    GPIO.output(color, GPIO.HIGH)

    start_time = time.time()
    while True:                # 랜덤 시간 만큼 반복
        ret = GPIO.input(SW2)  # 빨강 - SW2
        if ret == 0:
            judgment2 = 1
            if color != LED_RED:
                judgment = 1
        
        ret = GPIO.input(SW3)  # 초록 - SW3
        if ret == 0:
            judgment2 = 1
            if color != LED_GREEN:
                judgment = 1
        
        ret = GPIO.input(SW4)  # 파랑 - SW4
        if ret == 0:
            judgment2 = 1
            if color != LED_BLUE:
                judgment = 1

        current_time = time.time()
        if current_time - start_time >= sleep_time: # 지정한 시간이 지나면 종료 
            break
    
    if judgment == 1:     # 틀린 버튼을 누르는 경우
        print("bad")
    elif judgment2 == 0:  # 버튼을 시간내에 누르지 못한 경우
        print("miss")
    else:                 # 시간내에 올바른 버튼을 누른 경우 
        total += 1
        print("perfect")  

    GPIO.output(color, GPIO.LOW)

print("최종 점수는 "+str(total)+"점")  # 최종 점수 출력 

GPIO.cleanup()