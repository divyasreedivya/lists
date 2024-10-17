'''
10)Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''
# Input the list elements
elements = input().split()  # Read elements as a space-separated string

# Convert the list of strings to a list of integers
my_list = [int(element) for element in elements]

# Sort the list
my_list.sort()

# Output the sorted list
print(" ".join(map(str, my_list)))
