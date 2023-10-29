import openai
from flask import Flask, request, render_template
from PyPDF2 import PdfReader
import docx2txt
import os

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    page = reader.pages[0]
    resume_text = page.extract_text()
    return resume_text

def extract_text_from_docx(docx_file):
    docx_text = docx2txt.process(docx_file)
    return docx_text

app = Flask(__name__)


# Define a folder to temporarily store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


openai.api_key = 'your_openai_api_key'

# Define a function to match a single resume with a given job description (JD)
def match_resume_with_jd(resume, jd):
    # Use the OpenAI API to generate a rating for the resume based on the JD
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Please rate the following resume on a scale of 0-10 based on its fit for the following job description:\n\n{jd}\n\nResume:\n{resume}\n\nRating:"),
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Parse the rating from the API response
    rating = float(response.choices[0].text)

    # Use the OpenAI API to generate a reason for the rating
    reason_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Can you please explain why you gave the following resume a rating of {rating} for this job description:\n\n{jd}\n\nResume:\n{resume}\n\nReason:"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    reason = reason_response.choices[0].text

    return rating, reason

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/Resume', methods=['POST'])
def resume_rating():

    resume_file = request.files['resume_files']
    if resume_file.filename == '':
        return "No selected file", 400
    
    # Save the uploaded file to the UPLOAD_FOLDER
    uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
    resume_file.save(uploaded_file_path)

    # Check file format and extract text
    if uploaded_file_path.endswith('.pdf'):
        resume_text = extract_text_from_pdf(uploaded_file_path)
    elif uploaded_file_path.endswith('.docx'):
        resume_text = extract_text_from_docx(uploaded_file_path)
    else:
        return "Unsupported file format", 400

    # Get the job description from the form submission
    jd = request.form['job_description']

    # Call the function to rate the resume and get the reason
    rating, reason = match_resume_with_jd(resume_text, jd)

    # Render the result using the HTML template
    return render_template('result.html', rating=rating, reason=reason)

if __name__ == '__main__':
    app.run(debug=True)
