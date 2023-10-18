from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/pagepage/')
def pagepage():
    return('essa é a pagepage')

if __name__ == "__main__":
    app.run(debug=True)