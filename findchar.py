list_one = ["Hello", "Lamp", "Moto", "Nurse", "Dolly"]
x = 0
char = "ll"
newlist = []

for x in range(0, len(list_one)):
    if list_one[x].find(char) != -1:
        newlist.append(list_one[x])
print newlist



