from lib.design_and_test_drive_a_single_class import DiaryEntry

def test_format_returns_formatted_entry():
    entry = DiaryEntry("Holiday", "I went to the beach.")
    assert entry.format() == "Holiday: I went to the beach."

def test_format_with_empty_contents():
    entry = DiaryEntry("Silent Day", "")
    assert entry.format() == "Silent Day: "

def test_count_words_regular_entry():
    entry = DiaryEntry("Trip", "I visited the mountains and the lake.")
    assert entry.count_words() == 7

def test_count_words_empty_contents():
    entry = DiaryEntry("Blank", "")
    assert entry.count_words() == 0

def test_count_words_single_word():
    entry = DiaryEntry("One", "Hello")
    assert entry.count_words() == 1

def test_reading_time_exact_division():
    entry = DiaryEntry("Read", "one two three four five six")
    assert entry.reading_time(2) == 3  # 6 words / 2 wpm

def test_reading_time_rounds_up():
    entry = DiaryEntry("Read", "one two three")
    assert entry.reading_time(2) == 2  # 3 words / 2 wpm = 1.5 -> rounds up to 2

def test_reading_time_high_wpm():
    entry = DiaryEntry("Fast", "word " * 10)
    assert entry.reading_time(100) == 1  # Less than 1 min -> round up

def test_reading_time_zero_wpm_raises():
    entry = DiaryEntry("Bad", "Some text here")
    try:
        entry.reading_time(0)
        assert False, "Should raise ZeroDivisionError or ValueError"
    except (ZeroDivisionError, ValueError):
        assert True

def test_reading_chunk_returns_correct_first_chunk():
    entry = DiaryEntry("Read", "one two three four five six seven eight nine ten")
    assert entry.reading_chunk(2, 2) == "one two three four"

def test_reading_chunk_returns_next_chunk_on_second_call():
    entry = DiaryEntry("Read", "one two three four five six seven eight")
    entry.reading_chunk(2, 1)  # Reads: one two
    assert entry.reading_chunk(2, 1) == "three four"

def test_reading_chunk_wraps_around_after_full_read():
    entry = DiaryEntry("Loop", "one two three")
    entry.reading_chunk(1, 1)  # one
    entry.reading_chunk(1, 1)  # two
    entry.reading_chunk(1, 1)  # three
    assert entry.reading_chunk(1, 1) == "one"

def test_reading_chunk_large_minutes_exceeds_text():
    entry = DiaryEntry("Long", "one two three")
    assert entry.reading_chunk(10, 1) == "one two three"

def test_reading_chunk_with_exactly_enough_words():
    entry = DiaryEntry("Exact", "one two three four")
    entry.reading_chunk(2, 1)  # two words
    assert entry.reading_chunk(2, 1) == "three four"

def test_reading_chunk_handles_empty_contents():
    entry = DiaryEntry("Empty", "")
    assert entry.reading_chunk(5, 1) == ""
