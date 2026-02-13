file_read = open("codingal.txt", "r")
print("file in read mode . . .")
print(file_read.read())
file_read.close()

file_write = open("codingal.txt", "w")
print("file in write mode . . .")
file_write.write("I am a penguin and I am 100000 years old.")
file_write.close()

file_append = open("codingal.txt", "a")
print("file in append mode . . .")
file_append.write(" I am a penguin and I am 100000 years old.")
file_append.close()