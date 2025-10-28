import pyttsx3
from moviepy.editor import ColorClip, concatenate_videoclips, AudioFileClip, ImageClip
from PIL import Image, ImageDraw, ImageFont
import os

def generate_video(slides_data, ppt_path, outdir):
    engine = pyttsx3.init()
    voice_path = os.path.join(outdir, "narration.mp3")

    # ---- 1. Create narration audio ----
    narration_text = " ".join([s['notes'] for s in slides_data])
    engine.save_to_file(narration_text, voice_path)
    engine.runAndWait()

    # ---- 2. Helper to create an image with text ----
    def create_slide_image(title, bullets, size=(1280, 720)):
        img = Image.new("RGB", size, color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        try:
            title_font = ImageFont.truetype("arial.ttf", 48)
            bullet_font = ImageFont.truetype("arial.ttf", 32)
        except:
            title_font = ImageFont.load_default()
            bullet_font = ImageFont.load_default()

        # Title
        draw.text((60, 60), title, font=title_font, fill=(0, 0, 0))

        # Bullets
        y = 160
        for b in bullets:
            draw.text((100, y), f"• {b}", font=bullet_font, fill=(50, 50, 50))
            y += 60

        temp_path = os.path.join(outdir, f"slide_temp_{hash(title)}.png")
        img.save(temp_path)
        return temp_path

    # ---- 3. Make moviepy clips ----
    clips = []
    for slide in slides_data:
        slide_img = create_slide_image(slide["title"], slide["bullets"])
        clip = ImageClip(slide_img).set_duration(6)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    # ---- 4. Add TTS audio ----
    if os.path.exists(voice_path):
        video = video.set_audio(AudioFileClip(voice_path))

    # ---- 5. Write output ----
    video_path = os.path.join(outdir, "video.mp4")
    video.write_videofile(video_path, fps=24)

    # Cleanup temporary images
    for slide in slides_data:
        temp_file = os.path.join(outdir, f"slide_temp_{hash(slide['title'])}.png")
        if os.path.exists(temp_file):
            os.remove(temp_file)

    return video_path
