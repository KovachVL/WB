from flask import Flask, request, render_template_string

app = Flask(__name__)


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
        error = 'Login failed'
    return render_template_string('LOGIN PAGE: <br> <form method="post"><input type="text" name="username"><input type="password" name="password"><input type="submit" value="Login"></form>')


@app.route('/cmd')
def cmd():
    command = request.args.get('command', 'whoami')
    output = 'Command output'
    return render_template_string('<h2>' + output + '</h2>')

if __name__ == '__main__':
    app.run(debug=True)
