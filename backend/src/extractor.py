from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import utility



POPPLER_PATH = r'C:\poppler-24.08.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def extract(file_path, file_format):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''
    for page in pages:
        processed_image = utility.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text
    return document_text



    # if file_format == 'prescription':

    #     pass # Extract data from prescription
    # elif file_format == 'patient_details':
    #     pass # Extract data from patient details



if __name__ == '__main__':
    data = extract('../resources/patient_details/pd_1.pdf', 'prescription')
    print(data)