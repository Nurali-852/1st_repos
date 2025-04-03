def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    return upper_count, lower_count

string = "Hello World"

upper, lower = count_case(string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
