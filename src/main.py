from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login_user():
    if request.method == 'POST':
        details = request.form
        username = details["username"]
        return render_template('main.html', user=username)
    return render_template('login.html')
    
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)