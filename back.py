from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
bcrypt = Bcrypt(app)


client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  
users_collection = db['users']

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['logname']
        email = request.form['logemail']
        password = request.form['logpass']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        
        users_collection.insert_one({
            'name': name,
            'email': email,
            'password': hashed_password
        })

        return redirect(url_for('index'))

    return render_template('signup.html')  

if __name__ == '__main__':
    app.run(debug=True)


