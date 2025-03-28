from backend.src.parser_generic import MedicalDocParser
import re

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_fields('patient_name'),
            'patient_address': self.get_fields('patient_address'),
            'medicines': self.get_fields('medicines'),
            'directions': self.get_fields('directions'),
            'refill': self.get_fields('refill'),
        }


    def get_fields(self, field_name):
        pattern_dict = {
            'patient_name': {'pattern': 'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': 'Address:[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:[^\n]*(.*)Refill', 'flags': re.DOTALL},
            'refill': {'pattern': 'Refill:(.*)times', 'flags': 0},
        }

        pattern_obj = pattern_dict.get(field_name)
        if pattern_obj:
            match = re.findall(pattern_obj['pattern'], self.text, flags=pattern_obj['flags'])
            if len(match) > 0:
                return match[0].strip()

    def get_name(self):
        pattern = 'Name:(.*)Date'
        match = re.findall(pattern, self.text)
        if len(match) > 0:
            return match[0].strip()
        

    def get_address(self):
        pattern = "Address:(.*)\n"
        match = re.findall(pattern, self.text)
        if len(match) > 0:
            return match[0].strip()
        

    def get_medicines(self):
        pattern = "Address:[^\n]*(.*)Directions"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(match) > 0:
            return match[0].strip()
        
    def get_directions(self):
        pattern = "Directions:[^\n]*(.*)Refill"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(match) > 0:
            return match[0].strip()
        

    def get_refill(self):
        pattern = "Refill:(.*)times"
        match = re.findall(pattern, self.text)
        if len(match) > 0:
            return match[0].strip()
        

if __name__ == '__main__':

    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC
Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month
Refill: 3 times
'''
    pp = PrescriptionParser(document_text)
    print(pp.parse())