with open("codingal.txt" )as fp:
    data1 = fp.read()

with open("sample_doc.txt")as fp:
    data2 = fp.read()


data1 += "\n"
data1 += data2
print("merging 2 file . . .")
with open("mergedfile.txt", "w") as fp:
    fp.write(data1)