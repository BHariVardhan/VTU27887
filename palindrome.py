def is_palindrome(text):
    # Standardize input: convert to lowercase and remove non-alphanumeric characters
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    
    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]

# Testing the code
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("Hello"))    # Output: False
print(is_palindrome("A man, a plan, a canal: Panama")) # Output: True
