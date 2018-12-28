import sys


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @classmethod
    def from_position(cls, position):
        """
        Given a number from 1 to 52, creates the card in the correct position assuming the deck
        is sorted by alphabetical suits and then in ace-high ranks.
        """
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        suit = suits[(position-1) // 13]
        rank = ranks[(position-1) % 13]
        return cls(rank, suit)

    def __repr__(self):
        return '{} of {}'.format(self.rank, self.suit)


def shuffle():
    num_cases = int(sys.stdin.readline())
    sys.stdin.readline()  # Skip blank line

    for case_num in range(num_cases):
        if case_num != 0:
            print()  # Blank line

        # Read input
        num_shuffles = int(sys.stdin.readline())

        # Read shuffles
        shuffles = []
        count = num_shuffles * 52
        while count:
            data = [int(i) for i in sys.stdin.readline().split()]
            count -= len(data)
            shuffles.extend(data)
        shuffles = [shuffles[x:x+52] for x in range(0, len(shuffles), 52)]  # Split into sets of 52

        result = list(range(1, 52+1))

        # Read shuffles to apply until we reach a blank line
        line = sys.stdin.readline()
        while not line.isspace() and line != '':
            shuffle = shuffles[int(line) - 1]

            # Apply the shuffle
            previous = result.copy()
            for i, new_position in enumerate(shuffle):
                result[i] = previous[new_position-1]
            line = sys.stdin.readline()

        # Print card names
        for idx in result:
            print(Card.from_position(idx))


shuffle()
