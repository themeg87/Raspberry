#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <time.h>

// GPIO 핀 번호 설정
#define LED_RED 7
#define LED_GREEN 21
#define LED_BLUE 22
#define SW2 4
#define SW3 5
#define SW4 6

int main() {
    int total = 0;     // 총 점수

    //핀 모드 설정
	if(wiringPiSetup () == -1)
		return 1;
	pinMode(LED_RED,OUTPUT);
	pinMode(LED_GREEN,OUTPUT);
	pinMode(LED_BLUE,OUTPUT);

    //LED 초기화
	digitalWrite(LED_RED,0);
	digitalWrite(LED_GREEN,0);
	digitalWrite(LED_BLUE,0);

    srand(time(NULL)); // 랜덤 시드 초기화

    for (int i = 0; i < 10; i++) {  // 10회 반복 
        int ret = 2;
        int judgment = 0; // 판정1 : 버튼을 올바르게 눌렀는지 
        int judgment2 = 0; // 판정2 : 시간내에 버튼을 눌었는지 아닌지

        // 색 랜덤으로 출력하기 
        int color = rand() % 3;
        // 랜덤 시간 설정하기 
        double sleep_time = ((double)rand() / RAND_MAX) * 0.5 + 0.5;

        if (color == 0){
            digitalWrite(LED_RED, HIGH);
        }else if (color == 1){
            digitalWrite(LED_GREEN, HIGH);
        }else if (color == 2){
            digitalWrite(LED_BLUE, HIGH);
        }

        clock_t start_time = clock();
        while (1) {                // 랜덤 시간 만큼 반복
            ret = digitalRead(SW2);  // 빨강 - SW2
            if (ret == 0) {
                judgment2 = 1;
                if (color != 0) {
                    judgment = 1;
                }
            }
        
            ret = digitalRead(SW3);  // 초록 - SW3
            if (ret == 0) {
                judgment2 = 1;
                if (color != 1) {
                    judgment = 1;
                }
            }
        
            ret = digitalRead(SW4);  // 파랑 - SW4
            if (ret == 0) {
                judgment2 = 1;
                if (color != 2) {
                    judgment = 1;
                }
            }

            clock_t current_time = clock();
            if (((double)(current_time - start_time) / CLOCKS_PER_SEC) >= sleep_time) { // 지정한 시간이 지나면 종료 
                break;
            }
        }
    
        if (judgment == 1) {     // 틀린 버튼을 누르는 경우
            printf("bad\n");
        } else if (judgment2 == 0) {  // 버튼을 시간내에 누르지 못한 경우
            printf("miss\n");
        } else {                 // 시간내에 올바른 버튼을 누른 경우 
            total += 1;
            printf("perfect\n");
        }

        if (color == 0){
            digitalWrite(LED_RED, LOW);
        }else if (color == 1){
            digitalWrite(LED_GREEN, LOW);
        }else if (color == 2){
            digitalWrite(LED_BLUE, LOW);
        }
    }

    printf("최종 점수는 %d점\n", total);  // 최종 점수 출력 

    return 0;
}