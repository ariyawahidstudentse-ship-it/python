from flask import Flask, render_template, requst
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods =['POST'])
def calcuate_age():
    try:
        birth_year = int(requst.form['birh_year'])

        current_year = datetime.now().year

        if birth_year > current_year or birth_year < 1900:
            return render_template(
                'index.html',
                error="please enter a valid year (1900 _ CURRENT YEAR)"
            )
        age = current_year - birth_year

        return render_template('index.html', age=age)
    except ValueError:
        return render_template('index.html', error="please enter a valid number")
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
