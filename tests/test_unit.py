import pytest
from alphabetconverter.main import Converter

@pytest.fixture
def input_data():
    #Good case
    string1 = "I am converting this sentence to uppercase."
    string2 = "I AM CONVERTING THIS SENTENCE TO LOWERCASE."

    #Bad Case
    string3 = "13@#%@*%@%^"
    return [string1,string2,string3]


def test_string_checker(input_data):
    pass_converter = Converter(input_data[0])
    fail_converter = Converter(input_data[2])

    #Pass Case : returns True
    assert pass_converter.string_checker()==True

    #Fail Case : this function returns False
    assert fail_converter.string_checker()== False

def test_to_uppercase(input_data):
    pass_converter_to_uppercase =Converter(input_data[0])
    fail_converter_to_anycase =Converter(input_data[2])
    #Pass Case
    assert pass_converter_to_uppercase.to_upper_case()== input_data[0].upper()

    #Fail Case
    assert fail_converter_to_anycase.to_upper_case() == "Should contain at least one alphabet character"

def test_to_lowercase(input_data):
    pass_converter_to_lowercase =Converter(input_data[1])
    fail_converter_to_anycase =Converter(input_data[2])
    #Pass Case
    assert pass_converter_to_lowercase.to_lower_case()== input_data[1].lower()

    #Fail Case
    assert fail_converter_to_anycase.to_lower_case() == "Should contain at least one alphabet character"