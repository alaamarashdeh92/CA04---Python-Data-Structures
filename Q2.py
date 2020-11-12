# Q2
# *******

# reads a number (n) from the user
n = int(input( "Enter the number" ))

# print the number of row
for n in range(1, n+1):

    # print the number of column
    for x in range (1,n+1):
      # print the number
        print(x, end=' ')
    
    print(" ")
         