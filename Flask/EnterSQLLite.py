from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('student.html')


@app.route('/student',methods = ['POST', 'GET'])
def student():
   if request.method == 'POST':
      return 'Success '
   else:
      return 'not really'


if __name__ == '__main__':
   app.run()