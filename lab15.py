from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
  return '''
        <p> Katie S. : lmao </p>
        <p> Ash S. : ijbol </p>
        <p> Nico S. : lol </p>
        '''

@app.route('/han')
def t_test():
   return render_template('template.html')
