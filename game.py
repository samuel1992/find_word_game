from dataclasses import dataclass

from choose_word import choose_word


@dataclass
class Letter:
    value: str
    position: int


class Word:
    def __init__(self, word):
        assert len(word) == 5

        self.letters = [Letter(value=letter, position=position)
                        for position, letter in enumerate(word)]

    def has_at_same_position(self, letter):
        return letter in self.letters

    def has_at_different_position(self, letter):
        return letter.value in ''.join(i.value for i in self.letters)


class Game:
    def __init__(self):
        self.has_letters = []
        self.has_not_letters = []
        self.has_at_different_position_letters = []

    def compare_words(self, word, guessed_word):
        for letter in guessed_word.letters:
            if word.has_at_same_position(letter):
                word.letters.remove(letter)
                self.has_letters.append(letter)
            elif word.has_at_different_position(letter):
                self.has_at_different_position_letters.append(letter)
            else:
                self.has_not_letters.append(letter)

    def result_string(self):
        string = list(range(5))

        for letter in self.has_letters:
            string[letter.position] = '+'

        for letter in self.has_not_letters:
            string[letter.position] = '-'

        for letter in self.has_at_different_position_letters:
            string[letter.position] = '|'

        return ' '.join(string)

    def print_result(self, guessed_word):
        print('==', ' '.join(i.value for i in guessed_word.letters), '==')
        print('==', self.result_string(), '==')
