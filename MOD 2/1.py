# Question 13(a)
# Count character frequency in a given string and store in a dictionary

input_str = "programming"

# Create an empty dictionary
char_count = {}

# Loop through each character in the string
for char in input_str:
    if char in char_count:
        char_count[char] += 1  # Increment count if character already in dictionary
    else:
        char_count[char] = 1   # Initialize count

# Output
print("Character frequency dictionary:")
print(char_count)
