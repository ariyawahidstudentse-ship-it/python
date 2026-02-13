file = open("codingal.txt", "r")
print(file.read())
file.close()

file = open("codingal.txt", "r")
print("\n read in parts \n")
print(file.read(8))
file.close()

file = open("codingal.txt", "a")
file.write(" Hi, I am penguin and I am  100000 years old.")
file.close()