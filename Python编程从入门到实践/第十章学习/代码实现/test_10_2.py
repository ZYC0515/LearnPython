#test_10_2.py
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))
