"""utils"""
def validate(hand):
    """validating input"""
    if hand < 0 or hand > 2:
        return False
    return True


def print_hand(hand, name):
    """output user input for chosen hand"""
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])


def judge(player, computer):
    """judge who wins the game"""
    if player == computer:
        return 'Draw'
    if player == 0 and computer == 1:
        return 'Lose'
    if player == 1 and computer == 2:
        return 'Lose'
    if player == 2 and computer == 0:
        return 'Lose'
    return 'Win'
