# Q7
# *******


n = int(input( f"enter the age of person {1}: " ))
n1 = int(input( f"enter the age of person {2}: " ))
n2= int(input( f"enter the age of person {3}: " ))
if (n > n1 and n> n2):
    print(f"The oldest person is {1}")
elif (n1 > n and n1> n2):
    print(f"The oldest person is {2}")
else:
    print(f"The oldest person is {3}")

if (n < n1 and n < n2):
    print(f"The youngest  person is {1}")
elif (n1 < n and n1 < n2):
    print(f"The youngest  person is {2}")
else:
    print(f"The youngest  person is {3}")
