from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login_user():
    if request.method == 'POST':
        return "Posted Data"
    return render_template('login.html')
    
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)