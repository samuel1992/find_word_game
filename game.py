from choose_word import choose_word

from word import Word


class Game:
    def __init__(self):
        self.has_letters = []
        self.has_not_letters = []
        self.has_at_different_position_letters = []

    def compare_words(self, word, guessed_word):
        for letter in guessed_word.letters:
            if word.has_at_same_position(letter):
                letter.set_to_correct()
                word.letters[letter.position].set_to_correct()
                self.has_letters.append(letter)

        for letter in filter(lambda x: not x.correct, guessed_word.letters):
            if word.has(letter):
                self.has_at_different_position_letters.append(letter)
            else:
                self.has_not_letters.append(letter)

    def found_word(self, word, guessed_word):
        return word.letters == guessed_word.letters

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
        print('==', ' '.join(guessed_word), '==')
        print('==', self.result_string(), '==')


def ask_for_word():
    while True:
        guessed_word = input('Guess a word.\n ==> ')
        if len(guessed_word) == 5:
            return guessed_word

        print('Your word must have 5 letters.')


def play_game():
    _word = choose_word().upper()
    word = Word(_word)
    for _ in range(5):
        _guessed_word = ask_for_word().upper()
        guessed_word = Word(_guessed_word)

        game = Game()
        game.compare_words(word, guessed_word)
        game.print_result(_guessed_word)

        if game.found_word(word, guessed_word):
            print('You have found the word', _word)

    print('The word was', _word)


if __name__ == '__main__':
    print("""This is a game where you have to guess a 5 letters word. Instructions:
        + = it has the letter in the same position
        | = it has the letter but in a different position
        - = doesn't have the letter""")

    play_game()
