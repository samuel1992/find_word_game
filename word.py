from dataclasses import dataclass


@dataclass
class Letter:
    value: str
    position: int


class Word:
    def __init__(self, word):
        assert len(word) == 5

        self.letters = [Letter(value=letter, position=position)
                        for position, letter in enumerate(word)]

    def has(self, letter):
        return letter.value in ''.join(i.value for i in self.letters)

    def has_at_same_position(self, letter):
        return letter in self.letters
