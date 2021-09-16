from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

sampleArticles = [
    {
        "video" : "https://www.youtube.com/embed/RdT5X5EgPNU",
        "title" : "Python, APIs and Docker Boot Camp By Lux Academy and Data Science East Africa Onboarding Call"
    },
    {
        "video" : "https://www.youtube.com/embed/Sdk2EqIC1mI",
        "title" : "Build and Deploy Flask Application using Docker"
    },
    {
        "video" : "https://www.youtube.com/embed/mmCfUqrIe_Q",
        "title" : "Week 4 - Day1: Introduction to Python for Data Science"
    },
    {
        "video" : "https://www.youtube.com/embed/MetoIClcg6c",
        "title" : "Web Development with Python using Flask"
    },
    {
        "video" : "https://www.youtube.com/embed/xmcfFji0bSI",
        "title" : "Week 3: Day one - Demistifying the Flask Application Factory Pattern"
    },
    {
        "video" : "https://www.youtube.com/embed/85qBaxVnIhc",
        "title" : "Getting Started with Python Web Development, Flask and FastAPI"
    },
    {
        "video" : "https://www.youtube.com/embed/0331iclOw-U",
        "title" : "Introduction to Data Structures and Algorithms With Python"
    },
    {
        "video" : "https://www.youtube.com/embed/U7jxRXoaUUc",
        "title" : "Becoming a Badass Python Programmer by Joy Victor"
    },
]

@app.route('/', methods=['POST', 'GET'])
def login_user():
    if request.method == 'POST':
        details = request.form
        username = details["username"]
        return render_template('main.html', user=username, articles=sampleArticles)
    return render_template('login.html')
    
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)