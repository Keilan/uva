import sys


rank_map = {
    'A': 'Ace',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'T': '10',
    'J': 'Jack',
    'Q': 'Queen',
    'K': 'King'
}


suit_map = {
    'S': 'Spades',
    'H': 'Hearts',
    'D': 'Diamonds',
    'C': 'Clubs'
}


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return '{} of {}'.format(self.rank, self.suit)


def bridge():
    for line in sys.stdin.readlines():
        # Build hand
        hand = []
        for card in line.split():
            hand.append(Card(rank_map[card[0]], suit_map[card[1]]))

        # Evaluate Score
        points = 0
        suit_counts = {suit: 0 for suit in suit_map.values()}

        # Rule 1
        for card in hand:
            if card.rank == 'Ace':
                points += 4
            elif card.rank == 'King':
                points += 3
            elif card.rank == 'Queen':
                points += 2
            elif card.rank == 'Jack':
                points += 1

            suit_counts[card.suit] += 1

        # Rules 2-4
        for card in hand:
            if card.rank == 'King' and suit_counts[card.suit] == 1:
                points -= 1
            elif card.rank == 'Queen' and suit_counts[card.suit] <= 2:
                points -= 1
            elif card.rank == 'Jack' and suit_counts[card.suit] <= 3:
                points -= 1

        no_trump_points = points

        # Rule 5-7
        for suit, count in suit_counts.items():
            if count == 2:
                points += 1
            elif count == 1:
                points += 2
            elif count == 0:
                points += 2

        # Check if stopped
        stopped = set()
        for card in hand:
            if card.rank == 'Ace':
                stopped.add(card.suit)
            elif card.rank == 'King' and suit_counts[card.suit] > 1:
                stopped.add(card.suit)
            elif card.rank == 'Queen' and suit_counts[card.suit] > 2:
                stopped.add(card.suit)

        # Output result
        if points < 14:
            print('PASS')
        elif no_trump_points >= 16 and len(stopped) == 4:
            print('BID NO-TRUMP')
        else:
            suits = [s for s, v in suit_counts.items() if v == max(suit_counts.values())]
            selected = sorted(suits)[-1]  # Pick reverse alphabetically
            print('BID {}'.format(selected[0]))


bridge()