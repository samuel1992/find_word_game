from choose_word import choose_word


class Letter:
    def __init__(self, value, position):
        self.value = value
        self.position = position

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return self.value == other.value


class Word:
    def __init__(self, word):
        self.word = word
        self.letters = []

    def build(self):
        for position, letter in enumerate(self.word):
            self.letters.append(Letter(letter, position))

    def has(self, letter):
        letter_values = [l.value for l in self.letters]

        return letter.value in letter_values

    def same_position(self, letter):
        return self.letters[letter.position] == letter
