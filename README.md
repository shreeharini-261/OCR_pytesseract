# Real-Time OCR with Branding Overlay

This project captures real-time video frames from a camera, adds a customizable branding overlay, and performs OCR (Optical Character Recognition) on frames where the 'c' key is pressed. OCR results, including text and bounding box coordinates, are saved to an Excel file.

## Features
- **Real-Time Video Capture**: Captures frames from the default camera.
- **Branding Overlay**: Adds a semi-transparent branding overlay to each frame.
- **OCR Extraction**: Extracts text from frames when the 'c' key is pressed, saving text data and bounding boxes to an Excel file.
- **Save OCR Output**: OCR results are saved to `ocr_output.xlsx`.

## Prerequisites
Ensure you have Python 3.x installed and the required dependencies listed in `requirements.txt`.

### Installation

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Tesseract Installation**:
    - [Install Tesseract](https://github.com/tesseract-ocr/tesseract) on your system if not already installed.
    - Ensure `pytesseract` can access the Tesseract executable. You may need to set the Tesseract path:
        ```python
        pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'
        ```

## Usage

1. **Run the Script**:
    ```bash
    python ocr_code.py
    ```

2. **Controls**:
    - **'c' key**: Capture OCR data from the current frame.
    - **'q' key**: Quit the application.

3. **OCR Output**:
   - After running the script, OCR results will be saved to `ocr_output.xlsx`, including:
      - Detected text
      - Bounding box coordinates
      - OCR confidence score

## Project Structure

- `ocr_code.py`: The main script file that contains code for real-time OCR and branding overlay.
- `requirements.txt`: File to install all required dependencies.

## Troubleshooting

- **Failed to grab frame**: Ensure your webcam is connected properly.
- **Tesseract not found**: Check the Tesseract installation path and update `pytesseract.pytesseract.tesseract_cmd`.

## License
This project is licensed under the MIT License.
