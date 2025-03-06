sample_json1=[{"globalControlId": 72, "value": 0, "controlId": 2},
              {"globalControlId": 77, "value": 3, "controlId": 7}]
sample_json2=[{"globalControlId": 77, "value": 3, "controlId": 7},
              {"globalControlId": 77, "value": 3, "controlId": 7}, # duplicity
              {"globalControlId": 72, "value": 0, "controlId": 2}]

# dictionaries are unhashable, let's convert to strings for sorting
sorted_1 = sorted([repr(x) for x in sample_json1])
sorted_2 = sorted([repr(x) for x in sample_json2])
print(sorted_1 == sorted_2)

# in case the dictionaries are all unique or you don't care about duplicities,
# sets should be faster than sorting
set_1 = set(repr(x) for x in sample_json1)
set_2 = set(repr(x) for x in sample_json2)
print(set_1 == set_2)