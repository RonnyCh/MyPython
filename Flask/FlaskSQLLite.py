from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('student.html')

# do some sqls
@app.route('/student',methods = ['POST', 'GET'])
def student():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']

         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("delete from students where name is null or name = ''")
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            con.commit()
            msg = "Record successfully added"

         
      except:
         return 'you have errors'
      finally:
         con = sql.connect('database.db')
         con.row_factory = sql.Row 
         cur = con.cursor()
         cur.execute("select * from students")
         rows = cur.fetchall(); 
         return render_template("list.html",rows = rows)


# pass to another html
@app.route('/hello')
def hello():
   return render_template('hello.html')


if __name__ == '__main__':
   app.run()