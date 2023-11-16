import random
lower = " abcdefghijklmnopqrstuvwxyz "
upper = " ABCDEFGHIJKLMNOPQRSTUVWXYZ "
symbole = " !@#$%^&*?></\ "
Number = "0123456789"

string = lower+upper+Number+symbole
length = int(input("Enter the passwoard length:"))
password = "".join(random.sample(string,length))
print("Your new password is :", password)
