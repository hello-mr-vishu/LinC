
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Create the SQLite database file  
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username and password match a user in the database
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return 'Login successful!'
        else:
            return 'Invalid username or password.'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_username = request.form['newUsername']
        new_password = request.form['newPassword']

        # Check if username already exists
        existing_user = User.query.filter_by(username=new_username).first()
        if existing_user:
            return 'Username already exists!'

        # Create new user and add to database
        new_user = User(username=new_username, password=new_password)
        db.session.add(new_user)
        db.session.commit()

        return 'Registration successful!'

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
