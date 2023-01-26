# Import libraries
import pdftotext
import re
import stanza 
import pandas as pd
import streamlit as st
from collections import OrderedDict
import pdf_2_ner.data.load as load

# Download Spanish models
stanza.download('es')


# Set streamlit app title
st.title('PDF 2 NER')

# Upload a 'csv' or 'excel' file
uploaded_file = st.file_uploader("Load PDF to analyze", type=['pdf'], accept_multiple_files=False, key=None, on_change=None, disabled=False,
                                help="Please enter a valid format: \n- PDF")

# If there's an uploaded file
if uploaded_file:
    # Match file extension
    if uploaded_file.name.rsplit('.', 1)[1] == 'pdf':
        # Apply extract_text function to read PDF document
        path = uploaded_file.read()
        pdf_text = load.extract_text(path)
        st.write(pdf_text)