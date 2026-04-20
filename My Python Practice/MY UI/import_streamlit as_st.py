import streamlit as st
from PIL import Image

# Create an upload box for multiple images
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# Check if any files are uploaded
if uploaded_files:
    st.write(f"Number of images uploaded: {len(uploaded_files)}")

    # Display each image
    for i, uploaded_file in enumerate(uploaded_files):
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded Image {i+1}", use_column_width=True)
else:
    st.write("No images uploaded.")
