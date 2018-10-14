import hangman


def test_win(capsys):
    input_values = ['c', 'a', 'n', 't']

    def mock_input(s):
        return input_values.pop(0)

    hangman.input = mock_input
    answer = hangman.hangman(n_mistakes=1, words=['cat'])
    assert answer == 'You won!'


def test_lost(capsys):
    input_values = ['e', 'n']

    def mock_input(s):
        return input_values.pop(0)

    hangman.input = mock_input
    answer = hangman.hangman(n_mistakes=1, words=['cat'])

    assert answer == 'You lost!'
