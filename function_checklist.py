print "Let's go through the steps of creating a function.\nAnswer 'Y' for yes or 'N' for no"
print "Defining your function:"

a = raw_input("Did you start your function definition with def?")
b = raw_input("Does your function name have only characters and _ (underscore) characters?")
c = raw_input("Did you put an open parenthesis ( right after the function name?")
d = raw_input("Did you put your arguments after the parenthesis ( separated by commas?")
e = raw_input("Did you make each argument unique (meaning no duplicated names)?")
f = raw_input("Did you put a close parenthesis and a colon ): after the arguments?")
g = raw_input("Did you indent all lines of code you want in the function four spaces? No more, no less.")
h = raw_input("Did you 'end' your function by going back to writing with no indent (dedenting we call it)?")

print "Calling your function:"

i = raw_input("Did you call/use/run this function by typing its name?")
j = raw_input("Did you put the ( character after the name to run it?")
k = raw_input("Did you put the values you want into the parenthesis separated by commas?")
l = raw_input("Did you end the function call with a ) character?")

checklist = [a, b, c, d, e, f, g, h, i, j, k, l]

for check in checklist:
    if check is 'Y':
        print "Hooray! Your function checklist is complete."
    else:
        print "Your functions checklist is incomplete. Please go through and complete: %r" % check
