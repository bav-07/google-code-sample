"""A video playlist class."""

from typing import Sequence

class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name: str):
        self._name = name
        self._videos = []

    def x(self, videos):
        self._videos = videos

    def __del___(self):
        return

    @property
    def name(self) -> str:
        """Returns the title of a video."""
        return self._name

    @property
    def videos(self) -> Sequence[str]:
        """Returns the list of video."""
        return self._videos