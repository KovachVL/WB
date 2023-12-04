from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Заменить 'your_secret_key' на ваш секретный ключ

users = {'admin': 'admin_password'}

@app.route('/')
def index():
    message = request.args.get('message', 'Hello, World!')
    return render_template_string('<h2>' + message + '</h2>')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username  
            return redirect(url_for('cmd'))
        else:
            error = 'Login failed'
    return render_template_string('LOGIN PAGE: <br> <form method="post"><input type="text" name="username"><input type="password" name="password"><input type="submit" value="Login"></form><p>{{ error }}</p>', error=error)

@app.route('/cmd')
def cmd():
    if 'username' not in session:
        return redirect(url_for('login')) 
    command = request.args.get('command', 'whoami')
   
    allowed_commands = ['whoami', 'ls']
    if command not in allowed_commands:
        return 'Access denied'
    output = 'Command output: ' + command
    return render_template_string('<h2>' + output + '</h2>')

if __name__ == '__main__':
    app.run(debug=True)
