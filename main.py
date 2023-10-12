import random

print('''Welcome to the SLOT MACHINE simulator!
This is a simple slot machine. You will be asked to deposit some amount of $.
Anytime you want to stop playing, just hit "q"
Don't get bankdrupt!
Now play ><
''')

# Limits for input
MAX_LINES = 3 # all capitals for constants
MAX_BET = 100
MIN_BET = 1

# Matrix 
ROWS = 3
COLS = 3

# Symbols Dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

# Get a random list of columns of symbols.
def get_slot_machine_spin(cols, rows, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):            # 2 for loops to generate twice. 2 columns, 3 rows, then rotate to make 3 lines.
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Display the symbols in columns x rows format.
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Get how much money play wants to deposit.
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

# Get how many lines player wants to bet on.
def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a number.")
    
    return lines

# Get how much money player wants to bet on each line.
def get_bet():
    while True:
        bet = input("How much would you like to bet on each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a number between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    
    return bet

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough money to bet that amount. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.")   

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        ans = input("Press enter to play (q to quit).")
        if ans == "q":
            break
        balance += game(balance)
    
    print(f"You left with ${balance}.")

main()