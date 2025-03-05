import json

# …
def generate_diff(file1, file2):
    file_1 = json.load(open(file1))
    file_2 = json.load(open(file2))
    print(json.dumps(file_1, indent = 4))
    print(json.dumps(file_2, indent = 4))


    




