import random

MAX_LINES=3
MAX_BET=1000
MIN_BET=1
ROW=3
REEL=3

symbols_list={ 
   "@":1 ,
   "#":3 ,
   "$":5 ,
   "&":7 ,
   "O":10

}
symbols_value={ 
   "@":5 ,
   "#":4 ,
   "$":3 ,
   "&":2 ,
   "O":1

}

def check_winnings(reels,lines,bet,values):
   winnings=0
   winning_lines=[]
   for line in range(lines):
      symbol=reels[0][line]
      for reel in reels:
         symboltocheck=reel[line]
         if symbol!=symboltocheck:
            break
      else:
         winnings+=values[symbol]*bet
         winning_lines.append(line+1)
   
   return winnings,winning_lines

def spin(rows,reeels,symbols):
   all_symbols=[]
   for symbol , symbols_list in symbols.items():
      for _ in range(symbols_list):
         all_symbols.append(symbol)
   reels=[]
   for _ in range(reeels):
      reel=[]
      present_symbols=all_symbols[:]
      for _ in range(rows):
         value=random.choice(present_symbols)
         present_symbols.remove(value)
         reel.append(value)

      reels.append(reel)

   return reels

def print_slot_machine(reels):
   for row in range(len(reels[0])):
      for i , reel in enumerate(reels):
         if i!=len(reels)-1:
            print(reel[row], end=" | ")
         else:
            print(reel[row], end="")
      print()      
      



def dep():
    while True:
        amt=input("How much ? ₹")
        if amt.isdigit():
          amt=int(amt) 
          if amt > 0 :
             break
          else:
             print("Amount cannot be zero")
        else:
           print("Enter a number") 
    return amt

def number_of_lines():
    while True:
        lines=input("Enter the number of lines to bet on from 1 to " + str(MAX_LINES)+" " )
        if lines.isdigit():
          lines=int(lines) 
          if 1<=lines<=MAX_LINES :
             break
          else:
             print("Enter a valid number")
        else:
           print("Enter a number") 
    return lines

def bet1():
    while True:
        amt=input("How much would you like to bet on each line? ₹")
        if amt.isdigit():
          amt=int(amt) 
          if MIN_BET<=amt<=MAX_BET :
             break
          else:
             print(f"Amount should be between ₹{MIN_BET} - ₹{MAX_BET}")
        else:
           print("Enter a number") 
    return amt

def spin1(balance):
   lines=number_of_lines()
   while True:

     bet=bet1()
     total_bet=bet*lines
      
     if total_bet > balance:
        print(f"You  do not have enough balance.Your current balance is ₹{balance}")
     else:
        break
  
   print(f"Your total bet is ₹{total_bet}")

   slots=spin(ROW,REEL,symbols_list)
   print_slot_machine(slots)
   winnings, winning_lines=check_winnings(slots,lines,bet,symbols_value)
   print(f"YOU WON ₹{winnings}.")
   print(f"YOU WON ON LINES:", *winning_lines)
   return winnings-total_bet

def main():
   balance=dep()
   while True:
      print(f"Current balance is ₹{balance}")
      spin2=input("Press enter to spin  or hit q to quit")
      if spin2=="q":
         break
      balance+=spin1(balance)
   print(f"YOU LEFT WITH ₹{balance}")

   
   
main()   