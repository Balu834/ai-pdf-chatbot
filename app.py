import os
os.environ["STREAMLIT_SERVER_WATCH_FILE_SYSTEM"] = "false"
from pypdf import PdfReader

pdf_file = input("Enter PDF file name: ")
try:
    reader = PdfReader(pdf_file)
except FileNotFoundError:
    print("File not found. Please check the name.")
    exit()
except Exception as e:
    print("Error reading PDF:", e)
    exit() 
print("Total pages:", len(reader.pages))

text = ""

for page in reader.pages:
    text += page.extract_text()
print("Total characters:", len(text))

print(text[:500])
