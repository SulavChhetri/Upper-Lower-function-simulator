
from alphabetconverter.main import Converter

#Good case
string1 = "I am converting this sentence to uppercase."
string2 = "I AM CONVERTING THIS SENTENCE TO LOWERCASE."

#Bad Case
string3 = "13@#%@*%@%^"

def test_string_checker():
    pass_converter = Converter(string1)
    fail_converter = Converter(string3)

    #Pass Case : returns True
    assert pass_converter.string_checker()==True

    #Fail Case : this function returns False
    assert fail_converter.string_checker()== False

def test_to_uppercase():
    pass_converter_to_uppercase =Converter(string1)
    fail_converter_to_anycase =Converter(string3)
    #Pass Case
    assert pass_converter_to_uppercase.to_upper_case()== string1.upper()

    #Fail Case
    assert fail_converter_to_anycase.to_upper_case() == "Should contain at least one alphabet character"

def test_to_lowercase():
    pass_converter_to_lowercase =Converter(string2)
    fail_converter_to_anycase =Converter(string3)
    #Pass Case
    assert pass_converter_to_lowercase.to_lower_case()== string2.lower()

    #Fail Case
    assert fail_converter_to_anycase.to_lower_case() == "Should contain at least one alphabet character"

def test_smiley_function():
    pass_converter = Converter(string1)
    fail_converter = Converter(string3)
    #Pass Case :
    assert pass_converter.smiley_function() ==string1+' Smiley Added!!'

    #Fail Case:
    assert fail_converter.smiley_function() == "Should contain at least one alphabet character"


def test_natural_return():
    converter = Converter(string1)
    assert converter.natural_return() == string1

if __name__ == "__main__":
    test_string_checker()
    test_to_uppercase()
    test_to_lowercase()
    test_smiley_function()
    test_natural_return()