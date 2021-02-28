from flask import Flask, render_template, redirect, url_for, flash, session,request
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired
from wtforms import Form
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/contacts'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'abc'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'webdev.205120072@gmail.com'
app.config['MAIL_PASSWORD'] = '205120072'
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)



'''class Query(db.Model):
    #SNo = db.column(db.Integer)
    name = db.Column(db.String(20) , unique=False , nullable = False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    message = db.Column(db.String(200), unique=False, nullable=False)'''


@app.route("/")
def index():
    return render_template("contact.html")

@app.route('/contact',methods=['GET' , 'POST'])



def contact():
    if request.method == "POST":
        Name = request.form.get("Name")
        email = request.form.get("email")
        message = request.form.get("message")

        #entry = Contacts(name= Name, email=email, message=message)
        #db.session.add(entry)
        #db.session.commit()
        mail.send_message('New message', 
                           sender= email, 
                           recipients = ['webdev.205120072@gmail.com'],
                           body = Name+"\n"  + email+ "\n"  + message)
        flash('YOUR QUERY HAS BEEN SENT WILL CONTACT YOU SHORTLY!!!!')
    return render_template("contact.html")

if __name__== '__main__':
    app.run(debug=True)
