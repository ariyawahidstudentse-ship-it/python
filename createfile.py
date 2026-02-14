new_file = open("new_file.txt", "x")
new_file.close()

import os
print("Checking if my_files exist or not . . . ")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist.")

my_file = open("my_file.txt", "w")
my_file.write("I am a bengal potatia cat . ")
my_file.close()

os.remove("codingal.txt")

os.rmdir('Folder1')