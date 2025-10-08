import pytest
from lib.present import Present

def test_wrap():
    items = "book"
    x = Present()
    x.wrap(items)
    with pytest.raises(Exception) as info:
        x.wrap("Toy")

    assert str(info.value) == "A contents has already been wrapped."

def test_wrap_further():
    items = "book"
    x = Present()
    x.wrap(items)
    assert x.contents == items

def test_unwrap():
    x = Present()
    with pytest.raises(Exception) as info:
        x.unwrap()
    
    assert str(info.value) == "No contents have been wrapped."

def test_unwrap_further():
    items = "book"
    x = Present()
    x.wrap(items)
    x.unwrap()
    assert x.contents == items