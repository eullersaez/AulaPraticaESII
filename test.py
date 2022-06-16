import main

def test_convert_inches_to_centimeters():
    assert main.convert_inches_to_centimeters(1) == 2.54
    assert main.convert_inches_to_centimeters(0.5) == 1.27
    assert main.convert_inches_to_centimeters(3.5) == 8.89

def test_convert_centimeters_to_inches():
    assert main.convert_centimeters_to_inches(1) == 0.39
    assert main.convert_centimeters_to_inches(0.5) == 0.2
    assert main.convert_centimeters_to_inches(3.5) == 1.38

def test_convert_kilometers_to_miles():
    assert main.convert_kilometers_to_miles(1) == 0.62
    assert main.convert_kilometers_to_miles(0.5) == 0.31
    assert main.convert_kilometers_to_miles(3.5) == 2.18

def convert_miles_to_kilometers():
    assert main.convert_miles_to_kilometers(1) == 1.61
    assert main.convert_miles_to_kilometers(0.5) == 0.8
    assert main.convert_miles_to_kilometers(3.5) == 5.63