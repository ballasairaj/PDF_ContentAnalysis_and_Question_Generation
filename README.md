📄 AI PDF Visual Question Generator (RAG-Based)

An AI-powered document analysis system that processes PDF files, extracts text and images, and generates context-aware questions from visual content using deep learning models.
The system combines BLIP (for image captioning) and T5 (for question generation) to automatically create educational questions from images found inside PDFs.

This project demonstrates Retrieval-Augmented Generation (RAG), multimodal AI, and document intelligence using Python and Streamlit.

🚀 Features

📄 Upload PDF documents through a Streamlit web interface

📝 Extract text and images from PDF pages

🖼️ Generate image captions using BLIP

❓ Automatically generate questions from captions using T5 Question Generation model

📊 Display results interactively with images, captions, and generated questions

💾 Download generated results as structured JSON


🧠 Tech Stack

- Python

- Streamlit – Web interface

- PyMuPDF (fitz) – PDF parsing and image extraction

- Transformers (HuggingFace) – AI models

- BLIP – Image captioning

- T5 Question Generation Model – Question generation

- PIL (Python Imaging Library) – Image processing


🏗️ System Architecture

- PDF Upload

- Document Parsing

- Extract text

- Extract images

- Image Caption Generation

- BLIP model generates captions

- Question Generation

- T5 model generates questions from captions

- Output Display

- Image

- Caption

- Generated Question

- Export Results

- JSON output

📂 Project Structure
project/
│
├── extracted_images/
│   └── (Images extracted from PDF)
│
├── output/
│   ├── structured_output.json
│   └── generated_questions.json
│
├── app.py
├── requirements.txt
└── README.md
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/ai-pdf-question-generator.git
cd ai-pdf-question-generator
2️⃣ Install dependencies
pip install -r requirements.txt

Or install manually:

pip install streamlit transformers torch pillow pymupdf
3️⃣ Run the Streamlit App
streamlit run app.py
📊 Example Workflow

Upload an educational PDF

The system:

Extracts images and text

Generates captions for images

Produces AI-generated questions

Results appear in the interface with:

Image

Caption

Generated Question

📤 Example Output
Image: page1_img1.png

Caption:
"A diagram showing the structure of a human heart"

Generated Question:
"What are the main parts of the human heart shown in the diagram?"
🎯 Use Cases

📚 Educational content analysis

🧑‍🏫 Automatic question generation for learning materials

📄 Intelligent document understanding

🤖 AI-powered study material creation

🧠 Multimodal AI research projects

🔮 Future Improvements

Add text-based question answering from PDF content

Implement vector database (FAISS/Chroma) for full RAG pipeline

Support multiple languages

Improve UI with chat-based interaction

Add LLM-based summarization

👨‍💻 Author

Sairaj Balla
AI / Machine Learning Enthusiast
B.Tech Computer Science Engineering
