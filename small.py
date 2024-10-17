'''
6)Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
1
'''

# Input the size of the list
size = int(input())

# Initialize an empty list
my_list = []

# Input the list elements
for _ in range(size):
    element = int(input())
    my_list.append(element)

# Find the smallest element
smallest = min(my_list)

# Output the smallest element
print(smallest)
