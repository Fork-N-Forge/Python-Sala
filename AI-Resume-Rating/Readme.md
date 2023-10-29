# Resume Rating Web Application

The Resume Rating Web Application is a Python Flask-based web tool that allows users to upload a resume and receive a rating on how well it matches a given job description. This tool leverages the OpenAI API to assess the fit between a resume and a job description and provides a detailed reason for the rating.

## Features

- **Resume Upload**: Users can upload their resume in either PDF or DOCX format. The application extracts text from the uploaded file for analysis.

- **Job Description**: Users can input the job description for which they want to evaluate the resume.

- **Rating Generation**: The application sends the resume and job description to the OpenAI API, which generates a rating on a scale of 0 to 10, indicating how well the resume matches the job description.

- **Reasoning**: The tool also provides a detailed reason for the rating generated. This helps users understand why their resume received a particular score and suggests areas for improvement.

## Requirements

To run this web application, you'll need the following components:

- Python 3.x
- Flask
- PyPDF2
- docx2txt
- OpenAI API Key

## Setup

1. Clone or download the repository.

2. Install the required Python packages using pip:

   ```bash
   pip install Flask PyPDF2 docx2txt openai
   ```

3. Sign up for an OpenAI API key and replace `'your_openai_api_key'` in the code with your actual API key.

4. Run the Flask application:

   ```bash
   python main.py
   ```

The application will be accessible in your web browser at `http://localhost:5000`.

## Usage

1. Access the application in your web browser.

2. Upload your resume in either PDF or DOCX format.

3. Enter the job description for which you want to evaluate your resume.

4. Click the "Analyze Resume" button.

5. The application will use the OpenAI API to rate your resume and provide a detailed reason for the rating.

6. You will receive a JSON response with the rating and reason.

## Supported File Formats

The application supports resume files in the following formats:

- PDF (.pdf)
- Microsoft Word (.docx)

Unsupported file formats will result in an error message.

## Disclaimer

- The accuracy of the rating and the reasoning provided depends on the capabilities of the OpenAI API and the quality of the job description and resume provided. The application is not a definitive evaluation tool but rather a helpful aid.

- Ensure that you handle sensitive information and data privacy issues appropriately, as the application involves the uploading of personal resumes.

## Acknowledgments

- This application is built using the OpenAI GPT-3.5 model, and we acknowledge OpenAI for their contributions to natural language processing.

- We also thank the open-source community for providing tools and libraries that make projects like this possible.