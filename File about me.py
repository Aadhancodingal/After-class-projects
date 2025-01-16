file_read = open("Sample_file.txt","r")
print("File of coding = ")
print(file_read.read())
file_read.close()

file_write = open("Sample_file.txt","w")
print("File of my introduction -")
file_write.write("Hello, I am aadhan of class 5.I am studying coding for 1 year.\n")
file_write.close()

file_append = open("Sample_file.txt","a")
print("File of introduction and favourite subject")
file_append.write("My favourite subject is Math")
file_append.close