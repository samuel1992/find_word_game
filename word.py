from dataclasses import dataclass

from unidecode import unidecode


@dataclass
class Letter:
    value: str
    position: int

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        value = unidecode(other.value)
        position = other.position
        return value == unidecode(self.value) and position == self.position


class Word:
    def __init__(self, word):
        assert len(word) == 5

        self.letters = [Letter(value=letter, position=position)
                        for position, letter in enumerate(word)]

    def has(self, letter):
        value = unidecode(letter.value)
        return value in ''.join(unidecode(i.value) for i in self.letters)

    def has_at_same_position(self, letter):
        return letter in self.letters
