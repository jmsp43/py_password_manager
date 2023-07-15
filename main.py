MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

# function responsible for collecting user input
def deposit():
      while True:
            amount = input("How much money would you like to deposit? $")
            if amount.isdigit():
                  amount = int(amount)
                  if amount > 0:
                        break
                  else: print("Amount must be greater than $0")
            else: print("Please enter a number")
      return amount

def getNumberOfLines():
      while True:
            lines = input("Enter number of lines you'd like to bet on (1-" + str(MAX_LINES) + ")? ") 
            if lines.isdigit():
                  lines = int(lines)
                  if 1 <= lines <= MAX_LINES:
                        break
                  else: print("Enter valid amount of lines.")
            else: print("Please enter a number")
      return lines

def getBet():
      print('hello')

def main():
      balance = deposit()
      lines = getNumberOfLines()
      print(balance, lines)

main()