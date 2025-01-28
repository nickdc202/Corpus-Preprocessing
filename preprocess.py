import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os

# Define the path to the PDF folder
pdf_folder = 'pdfs'

# Define the path to the output folder
output_folder = 'preprocessed'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Loop through all PDF files in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        # Open the PDF file
        pdf_file = open(os.path.join(pdf_folder, filename), 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Extract the text from the PDF file
        text = ''
        for page in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page).extractText()

        # Tokenize the text
        tokens = word_tokenize(text)

        # Lemmatize the tokens
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

        # Save the preprocessed text to a new file
        output_filename = filename.replace('.pdf', '.txt')
        output_file = open(os.path.join(output_folder, output_filename), 'w')
        output_file.write(' '.join(lemmatized_tokens))
        output_file.close()

        # Close the PDF file
        pdf_file.close()
