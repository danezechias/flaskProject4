from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


# Route for Project 1
@app.route('/project1')
def project1():
    return render_template('portfolioSQL1.html')

if __name__ == '__main__':
    app.run(debug=True)