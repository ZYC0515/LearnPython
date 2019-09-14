#test_10_1.py
file_name = 'learning_python.txt'
with open(file_name) as file_object:
    # contents = file_object.read()
    # print(contents)
    lines = file_object.readlines()
    # for line in lines:
    #     print(line.rstrip())

for line in lines:
    print(line.strip())
