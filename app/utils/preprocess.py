import os
import re
from PyPDF2 import PdfReader

def extract_text_from_pdfs(data_dir):
    '''
    Helper function to extract text from pdf files in a directory
    '''
    texts = []
    for file in os.listdir(data_dir):
        if file.endswith('.pdf'):
            reader = PdfReader(os.path.join(data_dir, file))
            text = "".join(page.extract_text() for page in reader.pages)
            texts.append(text)
    
    return texts

def clean_text(text):
    '''
    Helper function to clean text
    '''
    text = re.sub(r'\s+', ' ', text)   # Removing extra spaces
    return text.strip()

def chunk_text(text, chunk_size=1000):
    '''
    Helper function to chunk text into smaller parts
    '''
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]