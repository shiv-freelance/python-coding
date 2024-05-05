# input = "ha12{5}nu,3ma$n"
# output => separate numbers, chars, special chars

string = "ha12{5}nu,3ma$n"

# 1st approach.
nums = []            # List to store numbers
chars = []           # List to store characters
special_chars = []   # List to store special characters

for char in string:  # Iterate through each character in the string
    if char.isalpha():            # Check if the character is a letter
        chars.append(char)        # Add it to the list of characters
    elif char.isdigit():          # Check if the character is a digit
        nums.append(int(char))    # Convert it to an integer and add it to the list of numbers
    else:                         # If it's neither a letter nor a digit (i.e., special character)
        special_chars.append(char)  # Add it to the list of special characters


print(nums)
print(chars)
print(special_chars)
    

# 2nd approach
nums = [int(char) for char in string if char.isdigit()]
chars = [char for char in string if char.isalpha()]
special_chars = [char for char in string if not (char.isalpha() or char.isdigit())]

print(nums)
print(chars)
print(special_chars)
    