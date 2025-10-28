# Visual Explanation Prototype

This project converts a PDF (e.g., textbook chapter) into:
- A short PowerPoint/PDF slide deck (6–12 slides)
- A short explainer video with narration (30–90s)

## 🚀 How to Run
```bash
pip install -r requirements.txt
python run_pipeline.py --input sample.pdf --outdir output/
```

Outputs:
- `output/slides.pptx`
- `output/video.mp4`

## ⚙️ Tech Stack
Python, pdfplumber, transformers, python-pptx, moviepy, pyttsx3

## 📄 Demo
Run the script on `sample.pdf` and view results in `output/`.
