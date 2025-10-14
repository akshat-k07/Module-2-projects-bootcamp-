from unittest.mock import Mock as mock
import pytest

# Delete the lines starting with `@pytest.mark.skip` one by one as you work through.

def test_set_up_blank_mock():
    # Uncomment and set up your mocks here
    fake_object = mock()

    # Don't edit below
    assert fake_object is not None


def test_set_up_mock_with_methods():
    # Uncomment and set up your mocks here
    fake_object = mock()
    fake_object.speak.return_value = "Meow, Jess"
    fake_object.count_ears.return_value = 2
    fake_object.count_legs.return_value = 4

    # Don't edit below
    assert fake_object.speak("Jess") == "Meow, Jess"
    assert fake_object.count_ears() == 2
    assert fake_object.count_legs() == 4


def test_assert_that_mock_was_called():
    fake_object = mock()

    # Don't edit this next line
    fake_object.speak.return_value = "Meow, Steve"
    fake_object.speak("Steve")

    assert fake_object.speak("Steve") == "Meow, Steve"


@pytest.mark.skip(reason="not yet implemented")
def test_creates_mock_for_specific_case():
    fake_diary = mock()
    fake_diary.count_entries.return_value = 2

    # Don't edit below
    fake_diary.add(mock())
    fake_diary.add(mock())
    assert fake_diary.count_entries() == 2

