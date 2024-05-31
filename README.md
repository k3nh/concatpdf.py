# concatpdf.py a PDF Concatenation Script

## Overview
This Python script provides a simple and convenient way to concatenate two PDF files: a resume and a cover letter. It combines these PDFs into a single output file, making it easier to share or submit as part of a job application. The script is designed to be user-friendly and offers a straightforward command-line interface.

## Requirements
- Python 3.x
- PyPDF2 library

You can install the required library using the following command:
```bash
pip install PyPDF2
```

## Usage
1. Place the script file (`concatpdf.py`) in the same directory as your PDF files.
2. Ensure that your PDF files are named according to the following convention:
   - `<name>_resume.pdf` (e.g., `John_Doe_resume.pdf`)
   - `<name>_cover.pdf` (e.g., `John_Doe_cover.pdf`)
3. Run the script using the Python interpreter:
   ```bash
   python concatpdf.py
   ```
4. When prompted, enter the desired name (e.g., "John_Doe"). If no input is provided, the default name ("John_Doe") will be used.
5. The script will check if the PDF files exist and then concatenate them. The output file will be named `<name>_cover_resume.pdf` (e.g., `John_Doe_cover_resume.pdf`).
6. A success message will be displayed, indicating the path to the concatenated PDF file.

## Example
Assuming you have the following PDF files:
- `John_Doe_resume.pdf`
- `John_Doe_cover.pdf`

Running the script with the input "John_Doe" will produce the output file `John_Doe_cover_resume.pdf` containing the concatenated resume and cover letter.

## Customization
You can easily customize the script to suit your specific requirements:
- Modify the `DEFAULT_NAME` variable to set a different default name.
- Adjust the file naming convention by changing the `<name>_resume.pdf` and `<name>_cover.pdf` patterns.
- Add error handling or additional functionality as needed to meet your specific use case.

## License
This script is provided under the MIT License. Feel free to use, modify, and distribute it according to the terms of the license.

Enjoy using the PDF concatenation script!
