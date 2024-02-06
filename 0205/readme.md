# Flask를 활용한 Raspberry Pi LED 제어

이 프로젝트는 Raspberry Pi에 연결된 LED를 제어하기 위한 Flask 웹 애플리케이션을 소개합니다. 이 코드는 GPIOZero 라이브러리를 활용하여 LED를 제어하며, 개별 LED 색상 (빨강, 녹색, 파랑)을 전환하거나 모든 LED를 동시에 켜고 끄는 간단한 웹 인터페이스를 제공합니다.

## 요구 사항

시작하기 전에 다음 구성 요소와 소프트웨어를 설치해야 합니다.

- Raspberry Pi (어떤 모델이든 상관 없음)
- GPIO 핀 14, 15, 18에 연결된 LED (필요 시 코드에서 핀 번호를 수정할 수 있음)
- Raspberry Pi에 Python 설치
- Flask 웹 프레임워크 (`pip install Flask`)
- GPIOZero 라이브러리 (`pip install gpiozero`)

## 사용 방법

1. 이 저장소를 Raspberry Pi에 복제하거나 다운로드합니다.
2. `app.py` 스크립트를 실행하여 Flask 애플리케이션을 시작합니다.

   ```bash
   python app.py
