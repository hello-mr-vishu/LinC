import os
import base64
import io
import openai
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify,send_file
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from pdf2image import convert_from_bytes
import google.generativeai as genai
from PIL import Image
from flask import render_template_string



# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

def create_tables():
    with app.app_context():
        db.create_all()

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    poppler_path = 'C:\\Program Files\\poppler-24.02.0\\Library\\bin' 
    images = convert_from_bytes(uploaded_file.read(), poppler_path=poppler_path)
    first_page = images[0]

    # Convert to bytes
    img_byte_arr = io.BytesIO()
    first_page.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    pdf_parts = [
        {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
        }
    ]
    return pdf_parts

@app.route('/')
def home():
    is_authenticated = 'user_id' in session
    return render_template('home.html', is_authenticated=is_authenticated)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('     Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('     Invalid username or password.', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('       You have been logged out.', 'success')
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_username = request.form['newUsername']
        new_password = generate_password_hash(request.form['newPassword'])
        # email = request.form['email']

        existing_user = User.query.filter_by(username=new_username).first()
        if existing_user:
            flash('Username already exists!', 'danger')
        else:
            new_user = User(username=new_username, password=new_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/streamlit')
def streamlit_embed():
    return redirect("http://localhost:8501")


@app.route('/part-time-jobs')
def part_time_jobs():
    # Render the jobs page
    return render_template('job-list.html')


@app.route('/job-detail')
def job_detail():
    return render_template('job-detail.html')

@app.route('/job-list')
def job_list():
    return render_template('job-list.html')

@app.route('/freelancing')
def freelancing():
    # Render the freelancing page
    return render_template('job-list.html')

@app.route('/career-counseling')
def career_counseling():
    # Render the career counseling page
    return render_template('career-counseling.html')

@app.route('/ats')
def ats():
    return render_template('ats.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify({"error": "No file uploaded"}), 400

    uploaded_file = request.files['file']
    input_text = request.form['input_text'] 
    action = request.form['action']

    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        
        if action == "Tell Me About the Resume":
            input_prompt = """
            You are an experienced Technical Human Resource Manager. Your task is to review the provided resume of a student against the provided job description from an organization looking to fill a part-time or freelance position.
        
        First, display the student's name.
        Second, list their skills.
        Third, provide their educational background.
        
        Next, provide a detailed evaluation of whether the student's profile aligns with the role specified in the job description.
        Highlight the strengths and weaknesses of the student's resume in relation to the job requirements outlined by the organization.
        Focus on the student's relevant skills, experience, educational background, and any projects or internships that demonstrate their suitability for the role.
        Additionally, mention any notable achievements or certifications that enhance the student's profile.
        Provide a clear and concise summary of how well the student's qualifications match the job description.
            """


        elif action == "Percentage match":
            input_prompt = """
            You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of part-time and freelance job requirements.
    Your task is to evaluate the student's resume against the provided job description from an organization. Calculate the percentage match of the resume to the job description.
    
    First, provide the match percentage.
    Second, list any missing keywords or skills that are critical for the job.
    Third, offer your overall assessment of the student's fit for the role, highlighting their strengths and areas for improvement.
    
    Your evaluation should help the student understand how closely their resume aligns with the job requirements and what they can improve.
            """


        
        response = get_gemini_response(input_text, pdf_content, input_prompt)
        return jsonify({"response": response})

    return jsonify({"error": "Error processing the file"}), 500



if __name__ == '__main__':
    create_tables()
    app.run(debug=True)

