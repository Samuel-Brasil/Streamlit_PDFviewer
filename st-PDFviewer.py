import streamlit as st
import base64

def display_pdf(file):
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" style="border: none;"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Select a Supreme Court opinion", type="pdf")

if uploaded_file is not None:
    display_pdf(uploaded_file)
