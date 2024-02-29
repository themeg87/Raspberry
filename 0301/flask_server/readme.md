# Python flask 를 이용한 웹서버 만들기 🚢
## raspberry pi5에서 docker를 사용   

 1. make Dockerfile
 2. make requirements.txt
 3. make app.py
 4. add container

### Dockerfile (container 생성시 필요) 🧰
<pre><code>
* FROM python:3.8-slim

* WORKDIR /app

* COPY requirements.txt /app/

* RUN pip install -r requirements.txt

* COPY . /app

* CMD ["flask", "run", "--host=0.0.0.0"]
</code></pre>
### requirements.txt (python에서 사용할 라이브러리 설치) 🧰
<pre><code>
+ Flask==2.0.1   
+ Werkzeug==2.0.1   
 </code></pre>

### app.py (웹에서 실행될 코드) 🗞️
<pre>
<code>
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
</code>
</pre>

### Build Docker image (raspberry)
<pre>
 <code>
docker build -t flask-app .
  </code>
</pre>
### Add container (potainer.io)

