from lib.report_length import report_length

def test_report_length():
    string = "Banana"
    result = report_length(string)
    expected = "This string was " + str(len(string)) + " characters long."
    assert result == expected
