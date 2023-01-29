import pandas as pd
import io
from google.colab import files
import PyPDF2
import docx2txt
import re

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

def main():
    uploaded_files = files.upload()
    file_paths = list(uploaded_files.keys())
    df = convert_to_dataframe(file_paths)
    print(df)

if __name__ == '__main__':
    main()
