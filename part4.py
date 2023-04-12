# Initialize the list
myNumbers = [5, 12, 8, 15, 4, 6, 10, 18, 20, 1]

# Define a function to print all elements of a list horizontally
def printList(lst):
    for num in lst:
        print(num, end=" ")

# Define a function to print all elements greater than 12 in a list horizontally
def printGreaterThan12(lst):
    for num in lst:
        if num > 12:
            print(num, end=" ")

# Print all elements of the list horizontally
print("All numbers in the list:")
printList(myNumbers)

# Print all numbers greater than 12 horizontally
print("\nNumbers greater than 12:")
printGreaterThan12(myNumbers)
