from tkinter.filedialog import askopenfilename, asksaveasfilename
import pyttsx3
import pdfplumber
import PyPDF2
from tkinter import Tk

Tk().withdraw()
file = askopenfilename()

pdfFileObj = open(file, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_of_pages = pdfReader.numPages

text_to_say = ''
with pdfplumber.open(file) as pdf:
    for i in range(0, num_of_pages):
        page = pdf.pages[i]
        text_to_say += page.extract_text()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.say(text_to_say)
filename_to_save = asksaveasfilename() + '.mp3'
engine.save_to_file(text_to_say, filename_to_save)
engine.runAndWait()
