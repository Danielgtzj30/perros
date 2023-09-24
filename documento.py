with st.sidebar:
    authenticator.logout("Logout", "sidebar")
    st.title("Libretas")
uploaded_file = st.file_uploader("Choose a file")
with pdfplumber.open(uploaded_file) as pdf:
    text = ''
    for page in pdf.pages:
        text += page.extract_text()

    st.write(text)