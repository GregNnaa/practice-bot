print("welcome to My first Bot!")
name = input("what is your name? ")
print("hello " + name + " thank you so much for coming in today")
services = """
Repairs

Formatting

data recovery

maintenace

IT support

Donate
 """
print( "here is a list of the services we offer \n\n" + services + " \n\nplease select a service and hit enter to proceed...")

order = input("kindly type what you want from our service list here, kindly know that the inputs are case sensitive, so you have to type exactly the way it appears. Thanks for understanding! \n\n")

print(name+"," + "\n you selected " + order + "\n\n thanks for the feedback, Our Bot is trying His best to contact a suitable Technician to attend to you")