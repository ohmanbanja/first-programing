from flask import Flask
import random

app = Flask(__name__)
#topics:변수이름
topics = [ 
  {"id":1, "title":"html", "body":"html is..."},
  {"id":2, "title":"css", "body":"css is..."},
  {"id":3, "title":"js", "body":"js is..."}
]

@app.route("/")
def home():
    return '''
    <html>
      <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
        <li><a href="/read/1/">html</a></li>
        <li><a href="/read/2/">css</a></li>
        <li><a href="/read/3/">js</a></li>
      </ol>
      <h2>Welcome</h2>
        Hello,web!
      </body>
    </html>
    '''
@app.route("/read/1/")
def readl():
  return '''
    <html>
      <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
        <li><a href="/read/1/">html</a></li>
        <li><a href="/read/2/">css</a></li>
        <li><a href="/read/3/">js</a></li>
      </ol>
      <h2>Welcome</h2>
        Read
      </body>
    </html>
    '''

@app.route("/create/")
def create():
    return 'create'
  

@app.route("/update/")
def update():
    return 'update'
  
app.run()