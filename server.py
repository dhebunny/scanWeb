from flask import Flask, render_template, request, redirect 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('splash.html')

@app.route('/splash')
def splash():
    return render_template('splash.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/scan')
def scan():
    return render_template('scan.html')

@app.route('/signup')
def signUp():
    return render_template('signUp.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submitted')
def submitted():
    return render_template('submitted.html')

def file_to_write(data):
    with open('db.txt', mode='a') as db:
        um = data['email']
        us = data['subject']
        msg= data['message']
        db.write(f'\n EMAIL:{um}, SUBJECT: {us}, MESSAGE: {msg}')
 
@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        file_to_write(data)
        return redirect('submitted')



if __name__ == "__main__":
    app.run(debug=True)