
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
       return render_template('home.html')

if __name__ == '__main__':
    app.run("0.0.0.0", "5000")

#from flask import Flask,render_template,request
 
#app = Flask(__name__)
 
#@app.route('/form')
#def form():
#    return render_template('home.html')
 
#@app.route('/data/', methods = ['POST', 'GET'])
#def data():
#    if request.method == 'GET':
#        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#    if request.method == 'POST':
#        form_data = request.form
#        return render_template('data.html',form_data = form_data)
 
#if __name__ == '__main__':
#    app.run("0.0.0.0", "5000")
