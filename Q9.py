# Q 9 
# ********

first_list = [3, 6, 9, 12, 15, 18, 21]
second_list = [4, 8, 12, 16, 20, 24, 28]
results_list  = list ()

Even = first_list[1::2]
print("Element at Even-index positions from first_list")
print(Even)

odd = second_list[0::2]
print("Element at odd-index positions from second_list")
print(odd)

print("Print the results_list")
results_list.extend(Even)
print(results_list)
results_list.extend(odd)
print(results_list)