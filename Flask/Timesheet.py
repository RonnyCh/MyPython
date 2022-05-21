

# first thing to do run this server
# then open login.html from your explorer
# it will open up in browser
# then type name click login, this will trigger code below

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template ('timesheet.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/timesheet',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      
      date = request.form['dt']
      day = request.form['dy']
      company = request.form['co']
      rate = request.form['rate']

      
      return redirect(url_for('success',name = date))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run()