
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
   return render_template('Buttons.html')

@app.route('/buttons',methods = ['POST','GET'])
def mybutton():
   if request.method=='POST':
      
      me = request.form['button']

      if me == 'submit1':
         # this will send to matplotlib pyhon codes
         return redirect(url_for('status1'))
      else:
         # this will create a dataframe
         global df
         name = ['Ron','Ch','Mercy','Mimi','VB']
         score = [1,2,3,4,5]
         df = pd.DataFrame({'Name':name,'Score':score})
         df.to_csv('test2.csv')
         return redirect(url_for('status2'))


@app.route('/button1')
def status1():
    # Matplotlib method in FLASK**.
    fig = Figure()
    ax = fig.subplots()
    mylist = [10,20,13,20,10,50,20]
    ax.plot(mylist)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
    #return list

@app.route('/button2')
def status2():
   # note the return must be string, dict or tuples
   return df.to_html(header="true",index=False)


if __name__ == '__main__':
   app.run(debug=True)
