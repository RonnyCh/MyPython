from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('student.html')


@app.route('/student',methods = ['POST', 'GET'])
def student():
   if request.method == 'POST':
      nm = request.form['nm']
      addr = request.form['add']
      city = request.form['city']
      pin = request.form['pin']

      with sql.connect("database.db") as con:
         cur = con.cursor()
         cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
         con.commit()
         msg = "Record successfully added"

      return msg
   else:
      return 'not really'


if __name__ == '__main__':
   app.run()