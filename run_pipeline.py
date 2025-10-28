import argparse
from modules import pdf_extraction, summarization, slide_maker, tts_and_video
import os

def main():
    parser = argparse.ArgumentParser(description="PDF to Slides + Video Pipeline")
    parser.add_argument("--input", required=True, help="Path to input PDF")
    parser.add_argument("--outdir", default="output", help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    print("📘 Step 1: Extracting text from PDF...")
    raw_text = pdf_extraction.extract_text(args.input)

    print("🧩 Step 2: Summarizing and creating slide content...")
    slides_data = summarization.create_slide_content(raw_text)

    print("🖼️ Step 3: Creating PowerPoint slides...")
    slides_path = slide_maker.create_ppt(slides_data, args.outdir)

    print("🎤 Step 4: Generating video with TTS narration...")
    video_path = tts_and_video.generate_video(slides_data, slides_path, args.outdir)

    print(f"✅ Done! Outputs saved in: {args.outdir}")
    print(f"Slides: {slides_path}")
    print(f"Video: {video_path}")

if __name__ == "__main__":
    main()
