import cv2
import easyocr
from PIL import ImageGrab
import os


print("Starting...")

# Grab image from clipboard
im = ImageGrab.grabclipboard()

if im is not None:
    # Save the image to a file
    im.save('somefile.png', 'PNG')
    print("Image saved successfully.")
    
    # Open the saved image using OpenCV
    img = cv2.imread('somefile.png')

    # Perform OCR
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img)

    # Extracted text
    extracted_text = ' '.join([text[1] for text in result])

    f = open("converted.txt", "w")
    f.write(extracted_text)
    f.close()

    os.system("notepad.exe converted.txt")
    
    # Print the extracted text
    print("Extracted text:")
    print(extracted_text)

else:
    print("No image found on the clipboard.")
