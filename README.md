# Clipboard Image to Text Converter

This Python script captures an image from the clipboard, performs Optical Character Recognition (OCR) to extract text from the image, saves the extracted text to a file, and opens the file in a text editor. The temporary files are deleted after the text editor is closed. OCR is done locally.

## Features

- Captures an image from the clipboard
- Saves the image to a temporary file
- Performs OCR on the saved image using EasyOCR
- Extracts text and saves it to a temporary text file
- Opens the text file in the default text editor (gedit)
- Deletes the temporary files after the text editor is closed

## Requirements

- Python 3.x
- OpenCV
- EasyOCR
- Pillow
- gedit (default text editor on many Linux distributions)
- xclip - linux
- gnome-screenshot - linux

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/tren03/ocrauto
    cd ocrauto
    ```

2. **Install the required Python packages:**

    ```sh
    pip install opencv-python easyocr pillow
    ```
3. **Add the following to your bashrc file:**

    ```sh
    ocrauto() {
        TEMP_FILE=$(mktemp /tmp/screenshot-XXXXXX.png)
        gnome-screenshot -a -f "$TEMP_FILE"
        xclip -selection clipboard -t image/png -i "$TEMP_FILE"
        rm "$TEMP_FILE"
        python3 <path to main.py file of this rep>
    }
    ```
3. **Update bashrc:**

    ```sh
    source ./bashrc
    ```

## Usage

1. **Run this on bash terminal:**

    ```sh
    ocrauto
