from dataclasses import dataclass

from choose_word import choose_word


@dataclass
class Letter:
    value: str
    position: int


class Word:
    def __init__(self, word):
        assert word

        self.letters = [Letter(value=letter, position=position)
                        for position, letter in enumerate(word)]

    def has(self, letter):
        letter_values = [l.value for l in self.letters]

        return letter.value in letter_values

    def same_position(self, letter):
        return self.letters[letter.position] == letter


class Game:
    @staticmethod
    def play():
        chosen_word = Word('GENIO')
        word = Word('GORDO')

        for letter in word.letters:
            if chosen_word.has(letter):
                print("has the letter", letter.value)

            if chosen_word.same_position(letter):
                print("has letter in same position", letter.value)

Game().play()
