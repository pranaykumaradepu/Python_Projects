from flask import Flask, render_template

# create Flask App
app = Flask(__name__)

# Defining A Route
@app.route('/')
def hello():
    return render_template('index.html')

# Greeting Route
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

@app.route('/about') 
def about():
    return render_template('about.html')

# Run The App
if __name__ == "__main__":
    app.run(debug=True)