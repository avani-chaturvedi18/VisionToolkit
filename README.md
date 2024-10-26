# Image Processing App with OpenCV and Streamlit

This is an interactive image processing application built using Streamlit and OpenCV. With this app, you can upload an image and apply various transformations, such as binarization, resizing, denoising, edge detection, and object segmentation, using an intuitive interface.

## Features

The app provides the following functionalities:

1. **Image Binarization**: Convert an image to a binary (black-and-white) format based on a selected threshold.
2. **Image Resizing**: Resize the image to specified width and height dimensions.
3. **Image Denoising**: Apply Gaussian, Median, or Bilateral denoising filters to reduce noise.
4. **Edge Detection**: Detect edges in the image using Canny, Laplacian, or Sobel edge detection techniques.
5. **Object Segmentation**: Segment specific objects from the image based on HSV color range selection.

## How to Use

1. **Upload an Image**: Use the file uploader to select a JPEG or PNG image.
2. **Select Operations**: In the sidebar, you can choose various image processing options:
   - **Binarization**: Choose a threshold value (0–255) to binarize the image.
   - **Resize**: Enter the desired width and height to resize the image.
   - **Denoising**: Select a denoising method (Gaussian, Median, Bilateral) to reduce noise in the image.
   - **Edge Detection**: Choose an edge detection technique (Canny, Laplacian, SobelX, SobelY) to highlight edges in the image.
   - **Object Segmentation**: Adjust HSV sliders to segment specific color ranges in the image.
3. **View Results**: The app will display the processed image(s) based on the selected options.

## Installation

To run this application, ensure you have [Python](https://www.python.org/downloads/) installed, and install the required packages with:

```bash
pip install streamlit opencv-python-headless
```

## Running the App

Save the code provided in a file (e.g., `app.py`), then run the app by navigating to the file location in the terminal and entering:

```bash
streamlit run app.py
```

This will open the app in your default web browser. You can now upload an image and explore the available image processing features.


## Additional Notes

- The object segmentation feature is based on HSV color ranges. Adjusting the sliders can help isolate specific colors for segmentation.
- Image resizing maintains the original aspect ratio by default; you can adjust both width and height as desired.
- For edge detection, the output will be in grayscale, highlighting only the detected edges.

## Technologies Used

- **Streamlit**: For building an interactive web interface.
- **OpenCV**: For image processing operations.
- **Pillow (PIL)**: For handling image uploads and conversions in Streamlit.
