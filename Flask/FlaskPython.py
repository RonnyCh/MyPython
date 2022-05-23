from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('buttons.html')

# do some sqls
@app.route('/buttons',methods = ['POST', 'GET'])
def student():
   if request.method == 'POST':
      if request.form['button'] == 'submit1':
         
         count = 100 * 2
         count = str(count)

         return count
      else:
         return 'button2'

# pass to another html
@app.route('/hello')
def hello():
   return render_template('hello.html')


if __name__ == '__main__':
   app.run()