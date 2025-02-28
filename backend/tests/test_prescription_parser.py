from backend.src.parser_prescription import PrescriptionParser


def test_get_name():
    pp = PrescriptionParser(document_text)
    assert pp.get_fields('patient_name') =='Marta Sharapova'

def test_get_address():
    pp = PrescriptionParser(document_text)
    assert pp.get_fields('patient_address') == '9 tennis court, new Russia, DC'

def test_get_medicines():
    pp = PrescriptionParser(document_text)
    assert pp.get_fields('medicines') == 'Prednisone 20 mg\nLialda 2.4 gram'

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