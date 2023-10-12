MAX_LINES = 3 # all capitals for constants
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("How much would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and" + str(MAX_LINES) + ".")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Please enter a number between " + str(MIN_BET) + " and " + str(MAX_BET) + ".")
        else:
            print("Please enter a number.")
    
    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(balance,lines,bet)

main()