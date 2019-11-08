
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
   return 'Hello World %s' %name


@app.route('/yes/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)


if __name__ == '__main__':
   app.run()
