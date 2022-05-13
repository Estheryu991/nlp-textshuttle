#!/usr/bin/env python3

from pathlib import Path


class Corpus:

    def __init__(self, path: Path):
        """
        Load segments from a file, one per line.
        """
        with path.open(encoding='utf-8') as corpus:
            self.segments = [s.strip('\n') for s in corpus]

    def filter(self, min_alpha: float = 0.5):
        """
        Discard all segments with too few alphabetical characters.

        Keep only segments where at least `min_alpha` of the
        characters are alphabetic.

        Examples for min_alpha == 0.5:
            "So."      # keep
            "¡Sí!"     # keep
            "Ja!!!"    # discard
            "123.5"    # discard
        """
        pass  # TODO: Task 1

    def normalize(self):
        """
        Replace fancy quotes like « » „ “ ” with ASCII quotes (").
        """
        pass  # TODO: Task 1

    def split(self, language: str = 'en'):
        """
        Split up segments containing multiple sentences using an online API.
        Remove any leading and trailing whitespace.

        Example:
            Before: self.segments = ["Wie geht's?", "Ausgezeichnet. Und dir?"]
            After:  self.segments = ["Wie geht's?", "Ausgezeichnet.", "Und dir?"]
        """
        pass  # TODO: Task 2


# TODO: Task 3
