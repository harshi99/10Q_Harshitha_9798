from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/iv', methods=['GET', 'POST'])
def iv_form():
    if request.method == 'POST':
        L1 = int(request.form['L1'])
        L2 = int(request.form['L2'])
        IV = request.form['IV']
        
        return render_template('cp_form.html', L1=L1, L2=L2, IV=IV)
    
    return render_template('iv_form.html')

@app.route('/cp', methods=['GET', 'POST'])
def cp_form():
    if request.method == 'POST':
        L1 = int(request.form['L1'])
        L2 = int(request.form['L2'])
        IV = request.form['IV']
        password = request.form['password']
        
        if len(password) < L1:
            return 'NotValid: Password is too short.'
        if len(password) > L2:
            return 'NotValid: Password is too long.'
        if not any(char.isdigit() for char in password):
            return 'NotValid: Password must contain at least one number.'
        if not sum(1 for char in password if char.isupper()) >= 2:
            return 'NotValid: Password must contain at least two uppercase letters.'
        if not any(char in '#@+-%' for char in password):
            return 'NotValid: Password must contain at least one of the special characters #, @, +, -, or %.'
        if any(char in '!@$*' for char in password):
            return 'NotValid: Password cannot contain the characters !, @, $, or *.'
        if any(char in IV for char in password):
            return 'NotValid: Password contains one or more characters from the invalid list.'
        
        return 'Valid'
    
    return render_template('cp_form.html')

if __name__ == '__main__':
    app.run(debug=True)
