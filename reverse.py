'''
9)Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
'''
# Input the list elements
elements = input().split()  # Read elements as a space-separated string

# Reverse the list
reversed_list = elements[::-1]

# Output the reversed list
print(" ".join(reversed_list))
