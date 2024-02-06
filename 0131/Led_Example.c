#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//함수 선언
void LEDAllOff();
void generatePattern();
void LEDPattern(int* pattern, int time1);
void LEDWrong();
void LEDCorrect();

// LED 핀 번호 설정
#define LED_RED 7
#define LED_GREEN 29
#define LED_BLUE 31

// 밝기 정도 pwm 설정
#define BRIGHT_VALUE 100

// 시간 설정
#define BRIGHT_TIME 3

// 랜덤 패턴을 저장할 배열
int pattern[6];

// LED를 모두 끄는 함수
void LEDAllOff() {
    digitalWrite(LED_RED, 0);
    digitalWrite(LED_GREEN, 0);
    digitalWrite(LED_BLUE, 0);
}

// 랜덤 패턴을 생성하는 함수
void generatePattern() {
    int i;
    int availablePins[] = {LED_RED, LED_GREEN, LED_BLUE};
    for (i = 0; i < 6; i++) {
        int randomIndex = rand() % 3;
        pattern[i] = availablePins[randomIndex];
    }
}

// LED 패턴을 출력하는 함수
void LEDPattern(int* pattern, int time1) {
    int i;
    for (i = 0; i < 6; i++) {
        digitalWrite(pattern[i], 1);
        delay(time1 * 1000);
        digitalWrite(pattern[i], 0);
        delay(time1 * 1000);
    }
}

// 오답일 경우 LED를 깜빡이는 함수
void LEDWrong() {
    int i;
    for (i = 0; i < 3; i++) {
        digitalWrite(LED_RED, 1);
        delay(500); // 0.5초
        digitalWrite(LED_RED, 0);
        delay(500);
    }
}

// 정답일 경우 LED를 깜빡이는 함수
void LEDCorrect() {
    int i;
    for (i = 0; i < 3; i++) {
        digitalWrite(LED_GREEN, 1);
        delay(500);
        digitalWrite(LED_GREEN, 0);
        delay(500);
    }
}

// 메인 함수
int main(void) {
    if (wiringPiSetup() == -1)
        return 1;

    //출력 설정
    pinMode(LED_RED, OUTPUT);
    pinMode(LED_GREEN, OUTPUT);
    pinMode(LED_BLUE, OUTPUT);

    //초기화 작업
    digitalWrite(LED_RED, 0); 
    digitalWrite(LED_GREEN, 0); 
    digitalWrite(LED_BLUE, 0);

    printf("안녕하세요 라즈베리파이 LED 패턴 암기 게임입니다.\n");
    delay(1000);
    printf("패턴이 랜덤하게 생성 되어 LED가 점등됩니다.\n");
    delay(1000);
    printf("6개의 패턴을 기억한 후 패턴이 끝나면 정답을 입력해주세요.\n");
    delay(1000);
    printf("아무 키나 누르면 시작합니다.\n");
    getchar();

    // LED 초기화
    LEDAllOff();

    printf("패턴 생성중...\n");
    generatePattern();
    LEDPattern(pattern, 1);

    printf("정답을 입력해주세요. 빨강 = 7, 초록 = 29, 파랑 = 31\n");

    int player_pattern[6];
    int i;

    for (i = 0; i < 6; i++) {
        scanf("%d", &player_pattern[i]);
    }

    int correct = 1;
    for (i = 0; i < 6; i++) {
        if (pattern[i] != player_pattern[i]) {
            correct = 0;
            break;
        }
    }

    if (correct) {
        printf("정답입니다!\n");
        LEDCorrect();
    } else {
        printf("오답입니다!\n");
        printf("정답은 ");
        for (i = 0; i < 6; i++) {
            printf("%d ", pattern[i]);
        }
        printf("입니다.\n");
        LEDWrong();
    }

    return 0;
}
