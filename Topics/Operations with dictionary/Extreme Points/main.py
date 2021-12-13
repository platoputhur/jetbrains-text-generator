# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
min_dict = max_dict = {}
for index, item in enumerate(test_dict.items()):
    if index == 0:
        min_dict = max_dict = item
    min_key, min_value = min_dict
    max_key, max_value = max_dict
    key, value = item
    if value > max_value:
        max_dict = item
    if value < min_value:
        min_dict = item
min_key, _ = min_dict
max_key, _ = max_dict
print(f"min: {min_key}")
print(f"max: {max_key}")
