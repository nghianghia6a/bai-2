print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Input a string from the user
input_string = input("Enter a String: ")

# Initialize an empty dictionary to store character frequencies
char_count = {}

# Loop through each character in the string
for char in input_string:
    # Check if the character is already in the dictionary
    if char in char_count:
        char_count[char] += 1  # Increment the count if it exists
    else:
        char_count[char] = 1  # Initialize the
