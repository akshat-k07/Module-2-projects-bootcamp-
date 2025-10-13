from lib.music_library import MusicLibrary
from lib.track import Track

def test_track_initializes_with_title_and_artist():
    track = Track("Imagine", "John Lennon")
    assert track.title == "Imagine"
    assert track.artist == "John Lennon"

def test_track_format_returns_correct_string():
    track = Track("Imagine", "John Lennon")
    assert track.format() == "Imagine by John Lennon"

def test_music_library_initializes_with_empty_tracks():
    library = MusicLibrary()
    assert library.tracks == []

def test_music_library_adds_single_track():
    library = MusicLibrary()
    track = Track("Imagine", "John Lennon")
    library.add(track)
    assert library.tracks == [track]

def test_music_library_adds_multiple_tracks():
    library = MusicLibrary()
    track1 = Track("Imagine", "John Lennon")
    track2 = Track("Hey Jude", "The Beatles")
    library.add(track1)
    library.add(track2)
    assert library.tracks == [track1, track2]

def test_search_by_title_finds_matching_track():
    library = MusicLibrary()
    track = Track("Imagine", "John Lennon")
    library.add(track)
    result = library.search_by_title("Imagine")
    assert result == [track]

def test_search_by_title_is_case_insensitive():
    library = MusicLibrary()
    track = Track("Bohemian Rhapsody", "Queen")
    library.add(track)
    result = library.search_by_title("bohemian")
    assert result == [track]

def test_search_by_title_returns_multiple_matches():
    library = MusicLibrary()
    track1 = Track("Rhapsody in Blue", "George Gershwin")
    track2 = Track("Bohemian Rhapsody", "Queen")
    library.add(track1)
    library.add(track2)
    result = library.search_by_title("rhapsody")
    assert result == [track1, track2]

def test_search_by_title_returns_empty_list_if_no_match():
    library = MusicLibrary()
    track = Track("Imagine", "John Lennon")
    library.add(track)
    result = library.search_by_title("Yesterday")
    assert result == []
