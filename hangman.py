import numpy as np


def hangman(n_mistakes=5, words=None):
    if words is None:
        words = [
            'aluminium',
            'anaesthetist',
            'anonymous',
            'ethnicity',
            'facilitate',
            'february',
            'hereditary',
            'hospitable',
            'onomatopoeia',
            'particularly',
            'phenomenon',
            'philosophical',
            'prejudice',
            'prioritising',
            'pronunciation',
            'provocatively',
            'regularly',
            'remuneration',
            'statistics',
            'thesaurus'
        ]
    word = words[np.random.randint(len(words))]
    g_count = 0
    m_count = 0
    n = len(word)
    n_hit = len(set(word))
    guess = '*'*n
    while g_count < n_hit and m_count <= n_mistakes:
        letter = (input("Guess a letter: "))
        if letter in word:
            g_count += 1
            guess = ''.join([(guess[i], word[i])[word[i] == letter]
                             for i in range(n)])
            print 'Hit!'
            print 'The word: ', guess, '\n'
        elif m_count < n_mistakes:
            m_count += 1
            print 'Missed, mistake ', m_count, ' out of ', n_mistakes
            print 'The word: ', guess, '\n'
        else:
            m_count += 1
    if guess == word:
        return 'You won!'
    else:
        return 'You lost!'


if __name__ == '__main__':
    print hangman()
