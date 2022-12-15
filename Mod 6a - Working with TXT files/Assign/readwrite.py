#read file to list of lines and replace Aqua
def read(file):
    list_of_lines = []
    f = open(file,"r")
    word = f.readline()
    while(word!=""):
        if("Aqua" in word):
            list_of_lines.append("Azure #007fff")
        else:
            list_of_lines.append(word.strip())
        word = f.readline()
    return list_of_lines

#Modify
def modify(file,list_of_lines):
    f = open(file,"w")
    for line in list_of_lines:
        f.write(line + "\n")
    f.close()

file = "file.txt"
list_of_lines = read(file)
print(list_of_lines)
modify(file,list_of_lines)