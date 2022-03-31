#flask = 프레임 워크 #라이브러리와 프레임워크의 차이점?
from flask import Flask,request,redirect

app = Flask(__name__)
#내가 가진 데이터

topics = [
  {"id":1, "title":"html", "body":"html is ...."},
  {"id":2, "title":"css", "body":"css is ...."},
  {"id":3, "title":"js", "body":"js is ...."}
]
nextId = 4

def template(content):
  liTags = ''
  for topic in topics:
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

@app.route("/")#최상위 디렉터리
def index():
  return template('<h2>Welcome</h2>Hello, WEB!')

@app.route("/read/<int:id>/")
def read(id):
  title = ''
  body = ''  
  for topic in topics :
    if topic['id'] == id:
      title = topic['title']
      body = topic['body']
      break;
  return template(f'<h2>{title}</h2>{body}')

@app.route('/create/')
def create():
  content = '''
    <form action="/create_process/" methods="POST">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea name="body" placeholder="body"></textarea></p>
      <p><input type="submit" value="create"></p>
    </form>
  '''
  return template(content)

@app.route('/create_process/', methods = ['POST']) 
def create_process():
  global nextId 
  title = request.form['title']  #name="title" 값 출력
  body = request.form['body']
  newTopic = {"id":nextId, "title":title, "body":body}
  topics.append(newTopic)
  nextId = nextId + 1 #nextId는 함수 밖에 있기 떄문에 global로 지정
  return f'success!! go:/read/{nextId-1}/'

@app.route('/redirect/')
def a():
  
  return redirect('/')
# @app.route('/update/')
# def update():
#   return 'Update'

app.run()