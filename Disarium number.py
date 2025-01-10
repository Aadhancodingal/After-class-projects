num = int(input("Enter a three digit number"))

num_str = str(num)

first_digit = int(num_str[0])

second_digit = int(num_str[1])

third_digit = int(num_str[2])
print("Number to be checked:",num)
first_digit = first_digit
second_digit = second_digit**2
third_digit = third_digit**3
if(first_digit + second_digit + third_digit == num ):
 print("Number is a disarium number")
else:
 print("Number is not a disarium number")    