# 🎯 ATS Resume Scanner

## AI-Powered Resume Analysis Tool for Job Applications

[![Deploy to GitHub Pages](https://github.com/abhizazu/ATS--Scanner-2/actions/workflows/deploy.yml/badge.svg)](https://github.com/abhizazu/ATS--Scanner-2/actions/workflows/deploy.yml)

## 🚀 Project Overview

ATS Resume Scanner is a powerful web application that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). The application analyzes how well a resume matches a specific job description by extracting important keywords, calculating a match score, and identifying missing keywords that could improve the resume's ATS compatibility.

This project combines a Flask backend for robust text analysis with a clean, responsive frontend interface, demonstrating skills in full-stack web development, natural language processing, and creating user-friendly applications.

## ✨ Features

- **💻 Resume Analysis**: Upload or paste resume text for instant, accurate analysis
- **📋 Job Description Matching**: Sophisticated algorithm identifies key terms from job descriptions
- **🎯 Smart Scoring System**: Calculates precise percentage match based on keyword presence and importance
- **🔍 Missing Keywords Identification**: Highlights critical skills or qualifications missing from your resume
- **⚡ Fast & Efficient**: Optimized algorithms provide instant results
- **🔄 Client-Server Architecture**: Combines frontend simplicity with backend processing power
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ How to Use

1. Visit the application in your web browser
2. Paste your resume text in the "Resume" field
3. Paste the job description in the "Job Description" field
4. Click "Analyze Resume"
5. Review your match score and any missing keywords
6. Update your resume based on the analysis to improve your chances

## 🔧 Technical Architecture

### Frontend
- **HTML/CSS/JavaScript**: Clean, responsive user interface
- **Vanilla JS**: Lightweight client-side processing for immediate user feedback
- **Responsive Design**: Adapts to different screen sizes and devices

### Backend
- **Flask**: Python web framework for handling API requests
- **Natural Language Processing**: Custom algorithms for text analysis and keyword extraction
- **RESTful API**: Clean API endpoints for resume analysis

### Deployment
- **GitHub Actions**: Automated CI/CD pipeline
- **GitHub Pages**: Static hosting for the application

## 🧰 Project Structure

```
ATS--Scanner-2/
├── .github/                # GitHub configuration
│   └── workflows/          # CI/CD workflows
│       └── deploy.yml      # GitHub Pages deployment
├── backend/                # Server-side code
│   ├── app.py              # Flask application & API endpoints
│   └── parser_utils.py     # Text analysis utilities
├── frontend/               # Client-side code
│   └── index.html          # Main application interface
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Flask

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/ATS--Scanner-2.git
   cd ATS--Scanner-2
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application
   ```bash
   python backend/app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## 💡 Key Insights & Learning

- **Text Analysis Techniques**: Implemented efficient algorithms for keyword extraction and matching
- **Full-Stack Development**: Balanced frontend user experience with backend processing capabilities
- **Deployment Automation**: Configured GitHub Actions for seamless deployment
- **User Experience Design**: Created an intuitive interface for non-technical users

## 🔮 Future Enhancements

- **Advanced NLP**: Implement more sophisticated natural language processing for better keyword extraction
- **PDF/DOCX Parsing**: Add support for direct file uploads in various formats
- **Industry-Specific Analysis**: Customize analysis based on different industries and job types
- **Suggestion Engine**: Provide specific recommendations for improving resume content

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Developed with ❤️ by ABHI

