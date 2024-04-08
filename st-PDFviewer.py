import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

pdf_file = st.file_uploader("Upload PDF file", type=('pdf'))

if pdf_file:
    binary_data = pdf_file.getvalue()
    pdf_viewer(input=binary_data,
               width=700)

