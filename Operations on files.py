file = open("Sample_file.txt","r")
print(file.read())
file.close()

file = open("Sample_file.txt","r")
print("First ten characters-")
print(file.read(10))
file.close()

file = open("Sample_file.txt","r")
print("First line")
print(file.readline())
file.close()

file = open("Sample_file.txt","r")
print("First 4 lines")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open("Sample_file.txt","r")
print("Loops in file")
for x in file:
 print(x)
file.close() 