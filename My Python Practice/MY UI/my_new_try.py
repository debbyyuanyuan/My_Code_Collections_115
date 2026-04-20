import streamlit as st
from PIL import Image

# Title and description for the page
st.title("Software Studio APP")
st.write("This is a gallery displaying images in a 2x3 grid layout.")

# Upload an image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Open the image using PIL
    img = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(img, caption='Tags:', use_column_width=True)
else:
    st.write("Please upload an image file.")

import pandas as pd
from io import StringIO

# List of image file paths or URLs
image_paths = [
    "https://i.pinimg.com/originals/7b/f0/33/7bf03326844b0ad2da2c9c1a40bc7d6e.png",
    "https://i.pinimg.com/originals/85/70/5c/85705c379b8ba1d732604cffad8b626f.jpg",
    "https://i.pinimg.com/originals/c0/79/2e/c0792e0c40de4caf66b0746c69c68890.jpg",
    "https://i.pinimg.com/originals/20/93/45/2093450c389053f34909b209b15c46d3.jpg",
    "https://i.pinimg.com/originals/e3/e5/be/e3e5be538eddbdedb05c34cafa5ae709.jpg",
    "https://i.pinimg.com/originals/fc/d4/cf/fcd4cfb8030fe0502e1a52f27ebb07dc.jpg"
]

# Corresponding captions for each image
captions = [
    "Animal 1",
    "Animal 2",
    "Animal 3",
    "Animal 4",
    "Animal 5",
    "Animal 6"
]
# Fixed image width (in pixels)
image_width = 250
image_height = 300

# Number of images per row (in this case, 3 images per row)
images_per_row = 3

# Display images in a grid format
for i in range(0, len(image_paths), images_per_row):
    cols = st.columns(images_per_row)  # Create columns for each row
    for idx, img_path in enumerate(image_paths[i:i+images_per_row]):
        with cols[idx]:
            # Use an anchor tag to make the image clickable and open in a new tab
            st.markdown(f"""
            <a href='{img_path}' target='_blank'>
                <img src='{img_path}' style='width:{image_width}px; height:{image_height}px;'>
            </a>""", unsafe_allow_html=True)
            # Center the caption using HTML
            st.markdown(f"<p style='text-align: center;'>{captions[i + idx]}</p>", unsafe_allow_html=True)

# Custom CSS to enhance the interface design
st.markdown("""
    <style>
    /* Set background color for the whole page */
    body {
        background-color: #f0f0f5;
    }
    /* Style the title */
    .stTitle {
        color: #333;
        font-family: 'Ariel Black', sans-serif;
        text-align: center;
        margin-bottom: 20px;
    }
    /* Style for captions */
    p {
        color: #555;
        font-size: 16px;
        font-family: 'Montserrat', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Add a selectbox to filter images by category
category = st.sidebar.selectbox("Select Category", ["Most releveant", "Most popular", "Highest Score", "Lowest score"])

