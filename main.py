import random



def deal_card(list_cards):
    chosen_card = random.choice(list_cards)
    return chosen_card


def calculate_score(list_cards):
    score = sum(list_cards)
    if score == 21 and len(list_cards) == 2:
        return 0
    if 11 in list_cards and score > 21:
        list_cards.remove(11)
        list_cards.append(1)
        score = sum(list_cards)
    return score


def compare(final_user_score, final_computer_score):
    if final_user_score == final_computer_score:
        return "Draw"
    elif final_computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif final_user_score == 0:
        return "Win with a Blackjack"
    elif final_user_score > 21:
        return "You went over. You lose"
    elif final_computer_score > 21:
        return "Opponent went over. You lose"
    elif final_user_score > final_computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_card = []
    for i in range(0,2):
        user_cards.append(deal_card(card))
        computer_card.append(deal_card(card))
    isGameOver = False
    while not isGameOver:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_card)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isGameOver = True
            print("Game over")

        else:
            should_continue = input("Do you want to draw another card? 'y' or 'n': ").lower()
            if should_continue == 'y':
                user_cards.append(deal_card(card))
            else:
                isGameOver = True
                print("Game over")
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card(card))
        computer_score = calculate_score(computer_card)

    print(f"   Your final hand: {user_cards}, final_score: {user_score}")
    print(f"   Computer's hand: {computer_card}, final_score: {computer_score}")

    print(compare(user_score, computer_score))


if __name__ == '__main__':
    while input("Do you want to play a game of blackjack? Type 'y' or 'n'").lower() == "y":
        play_game()
    
