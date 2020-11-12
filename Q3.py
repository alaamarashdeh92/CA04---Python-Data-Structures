# Q3 
# *******

# reads a number (n) from the user
n = int(input( "Enter the number:" ))

# print statement
print("multiplication Table of",n)

# The multiplication table of a given number
for i in range (1,11):
    print(n,"x",i,"=", n*i,",", end=' ')