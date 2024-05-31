import os
import sys
from PyPDF2 import PdfMerger

DEFAULT_NAME = "Ken Hunt"

def check_file_exists(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        sys.exit(1)

def concatenate_pdfs(name):
    resume_file = None
    cover_file = None

    for file in os.listdir("."):
        if "resume" in file.lower() and file.endswith(".pdf"):
            resume_file = file
        elif "cover" in file.lower() and file.endswith(".pdf"):
            cover_file = file

    if not resume_file:
        print("Error: No file named 'resume' found.")
        sys.exit(1)

    if not cover_file:
        print("Error: No file named 'cover' found.")
        sys.exit(1)

    check_file_exists(resume_file)
    check_file_exists(cover_file)

    merger = PdfMerger()
    with open(resume_file, "rb") as resume, open(cover_file, "rb") as cover:
        merger.append(resume)
        merger.append(cover)

    output_file = f"{name}-cover-resume.pdf"
    with open(output_file, "wb") as output:
        merger.write(output)

    print(f"PDFs concatenated successfully! Output file: {output_file}")

def main():
    name = input(f"Enter name (default is {DEFAULT_NAME}): ") or DEFAULT_NAME
    concatenate_pdfs(name)

if __name__ == "__main__":
    main()
