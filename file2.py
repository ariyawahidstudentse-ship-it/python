file_read = open('codingal.txt', 'r')
print("file in read mode -")
print(file_read.read())
file_read.close()

file_write = open('codingal.txt', 'w')
file_write.write("file in write mode . . .")
file_write.close()

file_append = open('codingal.txt', 'a')
file_append.write("\n file in append mode . . .")
file_append.write("Hi I am Penguin, I am 0.1 seconds years old.")
file_append.close()