with open("codingal.txt", "w") as file:
    file.write("I am a cat and I am a fetus.")
    file.close()

with open("codingal.txt", "r") as file:
    data = file.readlines()
    print("words in this file  are . . .")
    for line in data:
        word = line.split()
        print(word)

file.close()