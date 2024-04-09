import streamlit as st
import base64
import requests
from pathlib import Path
from io import BytesIO


def load_pdf(source):
    """Load a PDF from various sources and return as a Base64 encoded string."""
    
    if isinstance(source, str) and source.startswith('http'):
        response = requests.get(source)
        response.raise_for_status()
        pdf_bytes = response.content
    elif isinstance(source, str) and Path(source).is_file():
        with open(source, 'rb') as file:
            pdf_bytes = file.read()
    elif isinstance(source, BytesIO):
        pdf_bytes = source.getvalue()
    else:
        raise ValueError("Invalid source type for PDF.")

    # Encode to Base64 and prepend MIME type
    base64_pdf = base64.b64encode(pdf_bytes).decode()
    full_base64_string = f'data:application/pdf;base64,{base64_pdf}'

    return full_base64_string

def pdf_reader(source, key=None):
    """Streamlit component to display a PDF from various sources."""
    
    if source is not None:
        # Encode the source to Base64
        base64_string = load_pdf(source)

        # Display PDF in the app using an iframe inside markdown
        st.markdown(f'<iframe src="{base64_string}" width="700" height="1000"></iframe>', unsafe_allow_html=True)

# Main app
st.title('PDF Viewer App')

source = st.file_uploader("Choose a PDF file:", type=['pdf'])
if source:
    pdf_reader(source)
