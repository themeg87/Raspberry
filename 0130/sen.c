#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>

#define PIR_D 2 // PIR 센서가 연결된 GPIO 번호
char pir_flag = 0; // 센서 감지를 나타내는 flag

void PIR_interrupt() {
    pir_flag = 1;
}

int main(void) {
    if (wiringPiSetup() == -1)
        return -1;

    pinMode(PIR_D, INPUT);
    wiringPiISR(PIR_D, INT_EDGE_RISING, &PIR_interrupt);

    while (1) {
        if (pir_flag == 1) {
            printf("PIR Detected !!\n");
            pir_flag = 0;
        } else {
            printf("PIR Not detect !!\n");
        }
        usleep(500000); // 0.5초 딜레이
    }
    return 0;
}
