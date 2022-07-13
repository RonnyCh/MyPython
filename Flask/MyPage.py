
# there is a bit of problem in visual code
# if you can't run this code again
# select python terminal, right hand click and click it
# run it again
# this 

import pandas as pd
import sqlite3
import os
#import base64
#from io import BytesIO
#from matplotlib.figure import Figure
from flask import Flask, render_template,request, redirect, url_for
app = Flask(__name__)

###### render html for first page ######
@app.route('/')
def hello_flask():
   return render_template('Ronny.html')


###### this will get information from ronny.html #######
@app.route('/buttons',methods = ['POST','GET'])
def mybutton():
   if request.method=='POST':
      
      ### check the values come from ronny.html ###
      me = request.form['button']
      myval = request.form['nm']
      global mydate
      mydate = request.form['start']
      os.chdir(r'c:\Users\r.christianto\MyPython\SQLLite')
      con = sqlite3.connect("mydatabase")
      global sql
      global sql2

      ### do if function based on the above values ###
      if me == 'Database ParmTable':
         # this will send def status 1
         mysql = 'select * from parm_tbl_fcast' 
         sql2 = pd.read_sql_query(mysql,con)
         return redirect(url_for('status2'))
      elif me == 'Database Query':
         mysql = 'select * from actual_cbacard where date = "' + mydate + '"' 
         sql = pd.read_sql_query(mysql,con)
         return redirect(url_for('status1'))
      else:
         # this will create a dataframe
         global df
         df = pd.read_csv(r'C:\Users\r.christianto\MyPython\Yahoo\Yahoo.csv')
         df = df[df['Code']==myval]
         return redirect(url_for('status2'))

# def status 1 >>> send to web address >> /button 
@app.route('/cbacard')
def status1():
    return sql.to_html(header="true",index=False)
    #return mydate

# def status 2 >>> send to web address >> /button2
@app.route('/parmtable')
def status2():
   # note the return must be string, dict or tuples
   #return render_template('fcastmaster.html')
   return sql2.to_html(header="true",index=False)
   #return 'ok'

@app.route('/yahoo')
def status3():
   return me


@app.route('/date')
def status4():
   return mydate


if __name__ == '__main__':
   app.run(debug=True)
