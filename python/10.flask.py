#flask= 프레임워크
#모듈가져오기 from 모듈 import 이름 
#route = 도메인에서 하부 url로 이동 
from flask import Flask

app = Flask(__name__)
#내가 가진 데이터 배열화 2차원데이터
topics = [
  {"id":1, "title":"html", "body":"html is ...."},
  {"id":2, "title":"css", "body":"css is ...."},
  {"id":3, "title":"js", "body":"js is ...."}
]
# def = 변수 선언, template = 함수   
def template(content):
#topics에 있는 topic 모두 꺼내기
  liTags = ''
  for topic in topics: # f{} = f string (f'문자열 {변수} 문자열')
    liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
  return f'''
  <html>
    <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
        {liTags}
      </ol>
        {content}
      <ul>
        <li><a href="/create/">create</a></li>
      </ul>
    </body>
  </html>
  '''

@app.route("/") # 최상위 디렉토리
def index():
  return template('<h2>Welcome</h2>Hello, WEB!')
#id 변수처리

@app.route("/read/<int:id>/")#int<-- 정수
def read(id): #<-----변수처리한 id와 같은 
  title = ''
  body = ''  
  for topic in topics :
    #만약 topic의 id값이 id와 같다면 topic의    body,title 추출
    if topic['id'] == id: 
      title = topic['title']
      body = topic['body']
      break;
  return template(f'<h2>{title}</h2>{body}') 

@app.route('/create/')
def create():
      #placeholer : 작성할 내용 text box에 표시// 
      #textarea : text박스 여러 줄 // p tag: 단락
      #form action : submit 어디로 제출할지 지정
  content = '''
    <form action="/create/">             
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea name="body" placeholder="body"></textarea></p>
      <p><input type="submit" value="create"></p>
    </form>
  '''
  return template(content)

@app.route('/update/')
def update():
  return 'Update'

app.run()