import re

# your code here
template = '[B-N][aeiou]'
pet_name = input()
if re.match(template, pet_name) is not None:
    print("Suitable!")
