import time
from gtts import gTTS
from langdetect import detect
import pdfplumber
import os
from tkinter import filedialog as fd


# Allow selection of PDF File
def select_file():
    filetypes = (
        ('pdf files', '*.pdf'),
    )

    filename = fd.askopenfilename(
        title='Choose a PDF File to convert to an Audio Book',
        initialdir='/',
        filetypes=filetypes)

    return filename


# Get title of PDF File
pdf = select_file()
pdf_title = pdf.split(".")[0].split('/')[-1]

# Convert PDF to Txt File
with pdfplumber.open(pdf) as pdf_file:
    # Initialize an empty string to store the extracted text
    extracted_text = ''

    # Iterate through each page and extract text
    for page in pdf_file.pages:
        extracted_text += page.extract_text()

with open(f'{pdf_title}.txt', mode='a') as file:
    print('Converting PDF to Audio...')
    file.write(extracted_text)

# NLP Language Detection
with open(f"{pdf_title}.txt") as file:
    contents = file.read()
    lang = detect(contents)
    tts = gTTS(text=contents, lang=lang)
    tts.save(f"{pdf_title}.mp3")
    print('Almost there...')
    time.sleep(5)
    print('Done! Enjoy!')
    os.system(f"open {pdf_title}.mp3")
