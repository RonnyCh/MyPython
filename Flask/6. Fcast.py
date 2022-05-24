

# use this one for forecasting input table linked to SQLlite


from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('fcastmaster.html')

# do some sqls
@app.route('/fcast',methods = ['POST', 'GET'])
def student():
   if request.method == 'POST':
      try:
         mystart = request.form['start']
         mydesc = request.form['desc']
         myamt = request.form['amt']
         myinterval = request.form['interval']
         myend = request.form['end']
         mycat = request.form['cat']

         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("delete from parm_tbl_fcast where date is null or date = ''")  # clean up blank data/unnecesary ones
            cur.execute("INSERT INTO parm_tbl_fcast VALUES (?,?,?,?,?,?)",(mystart,mydesc,myamt,myinterval,myend,mycat) )
            con.commit()
            msg = "Record successfully added"

      except:
         return 'you have errors'
      finally:
         con = sql.connect('database.db')
         con.row_factory = sql.Row 
         cur = con.cursor()
         cur.execute("select * from parm_tbl_fcast")
         global rows
         rows = cur.fetchall(); 
         #return render_template("list.html",rows = rows)
         return render_template('fcastmaster.html')


# pass to another html
@app.route('/Student')
def hello():
   return render_template('Student.html')

@app.route('/listFcast')
def list():
   return render_template('listFcast.html',rows=rows)


if __name__ == '__main__':
   app.run()
