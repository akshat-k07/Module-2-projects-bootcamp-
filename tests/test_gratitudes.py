from lib.gratitudes import Gratitudes

def test_add():
    items = []
    x = Gratitudes()
    x.add("Hello, hope you are well")
    assert x.gratitudes == ["Hello, hope you are well"]

def test_format():
    items = ["Hello, hope you are well"]
    x = Gratitudes()
    x.add("Hello, hope you are well")
    result = x.format()
    assert result == "Be grateful for: Hello, hope you are well"
