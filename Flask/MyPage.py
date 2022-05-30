
# there is a bit of problem in visual code
# if you can't run this code again
# select python terminal, right hand click and click it
# run it again
# this 

import pandas as pd
import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask, render_template,request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def hello_flask():
   return render_template('Ronny.html')

@app.route('/buttons',methods = ['POST','GET'])
def mybutton():
   if request.method=='POST':
      
      ### check the value of button ###
      me = request.form['button']
      myval = request.form['nm']

      ### do if function based on the above
      if me == 'Forecast Master Table':
         # this will send to matplotlib pyhon codes
         return redirect(url_for('status2'))
      else:
         # this will create a dataframe
         global df
         df = pd.read_csv(r'C:\Users\r.christianto\MyPython\Yahoo\Yahoo.csv')
         df = df[df['Code']==myval]
         return redirect(url_for('status1'))


@app.route('/button1')
def status1():
    
    return df.to_html(header="true",index=False)

@app.route('/button2')
def status2():
   # note the return must be string, dict or tuples
   return render_template('fcastmaster.html')


if __name__ == '__main__':
   app.run(debug=True)
