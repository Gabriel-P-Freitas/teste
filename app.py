from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/questao01')
def questao01():
    return render_template('questao01.html')


app.run(host='0.0.0.0', port=81, debug='TRUE')

