#
#      공대선배 라즈베리파이썬 #11 python flask 1편
#      youtube 바로가기: https://www.youtube.com/c/공대선배
#      flask를 이용해 간단한 웹사이트 만들기
#
from flask import Flask     # flask 모듈을 불러움

app = Flask(__name__)       # Flask라는 이름의 객체 생성

@app.route('/')             # 기본 주소
def hello():                # 해당 주소에서 실행되는 함수 정의 (뷰함수)
   return "Hello Flask!"    # 반드시 return이 있어야하며, 해당 값을 화면에 보여줌

if __name__ == "__main__":  # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분
   app.run(host="192.168.1.4", port = "8080")
   # host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정
   # 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능
