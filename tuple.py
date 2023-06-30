#1. Write a Python program to create a tuple.
def create_tuple():
    my_tuple = (1, 2, 3, 'a', 'b', 'c')
    return my_tuple

# Example usage
result = create_tuple()
print("Tuple:", result)

#2.Write a Python program to create a tuple with different data types.
def create_mixed_tuple():
    my_tuple = (1, 'a', 3.14, True, [1, 2, 3])
    return my_tuple

# Example usage
result = create_mixed_tuple()
print("Tuple:", result)

#3.Write a Python program to unpack a tuple into several variables
def unpack_tuple():
    my_tuple = (1, 'a', 3.14)
    var1, var2, var3 = my_tuple
    return var1, var2, var3

# Example usage
result1, result2, result3 = unpack_tuple()
print("Unpacked variables:", result1, result2, result3)

#4.Write a Python program to convert a tuple to a string.
def convert_tuple_to_string(my_tuple):
    string = ''.join(str(item) for item in my_tuple)
    return string

# Example usage
my_tuple = (1, 'a', 3.14)
result = convert_tuple_to_string(my_tuple)
print("String:", result)

#5.Write a Python program to get the 4th element from the last element of a tuple
def get_fourth_from_last(my_tuple):
    fourth_from_last = my_tuple[-4]
    return fourth_from_last

# Example usage
my_tuple = (1, 2, 3, 4, 5, 6)
result = get_fourth_from_last(my_tuple)
print("Fourth element from the last:", result)

#6.Write a Python program to find repeated items in a tuple.
def find_repeated_items(my_tuple):
    repeated_items = []
    for item in my_tuple:
        if my_tuple.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items

# Example usage
my_tuple = (1, 2, 3, 2, 4, 1, 5, 6, 3, 4)
result = find_repeated_items(my_tuple)
print("Repeated items:", result)

#7.Write a Python program to slice a tuple
def slice_tuple(my_tuple, start, end):
    sliced_tuple = my_tuple[start:end]
    return sliced_tuple

# Example usage
my_tuple = (1, 2, 3, 4, 5, 6)
start_index = 2
end_index = 5
result = slice_tuple(my_tuple, start_index, end_index)
print("Sliced tuple:", result)

#8.Write a Python program to find the length of a tuple.
def find_tuple_length(my_tuple):
    length = len(my_tuple)
    return length

# Example usage
my_tuple = (1, 2, 3, 4, 5)
result = find_tuple_length(my_tuple)
print("Length of the tuple:", result)

#9.Write a Python program to reverse a tuple
def reverse_tuple(my_tuple):
    reversed_tuple = my_tuple[::-1]
    return reversed_tuple

# Example usage
my_tuple = (1, 2, 3, 4, 5)
result = reverse_tuple(my_tuple)
print("Reversed tuple:", result)

#10.Write a Python program to print a tuple with string formatting.
def print_tuple(my_tuple):
    formatted_tuple = ', '.join(str(item) for item in my_tuple)
    print("Tuple:", formatted_tuple)

# Example usage
my_tuple = (1, 2, 'Hello', 3.14)
print_tuple(my_tuple)












