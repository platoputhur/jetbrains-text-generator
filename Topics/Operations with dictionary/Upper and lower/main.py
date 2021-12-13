# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
# some_iterable = "Great loves too must be endured.".split()
new_dict = {item.upper(): item.lower() for item in some_iterable}
print(new_dict)
