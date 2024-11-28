import random
def initialize_deck():
    suits = ['H', 'S', 'D', 'C']
    cards = ['A', '2', '3', '4', '5', '6', '7', 
             '8', '9', '10', 'J', 'Q', 'K']
    
    deck = [card for card in cards
                for suit in suits]
    
    random.shuffle(deck)
    
    return deck

def deal(deck):
    dealer = [deck.pop(), deck.pop()]
    player = [deck.pop(), deck.pop()]

    return (dealer, player)

def hit(deck, cards):
    cards.append(deck.pop())

def stay():
    pass

def display_cards(dealer, player):
    print(f"Dealer: {dealer[0]}")
    print(f"Player: {', '.join(player)}")

def prompt_player():
    choice = input("Hit or stay?\n").lower()

    while choice[0] not in 'hs':
        print("Invalid choice.")
        choice = input("Hit or stay?\n").lower()

    return choice

def get_score(cards):
    total = 0

    for card in cards:
        if card in 'AJQK':
            if card == 'A':
                total += 11
            else:
                total += 10
        else:
            total += int(card)

    for card in cards:
        if total <= 21:
            break
        elif card == 'A':
            total -= 10

    return total

def bust(cards):
    if get_score(cards) > 21:
        return True
    
    return False

deck = initialize_deck()
dealer_cards, player_cards = deal(deck)
display_cards(dealer_cards, player_cards)
print(f"Player score: {get_score(player_cards)}")


while prompt_player()[0] == 'h':
    hit(deck, player_cards)
    display_cards(dealer_cards, player_cards)
    print(f"Player score: {get_score(player_cards)}")

    if bust(player_cards):
        print("Bust!")
        break

if bust(player_cards):
    print('Dealer wins!')
else:
    while get_score(dealer_cards) <= 17:
        hit(deck, dealer_cards)
        display_cards(dealer_cards, player_cards)
        print(f"Player score: {get_score(player_cards)}")
        print(f"Dealer score: {get_score(dealer_cards)}")

display_cards(dealer_cards, player_cards)
print(f"Player score: {get_score(player_cards)}")
print(f"Dealer score: {get_score(dealer_cards)}")

if bust(dealer_cards):
    print("Dealer bust.")
    print("Player wins!")
else:
    if get_score(player_cards) > get_score(dealer_cards):
        print("Player wins!")
    elif get_score(player_cards) < get_score(dealer_cards):
        print("Dealer wins!")
    else:
        print("Push.")