# input function

name = input("what's your name ?\n")
print("Hello, "+name+"!!")

# swap the contents of the glasses

glass1 = "milk"
glass2 = "juice"

print("before : glass1 : ", glass1, ",", "glass2 : ", glass2)

newglass = ""

newglass = glass1
glass1 = glass2
glass2 = newglass


print("after : glass1 : ", glass1, ",", "glass2 : ", glass2)
