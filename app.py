from flask import Flask, render_template, request, send_file
import numpy as np
from PIL import Image, ImageDraw
import io
from monai.data import SyntheticDataset

app = Flask(__name__)

def generate_medical_image(text):
    # Simulate synthetic data generation (replace with MONAI's generative models)
    # For demo: Create a simple image with text overlay
    width, height = 256, 256
    img = Image.new("L", (width, height), color=0)  # Grayscale
    draw = ImageDraw.Draw(img)
    
    # Add text to the image (simulate anatomy labels)
    draw.text((10, 10), f"Mock {text}", fill=255)
    
    # Add synthetic "anatomy" shapes (circles, rectangles)
    draw.rectangle([50, 50, 200, 200], outline=255)
    draw.ellipse([80, 80, 180, 180], outline=255)
    
    return img

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        img = generate_medical_image(text)
        
        # Save image to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")
        img_byte_arr.seek(0)
        
        return send_file(img_byte_arr, mimetype="image/png")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
