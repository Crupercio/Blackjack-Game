
import  art
import  random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(_cards):
    """Take a list of cards and returned calculated score"""
    if sum(_cards) == 21 and len(_cards) == 2:
        return 0
    if 11 in _cards and sum(_cards) > 21:
        _cards.remove(11)
        _cards.append(1)
    return sum(_cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw !"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack"
    elif user_score > 21:
        return "You went over. You Lose"
    elif computer_score > 21:
        return "Opponent went over. You Win!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"

def play_game():
    print(art.logo)
    player_hand = []
    dealer_hand = []
    dealer_score = -1
    player_score = -1

    is_game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"\t You cards: {player_hand}, current score: {player_score}\n\tComputer's first card: {dealer_hand[0]}")
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            new_card = input(f"Type 'y' to get another card, type 'n' to pass: ")
            if new_card == "y":
                player_hand.append(deal_card())
            else:
                is_game_over = True

    player_score = calculate_score(player_hand)
    if player_score > 21:
        player_over = True
    else:
       while dealer_score != 0 and dealer_score < 17 and player_score != 0:
            dealer_hand.append(deal_card())
            dealer_score = calculate_score(dealer_hand)

    print(f"  Your final hand: {player_hand}, final score: {player_score}")
    print(f"  Computer's final hand: {dealer_hand}, final score {dealer_score}")
    print(compare(player_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
