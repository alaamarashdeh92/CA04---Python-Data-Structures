# Q5
# *******

num = [1, 3, 5, 7, 9, 150, 160]
l= len(num)
for i in range(int(l/2)):
    n =num [i]
    num[i]=num[l-i-1]
    num[l-i-1]=n
print(num)


