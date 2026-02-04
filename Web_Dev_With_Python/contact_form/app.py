from flask import Flask, render_template, redirect, request, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# app.config['WTF_CSRF_ENABLED'] = False

# Fallback key for testing if .env is missing
app.secret_key = os.getenv('SECRET_KEY', 'default-dev-key-123')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Please enter your name.")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email address.")])
    message = TextAreaField('Message', validators=[DataRequired(message="Please write a message.")])
    submit = SubmitField('Send Message')

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('contact.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)