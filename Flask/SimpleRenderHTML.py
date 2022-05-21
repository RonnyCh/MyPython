
# you need to put the html template in folder templates


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def success():
   return render_template('hellosimple.html')


if __name__ == '__main__':
   app.run()