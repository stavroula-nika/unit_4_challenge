from lib.music import music
import pytest

"""
Given a track (string), add_track()
Add the track to the playlist 
"""
def test_add_track_adds_track_to_playlist():
    my_music = music()
    my_music.add_track("Track1")
    assert my_music.playlist == ["Track1"]

"""
Given a track (non-string), add_track()
Raises an error -> "Input valid track!"
"""
def test_non_string_raises_error():
    my_music = music()
    with pytest.raises(Exception) as err:
        my_music.add_track(1234)
    assert str(err.value) == "Input valid track!"

"""
Given a track (empty string), add_track()
Raises an error -> "Input valid track!"
"""
def test_empty_string_raises_error():
    my_music = music()
    with pytest.raises(Exception) as err:
        my_music.add_track("")
    assert str(err.value) == "Input valid track!"

"""
Given multiple tracks (strings) have been added to the playlist, see_playlist()
Return the playlist (as a list)
"""
def test_see_playlist_returns_playlist():
    my_music = music()
    my_music.add_track("Track1")
    my_music.add_track("Track2")
    assert my_music.see_playlist() == ["Track1", "Track2"]

"""
Given no tracks (strings) have been added to the playlist, see_playlist()
Return empty playlist (as a list)
"""
def test_see_playlist_returns_empty_playlist():
    my_music = music()
    assert my_music.see_playlist() == []