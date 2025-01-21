with open("Sample_File.txt","w") as file:
 file.write("Hello, I am aadhan of class 5.I am studying coding for 1 year.")
file.close()

with open("Sample_File.txt","r") as file:
 data = file.readlines()
 print("Words in the files are ......")
 for line in data:
  word = line.split()
  print(word)
file.close()

import os
print("Checking if my_file exists")
if os.path.exists("my_file.txt"):
 os.remove("my_file.txt")
else:
 print("The file does not exist.Creating new one")
my_file = open("my_file.txt","w")
my_file.write("Hello, I am aadhan of class 5.I am studying coding for 1 year.")
my_file.close()

os.remove("Sample_File.txt")
