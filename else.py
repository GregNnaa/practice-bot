print("first python example in Visual studio coode")
name = input("what is your name? ")
print(name)
Age = input("how old are you? ")
print(Age)
MMN = input("what is your mother's maiden name?")
print(MMN)
Origin = input("where are you from? ")
if Origin == "Nigeria":
    print(Origin + "\n\n\nlucky you're eligible for this programme \n\n" + name )
else:
    print("sorry... " + name + "," + " the programme is not for people in your location")
    exit()

print(Origin)* 30