num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
print("Operations :" + "+","-","*","/" + "Type your answer")
def calculation(num1,num2):
 operation = str(input("Enter a option for the operation given above"))
 if(operation=="A"):
  print("Answer is:",num1+num2)
 elif(operation=="B"):
  print("Answer is:",num1-num2)
 elif(operation=="C"):
  print("Answer is:",num1*num2)
 else:    
   print("Answer is:",num1/num2)

calculation(num1,num2)