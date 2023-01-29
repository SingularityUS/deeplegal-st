import pandas as pd
import io
#from google.colab import files
import PyPDF2
import docx2txt
import re
import streamlit as st


def process_file(file_path):
    """Extract text, file name, and page number from file_path.

    Args:
        file_path: string, the file path to the document.

    Returns:
        text: string, the extracted text from the document.
        file_path: string, the file path to the document.
        page_number: int, the page number of the document.
    """
    file_extension = file_path.split(".")[-1]
    if file_extension == "pdf":
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_number in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_number].extract_text()
        pdf_file.close()
    else:
        raise Exception("Unsupported file format")
    return text, file_path, page_number
'''
def convert_to_dataframe(file_paths, usernames):
    """Convert a list of file paths to a Pandas dataframe.

    Args:
        file_paths: list, a list of file paths to the documents.

    Returns:
        df: pandas dataframe, a dataframe with the extracted text, file name,
            page number, and username.
    """
    data = []
    for file_path, username in zip(file_paths, usernames):
        text, file_path, page_number = process_file(file_path)
        data.append([text, file_path, page_number, username])
    df = pd.DataFrame(data, columns=["Text", "File Path", "Page Number", "Username"])
    return df
'''
def convert_to_dataframe(file_paths):
    rows = []
    for file_path in file_paths:
        text, file_name, page_number = process_file(file_path)
        rows.append([text, file_name, page_number])
    return pd.DataFrame(rows, columns=["Text", "Document Name", "Page Number", "Username"])

# Add a file uploader widget


#uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

if uploaded_files:
    # Get the file name
    file_name = uploaded_file.name
    file_paths = [uploaded_file]
    df = convert_to_dataframe(file_paths)
    st.write("Text: ", df["Text"])
    st.write("Document Name: ", df["Document Name"])
    st.write("Page Number: ", df["Page Number"])
    
    
def main():
    uploaded_files = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
    file_paths = list(uploaded_files.keys())
    df = convert_to_dataframe(file_paths)
    print(df)
    
username = st.text_input("Enter your username: ")
'''
if uploaded_file:
    file_name = uploaded_file.name
    file_paths = [uploaded_file]
    df = convert_to_dataframe(file_paths)
    df["Username"] = username
    st.write("Text: ", df["Text"])
    st.write("Document Name: ", df["Document Name"])
    st.write("Page Number: ", df["Page Number"])
    st.write("Username: ", df["Username"])
'''
if __name__ == '__main__':
    main()
