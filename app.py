from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def calculate_age(birthdate):
    today = datetime.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += 30

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

@app.route('/', methods=['GET', 'POST'])
def index():
    age = None
    if request.method == 'POST':
        dob = request.form['dob']
        birthdate = datetime.strptime(dob, "%Y-%m-%d")
        age = calculate_age(birthdate)
    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
