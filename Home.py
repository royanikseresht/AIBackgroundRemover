import streamlit as st
from PIL import Image
import io
from rembg import remove

def main():
    """
    Main Function
    """
    st.set_page_config(
        page_title="AI Background Remover",
        page_icon="./assets/favicon.ico",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/royanikseresht/AIBackgroundRemover',
            'Report a bug': "https://github.com/royanikseresht/AIBackgroundRemover/issues",
            'About': "## A minimalistic application to remove image backgrounds built using Python."
        })

    st.title("AI Background Remover")
    uploaded_img = st.file_uploader(label="Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

    if uploaded_img is not None and st.button("Generate"):
        try:
            # Load the input image using PIL
            img = Image.open(uploaded_img)

            # Convert the image to raw bytes to pass to rembg
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')  # Save the image in PNG format
            img_byte_arr = img_byte_arr.getvalue()

            # Remove the background using rembg
            result = remove(img_byte_arr)

            # Convert the result back into a PIL Image
            result_img = Image.open(io.BytesIO(result))

            # Display the input and output images side by side
            col1, col2 = st.columns([2, 2], gap="large")
            with col1:
                st.markdown("### Input Image")
                st.image(img, caption="Original Image", use_column_width=True)

            with col2:
                st.markdown("### After Background Removal")
                st.image(result_img, caption="Processed Image", use_column_width=True)

        except Exception as e:
            st.error(f"Error processing the image: {str(e)}")

if __name__ == "__main__":
    main()
