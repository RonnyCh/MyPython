

# first thing to do run this server
# then open login.html from your explorer
# it will open up in browser
# then type name click login, this will trigger code below

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template ('login.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run()