from streamlit_pdf_reader import pdf_reader

if st.button('Say hello'):
    st.write('Why hello there')
    source3=st.file_uploader("Choose a pdf file:")
    pdf_reader(source3)
else:
    st.write('Goodbye')
