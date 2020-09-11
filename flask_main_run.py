from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import csv
app = Flask(__name__)

#config for flask_sqlalchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

db = SQLAlchemy(app) #create object from config

class students(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(100))
    lname = db.Column(db.String(50))
    def __init__(self, name,lname):
        self.name = name
        self.lname = lname

db.create_all()
student = students("dani", "din")
db.session.add(student)
db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/hello.html', methods=['GET', 'POST'])
def req():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        with open ("test.csv", 'a' , newline='') as fd:
            csvwriter = csv.writer(fd, delimiter=',')
            csvwriter.writerow([str(name), str(email)])
    return render_template('hello.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f =request.files['file']
        f.save(f.filename)
        return ('file uploaded successfully')

if __name__ == "__main__":
    app.run(debug=True)