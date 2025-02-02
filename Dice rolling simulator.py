import random
def dice_rolling():
 print("Welcome to dice rolling simulator.You can use to do what you want")
 dice_rolled = [1,2,3,4,5,6]
 rolled = random.choice(list(dice_rolled))
 if rolled == 1:
  print("The dice rolled",rolled)
 elif rolled == 2:
  print("The dice rolled",rolled)
 elif rolled == 3:
  print("The dice rolled",rolled)
 elif rolled == 4:
  print("The dice rolled",rolled)
 elif rolled == 5:
  print("The dice rolled",rolled)
 else:
  print("The dice rolled",rolled)
 Roll_again = str(input("Do you want to roll again"))
 if Roll_again == "Yes" or "yes":
     dice_rolling()
dice_rolling()           