
# there is a bit of problem in visual code
# if you can't run this code again
# select python terminal, right hand click and click it
# run it again
# this 

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_flask():
   return 'Hello Flask'


if __name__ == '__main__':
   app.run()


