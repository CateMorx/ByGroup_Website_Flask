from flask import Flask, render_template, request, flash
from math import pi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')

@app.route('/SearchAlgo', methods=['GET', 'POST']) #Ito yung iibahin natin for Lab Act 1
def area_of_a_circle():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        input_string = float(input_string)
        result = str(pi * input_string ** 2)
    return render_template('SearchAlgo.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
