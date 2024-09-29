from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///registrations.db"
app.config['SQLACHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy()
db.init_app(app)

class students(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    dept=db.Column(db.String(200),nullable=False)
    course=db.Column(db.String(200),nullable=False)
    sem=db.Column(db.Integer,nullable=False)
    roll=db.Column(db.String(200),nullable=False)
    phno=db.Column(db.Integer,nullable=False)
    def  __repr__(self)-> str:
        return f'<registrations{self.sno} - {self.name}>' 

with app.app_context():
    db.create_all()

#Front page______________________________________________________________________________________________________
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/button',methods=["GET","POST"])
def register():
    
    if request.method=="POST":
        name=request.form['name']
        dept=request.form['department']
        course=request.form['course']
        sem=request.form['semester']
        roll=request.form['roll_no']
        phno=request.form['phone_no']
        
        existing_student = students.query.filter_by(roll=roll).first()
        if existing_student:
            return render_template('error.html',message="Roll no previously present")
        else:

            details=students(name=name, dept=dept, course=course, sem=sem,roll=roll,phno=phno)
            db.session.add(details)
            db.session.commit()
        return redirect('/')
    else:
        
        return render_template('loginpage.html')

@app.route('/show')
def showregistrations():
    alldetails=students.query.all()
    print (alldetails)
    return render_template('show.html',alldetails=alldetails)

@app.route('/about')
def aboutus():
    return render_template('Aboutus.html')


if __name__=="__main__":
     app.run(debug=True)