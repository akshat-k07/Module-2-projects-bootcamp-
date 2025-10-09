from lib.diary import make_snippet

def test_small_snippet():
    text = "Hey all!"
    result = make_snippet(text)
    assert result == text

def test_large_snippet():
    text = "Hey I am really interested in football"
    result = make_snippet(text)
    assert result == "Hey I am really interested ..."

def test_empty_snippet():
    text = ""
    result = make_snippet(text)
    assert result == "Text cannot be empty"