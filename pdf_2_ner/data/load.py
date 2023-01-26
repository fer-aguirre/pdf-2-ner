import pdftotext

# Function to extract text from PDF file
def extract_text(path):
    # Read PDF file
    with open(path, "r") as f:
        pdf = pdftotext.PDF(f)
        pdf_text = ""
        # Iterate over all the pages
        for page in pdf:
            pdf_text += page
    return pdf_text