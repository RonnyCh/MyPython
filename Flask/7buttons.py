
# there is a bit of problem in visual code
# if you can't run this code again
# select python terminal, right hand click and click it
# run it again
# this 

import pandas as pd
from flask import Flask, render_template,request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def hello_flask():
   return render_template('Buttons.html')

@app.route('/buttons',methods = ['POST','GET'])
def mybutton():
   if request.method=='POST':
      
      me = request.form['button']

      if me == 'submit1':
         # do some python codes
         list = [1,2,3,4,5]
         df = pd.DataFrame({'A':list})
         df.to_csv('test1.csv')
         return redirect(url_for('status',name = 'button 1 executed'))
      else:
         list = [1,2,3,4,5]
         df = pd.DataFrame({'B':list})
         df.to_csv('test2.csv')
         return redirect(url_for('status',name = 'button 2 executed'))


@app.route('/success/<name>')
def status(name):
   return '>>>>>>>> %s' % name

if __name__ == '__main__':
   app.run(debug=True)
