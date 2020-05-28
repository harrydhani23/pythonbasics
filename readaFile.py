#====== read a file=======
"""
myfile = open("fruit.txt")
content = myfile.read()
myfile.close()

#==== with keyword=======
with open("fruit.txt") as myfile:
    content = myfile.read()
    #myfile.close() - close method is not required here cos with keyword apply close implicity once we exit the with block

print(content)

#===write to a file=======
with open("vegetables.txt","w") as myfile:
    myfile.write("orange\nkidaan darling")
    myfile.write("\nanda")
with open("vegetables.txt","r") as myfile:
    content = myfile.read()

print(content)
"""
#=====adding content to exiting file====
with open("vegetables.txt","a+") as myfile:
    myfile.write("\nsheeka")
    myfile.seek(0)
    content = myfile.read()

print(content)
