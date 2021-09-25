file = open("text.txt")
c = ""
index = 0



characters = {"Celeste" : "c", "Levi" : "l", "Noah" : "n", "Elijah" : "e", "Father" : "f", "Empress Mirelle" : "em", "Emperor Lucius" : "el"}

print()
for line in file:
    if(line[0] == "["):
        for x in line[1:]:
            index += 1
            if x == "]":
                index +=2
                break
            c = c + x

        c = c.split(" ")[0]
        if(c in characters.keys()):
            print(characters[c], line[index:-1])
        else:
            print("\"" + c + "\" " + line[index:-1])

        c = ""
        index = 0

    else:
        print("\"" + line[:-1] + "\"")
print()
