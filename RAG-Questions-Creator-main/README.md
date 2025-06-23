# AI-Powered Exam Question Generator from PDF Documents

A streamlined web application that automatically generates customized exam questions from PDF documents using AI. The application leverages Google's Generative AI to create high-quality, context-aware questions with varying difficulty levels and formats.

This project combines document processing, natural language understanding, and vector similarity search to create an intelligent question generation system. It allows educators and students to quickly generate relevant exam questions from their study materials, supporting multiple question formats including multiple choice, true/false, short answer, and essay questions. The application uses FAISS for efficient similarity search and supports saving generated questions as downloadable PDF files.

## Repository Structure
```
.
├── frontend.py              # Main Streamlit web interface implementation
├── requirements.txt         # Project dependencies and package versions
├── src/                    # Core application source code
│   ├── __init__.py         # Python package marker
│   └── helper.py           # Core functionality for PDF processing and question generation
└── temp.py                 # Utility script for project structure setup
```

## Usage Instructions
### Prerequisites
- Python 3.7 or higher
- Google Generative AI API key
- Sufficient storage space for vector embeddings

Required Python packages:
```txt
streamlit
google-generativeai
python-dotenv
langchain
PyPDF2
faiss-cpu
langchain-google-genai
fpdf
```

### Installation

1. Clone the repository:
```bash
git clone <[repository-url](https://github.com/MohammedHamza0/RAG-Questions-Creator.git)>
cd <RAG-Questions-Creator>
```

2. Create a virtual environment with Python 3.10:
```bash
# Windows
python -m venv venv --python=python3.10
# or
py -3.10 -m venv venv

# macOS/Linux
python3.10 -m venv venv
```

3. Activate the virtual environment:
```bash


4. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### Quick Start

1. Start the application:
```bash
streamlit run frontend.py
```

2. Upload PDF documents through the sidebar
3. Click "Process" to analyze the documents
4. Configure question generation parameters:
   - Enter your query
   - Select number of questions (10-100)
   - Choose difficulty level (easy/medium/hard)
   - Select question type
5. Click "Generate" to create questions
6. Save or download the generated questions as PDF

### More Detailed Examples

Generate Multiple Choice Questions:
```python
# Example configuration
question = "Generate exam questions about chapter 1"
num_questions = 20
difficulty_level = "medium"
question_types = "multiple choice"
```

Generate Mixed Format Questions:
```python
# Example configuration
question = "Create a comprehensive exam"
num_questions = 50
difficulty_level = "hard"
question_types = ["multiple choice", "essay", "short answer"]
```

### Troubleshooting

Common Issues:

1. PDF Text Extraction Fails
   - Error: "Couldn't extract any text from the PDF"
   - Solution: Ensure PDF is not scanned/image-based
   - Try converting to searchable PDF first

2. API Key Issues
   - Error: "API key not found"
   - Solution: 
     - Verify .env file exists
     - Check GEMINI_API_KEY is correctly set
     - Restart application after setting key

3. Memory Issues with Large PDFs
   - Error: Out of memory
   - Solution:
     - Reduce chunk size in get_text_chunks()
     - Process smaller PDF files
     - Increase available system memory

## Data Flow
The application processes PDFs through a pipeline of text extraction, chunking, embedding, and question generation.

```ascii
PDF Files → Text Extraction → Chunking → Vector Embedding → FAISS Store
    ↓                                                          ↓
User Query → Similarity Search → Context Retrieval → Question Generation → PDF Output
```

Key Component Interactions:
1. PDF processor extracts raw text using PyPDF2
2. Text splitter creates manageable chunks for processing
3. Google's embedding model converts text to vectors
4. FAISS handles vector storage and similarity search
5. Gemini AI generates questions based on retrieved context
6. FPDF creates downloadable PDF output
7. Streamlit manages user interaction and display
