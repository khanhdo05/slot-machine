MAX_LINES = 3 # all capitals for constants

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
            if lines > 0:
                break
            else:
                print("Number of lines must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return lines

def main():
    balance = deposit()

main()