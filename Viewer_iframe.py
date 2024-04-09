import streamlit as st
import base64

# Title for your app
st.title("PDF Viewer")

# Create a file uploader for users to upload PDFs
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert the uploaded PDF file to base64
    base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')
    # Embed the PDF in an iframe
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    # Display the PDF
    st.markdown(pdf_display, unsafe_allow_html=True)
