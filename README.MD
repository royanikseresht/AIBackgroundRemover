# AI Background Remover

An easy-to-use web application that allows users to remove the background from images using machine learning models. Built with Python, Streamlit, and the `rembg` library, this app provides a simple interface for quickly uploading an image and obtaining a background-free version.

## Features

- Upload PNG, JPG, or JPEG images.
- Automatically remove the background from the uploaded image.
- Display the original and processed image side by side.
- Simple and minimalistic user interface.
- Built with Streamlit for quick deployment.

## Technologies Used

- **Python 3.7+**
- **Streamlit**: A web framework for creating interactive applications.
- **rembg**: A library that uses machine learning to remove backgrounds from images.
- **Pillow**: Python Imaging Library (PIL), used for handling and processing images.
- **requests**: For fetching resources over the network, e.g., Lottie animations.
- **pandas & numpy**: For handling data manipulation (used for map plotting functionality).
- **Lottie Animations** (optional): Custom or external animations to enhance the user interface.

## Installation

### Prerequisites

Make sure you have Python 3.7 or higher installed. You'll also need to install the required libraries using `pip`.

### 1. Clone the Repository

```bash
git clone https://github.com/royanikseresht/AIBackgroundRemover.git
cd AIBackgroundRemover

python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

pip install -r requirements.txt

streamlit run Home.py
