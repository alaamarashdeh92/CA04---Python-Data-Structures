# Q1 
# *******

# reads a number (n) from the user
n = int(input( "enter a integer: " ))

sum_n =0

for i in range(1, n+1): 
       sum_n += i
# print the sum of all numbers between 1 and n
print(f'The sum of all numbers between 1 and {n} = {sum_n}')