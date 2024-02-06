#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>

#define LED_RED 7
#define LED_GREEN 21
#define LED_BLUE 22

int main(void){
    srand(time(NULL));
    int randColor[3] = {0, 0, 0};
    int number;

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
	
    //게임 시작
    printf("------------------------------------------------\n");
    printf("                빛의 삼원색 게임 \n");
    printf("- 색을 확인하고 합쳐지면 어떤 색이 되는지 맞춰보자 -\n");
	printf("------------------------------------------------\n\n");

    //랜덤 색 2개 or 3개 선정 
    if (rand()%3 != 0){
        //화이트 이외의 다른 색
        randColor[0] = rand() % 3 + 1;
        randColor[1] = rand() % 3 + 1;
        while (randColor[0] == randColor[1]){
            randColor[1] = rand() % 3 + 1;
        }
    }else{
        //화이트가 되는 경우
        randColor[2] = 7;
    }

    //랜덤 색 출력
    //화이트가 되는 경우
    usleep(1000000);
    if(randColor[2] == 7){
        digitalWrite(LED_RED,1);
	    usleep(500000);
	    digitalWrite(LED_RED,0);
        digitalWrite(LED_GREEN,1);
	    usleep(500000);
	    digitalWrite(LED_GREEN,0);
        digitalWrite(LED_BLUE,1);
	    usleep(500000);
	    digitalWrite(LED_BLUE,0);
    }else{
        //다른 색인 경우 
        switch(randColor[0]){
            case 1:
                digitalWrite(LED_RED,1);
                usleep(500000);
                digitalWrite(LED_RED,0);
                break;
            case 2:
                digitalWrite(LED_GREEN,1);
                usleep(500000);
                digitalWrite(LED_GREEN,0);
                break;
            case 3:
                digitalWrite(LED_BLUE,1);
                usleep(500000);
                digitalWrite(LED_BLUE,0);
                break;
            default:
                printf("출력 오류");
                break;    
        }

        switch(randColor[1]){
            case 1:
                digitalWrite(LED_RED,1);
                usleep(500000);
                digitalWrite(LED_RED,0);
                break;
            case 2:
                digitalWrite(LED_GREEN,1);
                usleep(500000);
                digitalWrite(LED_GREEN,0);
                break;
            case 3:
                digitalWrite(LED_BLUE,1);
                usleep(500000);
                digitalWrite(LED_BLUE,0);
                break;
            default:
                printf("출력 오류");
                break;    
        }
    }

    //선택 옵션 출력
    printf("---------------------------\n");
    printf("1. yellow\n");
    printf("2. magenta\n");
    printf("3. cyan\n");
    printf("4. white\n");
    printf("---------------------------\n\n");

    //답 입력 받기 
    printf("숫자를 입력하세요: ");
    scanf("%d", &number);

    //정답일 경우
    if (number+2 == randColor[0]+randColor[1] || number+3 == randColor[2]){ 
        printf("정답입니다.\n");
        digitalWrite(LED_RED,1);
	    usleep(500000);
        digitalWrite(LED_GREEN,1);
	    usleep(500000);
        digitalWrite(LED_BLUE,1);
	    usleep(500000);
        digitalWrite(LED_RED,0);
        digitalWrite(LED_GREEN,0);
	    digitalWrite(LED_BLUE,0);
    }else{
        //오답일 경우 
        printf("오답입니다.\n");
        digitalWrite(LED_RED,1);
	    usleep(500000);
	    digitalWrite(LED_RED,0);
        usleep(500000);
        digitalWrite(LED_RED,1);
	    usleep(500000);
	    digitalWrite(LED_RED,0);
        usleep(500000);
        digitalWrite(LED_RED,1);
	    usleep(500000);
	    digitalWrite(LED_RED,0);
    }

	return 0;
}