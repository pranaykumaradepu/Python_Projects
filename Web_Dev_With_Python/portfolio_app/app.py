from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import dotenv

# loading environment variables
dotenv.load_dotenv()

app = Flask(__name__)

# Fallback key for development
app.secret_key = os.getenv('SECRET_KEY', 'default_dev_key')

# database config
database_url = os.getenv('DATABASE_URL', 'sqlite:///portfolio.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Postgres connection fixes (if hosted later)
if database_url.startswith('postgresql'):
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False) # Increased length
    image = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(200), nullable=True) # Made link nullable

# Home Route
@app.route('/')
def home():
    projects = Project.query.limit(3).all() 
    return render_template('index.html', projects=projects)

# Projects Route
@app.route('/projects')
def projects():
    all_projects = Project.query.all()
    return render_template('projects.html', projects=all_projects)

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Route
@app.route('/contact', methods=['GET', 'POST']) 
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not name or not email or not message:
            flash('All fields are required!', 'error')
        else:
            flash('Your message has been sent successfully!', 'success')    
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Project Detail Route
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)







# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# import os
# import dotenv

# # loading environment variables
# dotenv.load_dotenv()

# app = Flask(__name__)

# # Fallback key for development if .env is missing
# app.secret_key = os.getenv('SECRET_KEY', 'default_dev_key')

# # database config
# # Use 'sqlite:///portfolio.db' as a default if DATABASE_URL isn't set
# database_url = os.getenv('DATABASE_URL', 'sqlite:///portfolio.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = database_url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Prevent stale SSL connections (common with hosted Postgres like Neon)
# if database_url.startswith('postgresql'):
#     app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
#         'pool_pre_ping': True,
#         'pool_recycle': 300,
#         'connect_args': {
#             'sslmode': 'require',
#             'keepalives': 1,
#             'keepalives_idle': 30,
#             'keepalives_interval': 10,
#             'keepalives_count': 5,
#         },
#     }

# db = SQLAlchemy(app)

# # Capitalized class name is standard convention
# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(200), nullable=False) 
#     image = db.Column(db.String(100), nullable=False)
#     link = db.Column(db.String(200), nullable=False)

# # Initialize DataBase
# with app.app_context():
#     db.create_all()
#     if Project.query.first() is None:
#         sample_project = Project(
#             title='Sample Project: Personal Portfolio',
#             description='A clean, responsive portfolio site built with Flask and SQLite.',
#             image='sample-project.svg',
#             link='https://example.com'
#         )
#         db.session.add(sample_project)
#         db.session.commit()

# # Home Route
# @app.route('/')
# def home():
#     # Fetch first 3 projects for the home page
#     projects = Project.query.limit(3).all() 
#     return render_template('index.html', projects=projects)

# # Projects Route
# @app.route('/projects')
# def projects():  # Function name MUST be 'projects' to match your HTML
#     # We use 'all_projects' here to avoid conflict with the function name
#     all_projects = Project.query.all()
#     return render_template('projects.html', projects=all_projects)

# # About Route
# @app.route('/about')
# def about():
#     return render_template('about.html')

# # Contact Route
# @app.route('/contact', methods=['GET', 'POST']) # Fixed list syntax
# def contact(): # Renamed from 'about' to 'contact'
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
        
#         if not name or not email or not message:
#             flash('All fields are required!', 'error')
#         else:
#             # Here you would typically save the message or email it
#             flash('Your message has been sent!', 'success')    
#             return redirect(url_for('home'))
    
#     return render_template('contact.html')

# # Project Detail Route (Missing in your original code)
# @app.route('/project/<int:project_id>')
# def project_detail(project_id):
#     project = Project.query.get_or_404(project_id)
#     return render_template('project_detail.html', project=project)

# if __name__ == '__main__':
#     app.run(debug=True)
