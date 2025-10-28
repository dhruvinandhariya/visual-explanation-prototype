from transformers import pipeline

def create_slide_content(text, num_slides=8):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=500, min_length=200, do_sample=False)[0]['summary_text']

    points = summary.split(". ")
    slides = []
    for i, p in enumerate(points[:num_slides]):
        slides.append({
            "title": f"Key Point {i+1}",
            "bullets": [p],
            "notes": p
        })
    return slides
