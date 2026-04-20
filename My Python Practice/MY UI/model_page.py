import streamlit as st

# List of image file paths or URLs
image_paths = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    "image4.jpg",
    "image5.jpg",
    "image6.jpg",
]

# Number of images per row (in this case, 3 images per row)
images_per_row = 3

# Title and description for the page
st.title("Software Studio APP")
st.write("This is a gallery displaying images in a 2x3 grid layout.")

# Display images in a grid format
for i in range(0, len(image_paths), images_per_row):
    cols = st.columns(images_per_row)  # Create columns for each row
    for idx, img_path in enumerate(image_paths[i:i+images_per_row]):
        with cols[idx]:
            st.image(img_path, use_column_width=True)  # Display image with column width


# Upload box
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)