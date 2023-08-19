from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret_key"  # Replace with your own secret key

# Simulated database of user credentials (for demonstration purposes)
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def index():
    return "Welcome to the simple login authentication system. <a href='/login'>Login</a> or <a href='/register'>Register</a>."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('secured'))
        else:
            return "Invalid credentials. <a href='/login'>Try again</a>."
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username not in users:
            users[username] = password
            return "Registration successful. <a href='/login'>Login</a>."
        else:
            return "Username already exists. <a href='/register'>Try again</a>."
    
    return render_template('register.html')

@app.route('/secured')
def secured():
    if 'username' in session:
        return f"Welcome, {session['username']}! This is a secured page. <a href='/logout'>Logout</a>."
    else:
        return "You need to <a href='/login'>login</a> first to access this page."

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
