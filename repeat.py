'''
4 is not present in the given list
8)Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
'''
# Input the list elements
elements = input().split()  # Read elements as a space-separated string
my_list = [int(element) for element in elements]  # Convert to integers

# Input the value to count
value_to_count = int(input())

# Count the occurrences of the value in the list
count = my_list.count(value_to_count)

# Output the count
print(count)
