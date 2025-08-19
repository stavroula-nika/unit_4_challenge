# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class music_music_:

    def __init__(self):
        # List of strings: self.playlist

    def add_track(self, track):
        # Parameters:
            # track: string
        # Side effect: 
            # Adds 'track' to playlist (list of strings)
        # Return: nothing

    def see_playlist(self):
        # Parameters:
            None
        # Side effects:
            None
        # Return:
            # Playlist (list of strings)
    

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

# """
# Given a track (string), add_track()
# Add the track to the playlist 
# """
# my_music = music()
# my_music.add_track("Track1")
# my_music.playlist => ["Track1"]

# """
# Given a track (non-string), add_track()
# Raises an error -> "Input valid track!"
# """
# my_music = music()
# my_music.add_track(12345) => error

# """
# Given a track (empty string), add_track()
# Raises an error -> "Input valid track!"
# """
# my_music = music()
# my_music.add_track("") => error

"""
Given multiple tracks (string) have been added to the playlist, see_playlist()
Return the playlist (as a list)
"""
my_music = music()
my_music.add_track("Track1")
my_music.add_track("Track2")
my_music.see_playlist => ["Track1", "Track2"]




```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
