#1
import re

pattern = r"ab*"
test_strings = ["a", "ab", "abb", "ac", "ba", "b", "abbbbbb"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"Match: {string}")

#2

pattern = r"ab{2,3}$"
test_strings = ["a", "ab", "abb", "abbb", "abbbb"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"Match: {string}")

#3

pattern = r"[a-z]+_[a-z]+"
test_strings = ["hello_world", "test_example", "snake_case", "not_match", "Test_Case"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"Match: {string}")


#4

pattern = r"[A-Z][a-z]+"
test_strings = ["Hello", "World", "TestCase", "notMatch", "UPPER", "CamelCase"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"Match: {string}")


#5

pattern = r"a.*b$"
test_strings = ["ab", "acb", "axyzb", "a123b", "a", "b", "abc"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"Match: {string}")


#6

pattern = r"[ ,.]"
text = "Hello, world. Python is great!"

result = re.sub(pattern, ":", text)
print(result)

#7

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

print(snake_to_camel("hello_world_test"))

#8

pattern = r"(?=[A-Z])"
text = "HelloWorldPython"

result = re.split(pattern, text)
print(result)

#9

pattern = r"(?<!^)(?=[A-Z])"
text = "ThisIsAnExample"

result = re.sub(pattern, " ", text)
print(result)

#10

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

print(camel_to_snake("HelloWorldPython"))
