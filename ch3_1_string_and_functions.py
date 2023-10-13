
my_string = "Hello, this is a sample string for demonstration purposes!"

string_length = len(my_string)
print(f"Length of the string: {string_length}")


lowercase_string = my_string.lower()
print(f"Lowercase string: {lowercase_string}")


uppercase_string = my_string.upper()
print(f"Uppercase string: {uppercase_string}")

substring_count = my_string.count('s')
print(f"Count of 's' in the string: {substring_count}")

substring_index = my_string.find('sample')
print(f"Index of 'sample' in the string: {substring_index}")

string_list = my_string.split(' ')
print(f"List of words in the string: {string_list}")

new_string = my_string.replace('Hello', 'Hi')
print(f"Updated string: {new_string}")

stripped_string = my_string.strip()
print(f"Stripped string: {stripped_string}")

is_alpha = my_string.isalpha()
print(f"Is the string alphabetic? {is_alpha}")

capitalized_string = my_string.capitalize()
print(f"Capitalized string: {capitalized_string}")
