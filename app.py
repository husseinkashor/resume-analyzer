from flask import Flask, request, render_template
from resume_parser import extract_text
from analyzer import analyze_resume
from grammar_check import check_grammar
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            text = extract_text(filepath)
            analysis = analyze_resume(text)
            grammar_issues = check_grammar(text)

            return render_template('index.html', analysis=analysis, grammar=grammar_issues)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
