from lib.track import Track
from lib.music_library import MusicLibrary
from unittest.mock import Mock as mock

def test_track_initializes_with_title_and_artist():
    track = Track("Imagine", "John Lennon")
    assert track.title == "Imagine"
    assert track.artist == "John Lennon"

def test_track_format_returns_correct_string():
    track = Track("Imagine", "John Lennon")
    assert track.format() == "Imagine by John Lennon"


def test_music_library_adds_mock_track():
    lib = MusicLibrary()
    mock_track = mock()
    lib.add(mock_track)
    assert lib.tracks == [mock_track]

def test_search_by_title_returns_matching_mock_tracks():
    lib = MusicLibrary()

    mock1 = mock()
    mock1.title = "Love Story"

    mock2 = mock()
    mock2.title = "Hate Song"

    mock3 = mock()
    mock3.title = "Story of My Life"

    lib.add(mock1)
    lib.add(mock2)
    lib.add(mock3)

    results = lib.search_by_title("story")
    assert results == [mock1, mock3]

def test_search_by_title_case_insensitive_with_mock():
    lib = MusicLibrary()
    mock_track = mock()
    mock_track.title = "Bohemian Rhapsody"
    lib.add(mock_track)

    results = lib.search_by_title("bohemian")
    assert results == [mock_track]

def test_search_by_title_returns_empty_with_mock():
    lib = MusicLibrary()
    mock_track = mock()
    mock_track.title = "Hello"
    lib.add(mock_track)

    results = lib.search_by_title("Goodbye")
    assert results == []


def test_add_and_search_tracks_integration():
    lib = MusicLibrary()
    t1 = Track("Yellow Submarine", "The Beatles")
    t2 = Track("Submarine Life", "Ocean Sounds")
    t3 = Track("Let It Be", "The Beatles")

    lib.add(t1)
    lib.add(t2)
    lib.add(t3)

    results = lib.search_by_title("submarine")
    assert results == [t1, t2]

def test_format_method_with_search_results_integration():
    lib = MusicLibrary()
    t1 = Track("Fix You", "Coldplay")
    t2 = Track("Fix It", "Ryan Adams")
    t3 = Track("Yellow", "Coldplay")

    lib.add(t1)
    lib.add(t2)
    lib.add(t3)

    results = lib.search_by_title("fix")
    formatted = [track.format() for track in results]

    assert formatted == ["Fix You by Coldplay", "Fix It by Ryan Adams"]
