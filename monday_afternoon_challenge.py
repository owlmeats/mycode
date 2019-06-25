#!/usr/bin/env python3

#Monday Afternoon Challenge:
#Use the print function to return the following:
#"Hello Texas!"
#"Hi Sam, my name is _______.  WE are in Texas.  This is day 1"

#Use the following variables: 
#a = "Hello"
#b = "Texas"
#c = "Sam"
#d = "{Your name}"
#e = 1

#Use 2 different ways to print it out


a = "Hello"
b = "Texas"
c =  "Sam"
d = "JP"
e = 1


#print statement using .format syntax directly, and assigning to variable: 
print("{} {}!".format(a,b))

z = "{} {}!".format(a,b)
print(z)

#print statement using "f-string" syntax directly, and assigning to a variable:
print(f"{a} {b}!")
y = f"{a} {b}!"
print(y)



print("Hi {}, my name is {}.  We are in {}.  This is day {}".format(c,d,b,e))
x = "Hi {}, my name is {}.  We are in {}.  This is day {}".format(c,d,b,e)
print(x)






print(f"Hi {c}, my name is {d}.  We are in {b}.  This is day {e}")
w = f"Hi Sam, my name is {d}.  We are in Texas.  This is day {e}"
print(w)


