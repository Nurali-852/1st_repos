def all_true(tpl):
    return all(tpl)

tuple_data = (True, True, False)

if all_true(tuple_data):
    print("All elements are true.")
else:
    print("Not all elements are true.")
