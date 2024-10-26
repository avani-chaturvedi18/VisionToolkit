import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Function to binarize an image
def binarize_image(image, threshold=127):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return binary_img

# Function to resize an image
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Function to denoise an image
def denoise_image(image, method='Gaussian'):
    if method == 'Gaussian':
        return cv2.GaussianBlur(image, (5, 5), 0)
    elif method == 'Median':
        return cv2.medianBlur(image, 5)
    elif method == 'Bilateral':
        return cv2.bilateralFilter(image, 9, 75, 75)
    return image

# Function to perform edge detection
def edge_detection(image, method='Canny'):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if method == 'Canny':
        return cv2.Canny(gray, 100, 200)
    elif method == 'Laplacian':
        return cv2.Laplacian(gray, cv2.CV_64F)
    elif method == 'SobelX':
        return cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    elif method == 'SobelY':
        return cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    return gray

# Function for object segmentation (simple segmentation by color range)
def segment_object(image, lower_bound, upper_bound):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    segmented_img = cv2.bitwise_and(image, image, mask=mask)
    return segmented_img

st.title("Image Processing with OpenCV and Streamlit")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file))
    st.image(image, caption='Original Image', use_column_width=True)

    st.sidebar.title("Choose Operations")

    # Binarization
    if st.sidebar.checkbox("Binarize Image"):
        threshold = st.sidebar.slider("Threshold", 0, 255, 127)
        binary_img = binarize_image(image, threshold)
        st.image(binary_img, caption='Binarized Image', use_column_width=True, channels="GRAY")

    # Resize
    if st.sidebar.checkbox("Resize Image"):
        width = st.sidebar.number_input("Width", value=image.shape[1])
        height = st.sidebar.number_input("Height", value=image.shape[0])
        resized_img = resize_image(image, int(width), int(height))
        st.image(resized_img, caption='Resized Image', use_column_width=True)

    # Denoise
    if st.sidebar.checkbox("Denoise Image"):
        denoise_method = st.sidebar.selectbox("Denoise Method", ["Gaussian", "Median", "Bilateral"])
        denoised_img = denoise_image(image, denoise_method)
        st.image(denoised_img, caption='Denoised Image', use_column_width=True)

    # Edge Detection
    if st.sidebar.checkbox("Edge Detection"):
        edge_method = st.sidebar.selectbox("Edge Detection Method", ["Canny", "Laplacian", "SobelX", "SobelY"])
        edges = edge_detection(image, edge_method)
        st.image(edges, caption='Edge Detected Image', use_column_width=True)

    # Object Segmentation
    if st.sidebar.checkbox("Segment Object"):
        lower_hue = st.sidebar.slider("Lower Hue", 0, 179, 0)
        lower_sat = st.sidebar.slider("Lower Saturation", 0, 255, 0)
        lower_val = st.sidebar.slider("Lower Value", 0, 255, 0)
        upper_hue = st.sidebar.slider("Upper Hue", 0, 179, 179)
        upper_sat = st.sidebar.slider("Upper Saturation", 0, 255, 255)
        upper_val = st.sidebar.slider("Upper Value", 0, 255, 255)
        
        lower_bound = np.array([lower_hue, lower_sat, lower_val])
        upper_bound = np.array([upper_hue, upper_sat, upper_val])
        
        segmented_img = segment_object(image, lower_bound, upper_bound)
        st.image(segmented_img, caption='Segmented Image', use_column_width=True)
